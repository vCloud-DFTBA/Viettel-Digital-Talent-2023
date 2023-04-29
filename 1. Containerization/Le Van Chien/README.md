# VDT Containerization homework
My very very very first web app, and docker usage.
## So sánh các instructions trong dockerfile
---
1. ARG và ENV
- `ARG`: định nghĩa các biến có thể được gọi trong Dockerfile trong quá trình build image, nhưng không thể truy cập được sau đó.
- `ENV`: ngược lại, ENV định nghĩa các biến môi trường có thể được sử dụng trong container lúc runtime. Các biến cũng này có thể được override sau khi run container.
2. COPY và ADD
- `COPY`: sử dụng để sao chép các file và thư mục vào container.
- `ADD`: ADD cũng tương tự COPY, nhưng có thêm một số tính năng khác như giải nén các file (e.g., `.tar`, `.zip`) và tải file từ URLs
3. ENTRYPOINT và CMD
- `ENTRYPOINT`: chỉ định các câu lệnh sẽ chạy khi run container 
- `CMD`: chỉ định các arguments sẽ truyền vào `ENTRYPOINT`, hoặc chỉ định câu lệnh mặc định sẽ chạy nếu không có `ENTRYPOINT` nào được định nghĩa. Các giá trị được định nghĩa bởi `CMD` có thể được override bằng cách truyền vào argument trong lệnh `docker run` 

## Three-tier web app 
---
### Cài đặt
```
docker compose up
```
1. nginx

- Base image: nginx:1.22.0-alpine
- Mapping port 8080 của host

2. flask app
- Base image: python:3.9-slim, có thể sử dụng tag :3.9-alpine để giảm kích thước image, tuy nhiên quá trình cài đặt các python package sẽ phức tạp và lâu hơn.
3. database
- Base image: mongo:5.0
- Mount với thư mục /db
### Kết quả 
Tại http://localhost:8080/

![](images/localhost8080.png)