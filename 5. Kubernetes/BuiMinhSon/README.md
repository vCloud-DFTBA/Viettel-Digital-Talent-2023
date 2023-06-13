# Kubernetres
## Bùi Minh Sơn
### 1. Tổng quan về Kubernetes
- Tổng quan về kiến trúc,các khái niêm được tổng hợp trong Repositori sau https://github.com/bmson7112/TTS-VTNet/issues

### 2. Triển khai 3-tier app trên Kubernetes

#### 2.1. Tạo cụm Kubernetes 

- Thực hiện các câu lệnh sau để cài đặt Kind ( ở đây ta sử dụng Kind để tạo các cluster)
```sh
[ $(uname -m) = x86_64 ] && curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.19.0/kind-linux-amd64
[ $(uname -m) = aarch64 ] && curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.19.0/kind-linux-arm64
chmod +x ./kind
sudo mv ./kind /usr/local/bin/kind
```
- Vì muốn triển khai cụm có nhiều Node nên em sẽ tạo  file cấu hình để dựng cụm là `workerNodes.yaml` có nội dung như sau:

```yaml
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
- role: control-plane
- role: worker
```
- Sau khi chạy lệnh tạo cluster, ta có kết quả như hình 

![alt](./images/create-cluster.png)

#### 2.2. Tạo các deployment và service của từng thành phần 
##### 2.2.1. Database
- Sử dụng mã hóa base64 để mã hóa tài khoản mà mật khẩu mongoDB

![alt](./images/create-secret.png)
- Sau đó thêm mã trên vào file `db-secret.yaml`, đây chính là file cấu hình secret của mongoDB

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: db-secret
type: Opaque
data:
  mongo-user: cm9vdA==
  mongo-password: cGFzc3dvcmQ=
```
- Triển khai deployment và service cho database mongoDB, ở đây em gộp chung chúng lại vào file `db.yaml` như bên dưới: 

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: db
  labels:
    app: mongodb
spec:
  replicas: 1
  selector:
    matchLabels:
      app: mongodb
  template:
    metadata:
      labels:
        app: mongodb
    spec:
      containers:
        - name: mongodb
          image: minhson7112/sonbm-db:latest
          ports:
            - containerPort: 27017
          env:
            - name: MONGO_INITDB_ROOT_USERNAME
              valueFrom:
                secretKeyRef:
                  name: db-secret
                  key: mongo-user
            - name: MONGO_INITDB_ROOT_PASSWORD
              valueFrom:
                secretKeyRef:
                  name: db-secret
                  key: mongo-password

---

apiVersion: v1
kind: Service
metadata:
  name: db
spec:
  selector:
    app: mongodb
  ports:
    - protocol: TCP
      port: 27017
      targetPort: 27017
  type: NodePort 
```
- Apply file yaml secret, deployment, service của database lên cluster ta có kết quả:

![alt](./images/apply-db.png)

##### 2.2.2. Backend (api)
- Tương tự Database, em cũng gộp cấu hình deployment, service của backend vào trong cùng 1 file `api.yaml` như sau:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api
spec:
  replicas: 3
  selector:
    matchLabels:
      app: api
  template:
    metadata:
      labels:
        app: api
    spec:
      containers:
        - name: api
          image: minhson7112/sonbm-api:v1.1.4
          ports:
            - containerPort: 5000
          env:
            - name: MONGO_HOST
              value: "10.96.126.56"
            - name: MONGO_USERNAME
              valueFrom:
                secretKeyRef:
                  name: db-secret
                  key: mongo-user
            - name: MONGO_PASSWORD
              valueFrom:
                secretKeyRef:
                  name: db-secret
                  key: mongo-password

---

apiVersion: v1
kind: Service
metadata:
  name: api
spec:
  selector:
    app: api
  ports:
  - protocol: TCP
    port: 5000
    targetPort: 5000
    nodePort: 30001
  type: NodePort
```
- Apply file yaml deployment, service của backend lên cluster ta có kết quả:

![alt](./images/apply-backend.png)