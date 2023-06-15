## Bài tập kuberneste

*Người thực hiện: Trần Mạnh Dũng*

#### 1. Dựng cụm k8s cluster
 - Ở bài tập về nhà này thì em tự dựng một cụm k8s single node chứ không dùng container kind để làm môi trường làm bài tập.
 - Một số hình ảnh thông tin cluster:

![alt](images/cluster-info.png)

![alt](images/frontend-5.png)
#### 2. Triển khai cơ sở dữ liệu
- Do cơ sở dữ liệu cần có các trường thông tin để có thể đăng nhập cơ sở dữ liệu và các trường thông tin này không thể để giá trị cụ thể mà cần phải được mã hóa. Em xây dựng `kind: Secret` để lưu trữ các giá trị này.
- Các giá trị cần được mã hóa dưới dạng base64 bằng câu lệnh trong hệ điều hành ubuntu `echo -n <value> | grep base64` như sau:

    ![alt](images/db-3.png)
- Mã nguồn Secret:

```yml
apiVersion: v1
kind: Secret
metadata:
  name: db-secret
type: Opaque
data:
  db-user: bXl1c2VybmFtZQ==
  db-password: bXlwYXNzd29yZA==
  db-name: bXlkYg==
```
- Tiếp theo em xây dựng file cấu hình gồm cả kind `Deployment` và `Service`

```yml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: db-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: db-pod
  template:
    metadata:
      labels:
        app: db-pod
    spec:
      containers:
      - name: db-container
        image: tranmanhdung582001/db
        resources:
          limits:
            memory: "128Mi"
            cpu: "500m"
        ports:
        - containerPort: 5432
        env:
          - name: POSTGRES_USER
            valueFrom:
              secretKeyRef:
                name: db-secret
                key: db-user
          - name: POSTGRES_PASSWORD
            valueFrom:
              secretKeyRef:
                name: db-secret
                key: db-password
          - name: POSTGRES_DB
            valueFrom:
              secretKeyRef:
                name: db-secret
                key: db-name
        volumeMounts:
          - mountPath: /var/lib/postgresql/data
            name: postgredb
      volumes:
        - name: postgredb


---
apiVersion: v1
kind: Service
metadata:
  name: db-service
spec:
  selector:
    app: db-pod
  ports:
  - port: 5432
    targetPort: 5432
  type: ClusterIP

```
- Với database em chỉ chọn `replicas: 1` bởi vì đối với hệ thống cơ sở dữ liệu sẽ không thể xây dựng cân bằng tải như backend hay frontend bởi vì còn liên quan đến vấn đề đồng bộ dữ liệu ở các pod database. Thông thường với hệ thống cơ bản, cơ sở dữ liệu nếu scale thì sẽ có 1 pod db chính (primary) có nhiệm vụ write hoặc có cả read data. Và thêm vào đó là các pod db phụ (stand by) có nhiệm vụ read data. Giải quyết vấn đề đồng bộ dữ liệu giữa pod primary với các pod stand by thì sau 1 khoảng thời gian ngắn thì pod primary sẽ tạo và gửi bản replicate data sang cho các pod stand by.
- `Service` sẽ có `type: ClusterIP` để đảm bảo là chỉ có các pod trong cluster này giao tiếp được với pod database.
- Một số hình ảnh kết quả:

![alt](images/db-1.png)

![alt](images/db-2.png)
#### 3. Triển khai backend
#### 4. Triển khai frontend
### Tổng kết