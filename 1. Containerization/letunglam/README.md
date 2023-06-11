# Containerization
## 1. ARG và ENV
Giống nhau:
* Dùng để khai báo các biến môi trường trong quá trình build Docker image

Khác nhau:
* Các biến được định nghĩa trong ARG có giá trị khi Container được khởi chạy
* Các biến trong ENV chỉ có giá trị trong quá trình build image
## 2. ADD và COPY
Giống nhau:
* Được dùng để sao chép một file hoặc một folder từ máy host vào trong container

Khác nhau:
* ADD có thêm hỗ trợ URL, giải nén tập tin tải về từ URL
* COPY chỉ sao chép file, folder
## 3. CMD và ENTRYPOINT
* CMD thực hiện lệnh mặc định khi chúng ta khởi tạo container từ image, lệnh mặc định này có thể được ghi đè từ dòng lệnh khi khởi tại container.
* ENTRYPOINT khá giống CMD đều dùng để chạy khi khởi tạo container, nhưng ENTRYPOINT không thể ghi đè từ dòng lệnh khi khi khởi tại container.
## 4. WEB-APP
Triển khai một 3-tier web application sử dụng Docker Compose. Đóng gói các services thành các images và tối ưu kích thước của các images.

Các images trên Dockerhub được sử dụng:
* nginx 1.22.0-alpine
* mongo 5.0-focal
* python 3.9-alpine **(48.16 MB)**

Project này chỉ build **một image app** duy nhất dựa trên image **python 3.9-alpine**.
- Kích thước image trước khi build: **48.16 MiB**
- Kích thước image **app** sau khi build: **64.89 MiB**

Docker-compose file:
```yaml
version: '3.8'

services:
  app:
    build:
      context: app
    ports: 
      - "5000"
    links:
      - db

  nginx:
    image: nginx:1.22.0-alpine
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
    depends_on:
      - app
      - db
    ports:
      - "80:80"

  db:
    image: mongo:5.0-focal
    # hostname: mongodb
    container_name: mongodb-server
    restart: always
    # environment:
    #     MONGO_INITDB_ROOT_USERNAME: <admin-user>
    #     MONGO_INITDB_ROOT_PASSWORD: <admin-password>
    #     MONGO_INITDB_DATABASE: <database to create>
    ports:
        - 27017:27017
    volumes:
        - ./mongo-init.js:/docker-entrypoint-initdb.d/mongo-init.js:ro
```

Image **app** [Dockerfile](./app/Dockerfile):
```Dockerfile
FROM python:3.9-alpine

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt --no-cache-dir

CMD gunicorn --bind 0.0.0.0:5000 wsgi:app
```

[mong-init.js](./mongo-init.js) (sample):
```js
db = db.getSiblingDB('students_db');

db.createCollection('names');

db.names.insertMany([
    {
        name: 'Bui Minh Son',
        dob: '2002',
    },
    {
        name: 'Dao Dai Hiep',
        dob: '2001',
    },
]);
```

[nginx.conf](./nginx.conf):
```conf
events {
    worker_connections 1000;
}

http {
    server {
        listen 80;

        location / {
            proxy_pass http://app:5000;
        }
    }
}
```

Build images:
```bash
docker compose up --build
```

History của image **app**:
```bash
docker history letunglam_app
```
![image](./images/app-history.png)


Kết quả là một **Json Object** chứa họ tên của các sinh viên được trả về tại địa chỉ:
**<http://localhost:80/students>**
![image](./images/list-students.png)