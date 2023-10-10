# Deploy a Multi-tier Application on Kubernetes
Build web 3 Tiers.
![web_3_tier](./3_K8s/imagek8s/web-3-tier.png)
Sử dụng 3 images trong dockerhub:

Database: huong195/k8s_db_image:v1.0
Backend: huong195/k8s_web_image:v1.0
Frontend: huong195/k8s_nginx_image:v1.0
## quá trình thực hiện 
### Install Kind and create Cluster
```c
[ $(uname -m) = x86_64 ] && curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.19.0/kind-linux-amd64
[ $(uname -m) = aarch64 ] && curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.19.0/kind-linux-arm64
chmod +x ./kind
sudo mv ./kind /usr/local/bin/kind
kind create cluster --image kindest/node:v1.22.0
```
```c
docker ps
```
```c
docker exec -it kind-control-plane bash
```
### Create the database deployment (Mongodb) and database service.
#### Create the database deployment
```c
apiVersion: apps/v1
kind: Deployment
metadata:
  name: db-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: database
  template:
    metadata:
      labels:
        app: database
    spec:
      containers:
      - name: db
        image: huong195/k8s_db_image:v1.0
        ports:
        - containerPort: 27017
```
#### Create the database service:
```c
apiVersion: v1
kind: Service
metadata:
  name: db
spec:
  selector:
    app: database
  ports:
  - protocol: TCP
    port: 27017
    targetPort: 27017
  type: NodePort
```
### Create the backend deployment and backend service
### Create the backend deployment
```c
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api-deployment
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
      - name: flask1
        image: huong195/k8s_web_image:v1.0
        ports:
        - containerPort: 9090
```
### Create the backend service
```c
apiVersion: v1
kind: Service
metadata:
  name: flask1
spec:
  selector:
    app: api
  ports:
  - protocol: TCP
    port: 9090
    targetPort: 9090

```
### Create the web deployment (Nginx) and web service
### Create the web deployment (Nginx)
```c
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx-container
        image: huong195/k8s_nginx_image:v1.0
        ports:
        - containerPort: 80
```
### Create the web service
```c
> apiVersion: v1     
kind: Service
metadata:
  name: nginx-service
spec:
  selector:
    app: nginx
  ports:
  - protocol: TCP
    port: 80
    targetPort: 80
    nodePort: 30000
  type: NodePort
```
Result
Lấy danh sách pod bằng lệnh
```c
$ kubectl get pod 
```
![pod](./3_K8s/imagek8s/pod.png)
Lấy danh sách deployment bằng lệnh
```c
$ kubectl get deployment
``` 
![deployment](./3_K8s/imagek8s/deployment.png)
Lấy danh sách Service bằng lệnh
```c
$ kubectl get service
```
![service](./3_K8s/imagek8s/service.png)

Kiểm tra các node
```c
$ kubectl get nodes -o wide
```
![ip](./3_K8s/imagek8s/ip.png)

Có được địa chỉ ip ta tiến hành truy cập http://172.18.0.2:30000 trên trình duyệt
hệ thống trae về kết quả :
![result](./3_K8s/imagek8s/result.png)