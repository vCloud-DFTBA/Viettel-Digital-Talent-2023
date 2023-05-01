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
Các images trên Dockerhub được sử dụng:
* nginx 1.22.0-alpine
* mongo 5.0-focal
* python 3.9-alpine (48.16 MB)

Project này chỉ build một image **app** duy nhất dựa trên image **python 3.9-alpine**. Kích thước image **app** sau khi build là **64.89 MB** lớn hơn image **python 3.9-alpine** (48.16 MB) không đáng kể. Hai images **nginx** và **mongo** được sử dụng trực tiếp từ Dockerhub và hoàn toàn không cần build mới.

```bash
docker compose up --build
```

Kết quả là một Json Object chứa họ tên của các sinh viên được trả về tại địa chỉ:
**<http://localhost:80/students>**