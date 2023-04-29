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
## 4. Web-app
Build một ứng dụng web sử dụng:
* nginx 1.22.0-alpine
* mongodb 5.0
* python 3.9

Sử dụng based-image python-alpine với kích thước rất nhỏ (48.16 MiB), sau khi build image ứng dụng flask thu được image mới với kích thước (64.89 Mib) lớn hơn kích thước ban đầu không đáng kể.