# Containerization

## Phần 1: Trả lời câu hỏi lý thuyết

### 1. How many optimization tricks used in this Dockerfile?


```Dockerfile
FROM alpine:3.5

# Install python and pip
RUN apk add --update py2-pip

# upgrade pip
RUN pip install --upgrade pip

# install Python modules needed by the Python app
COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

# copy files required for the app to run
COPY app.py /usr/src/app/
COPY templates/index.html /usr/src/app/templates/

# tell the port number the container should expose
EXPOSE 5000

# run the application
CMD ["python", "/usr/src/app/app.py"]
```

* Có một số  thủ thuật để tối ưu hóa Dockerfile trên, đó là:
    - Sử dụng base image là Alpine Linux, khá là nhẹ để giảm kích thước của image
    - Copy và cài đặt file requirement.txt để giới hạn và chỉ tải về các package cần thiết của Python
    - Sử dụng `--no-cache-dir` với lệnh `pip install` để giảm kích thước bộ nhớ cache

### 2. What are the differences between these instructions?
>ARG vs ENV
- `ARG` dùng để truyền giá trị vào trong quá trình build của Docker image, và giá trị của biến `ARG` có thể được truyền từ command line khi build image. Ngoài ra, các biến `ARG` chỉ tồn tại trong quá trình build và không được lưu trữ trong container khi chạy
- `ENV` được sử dụng để thiết lập các biến môi trường trong container. Những biến này có thể được sử dụng trong quá trình chạy của container. `ENV` có thể được định nghĩa trong Dockerfile hoặc thông qua lệnh docker run

>COPY vs ADD
- COPY nhận một src và destination. Nó chỉ cho phép ta sao chép một tệp cục bộ hoặc thư mục từ  máy vào Docker image
- ADD cũng cho phép bạn làm điều đó nhưng nó cũng hỗ trợ các chức năng. Đầu tiên, ta có thể sử dụng một URL thay vì một tệp/thư mục cục bộ. Thứ hai, ta cũng có thể trích xuất file tar từ nguồn trực tiếp vào đích. Điều này có nghĩa là nó có thể giải nén nội dung của file tar vào trong hệ thống file của container
- Tuy nhiên, COPY vẫn được ưa chuộng sử dụng hơn nhờ tính minh bạch của mình, sẽ chỉ sử dụng ADD khi thực sự cần tới các tính năng bổ sung của nó

>CMD vs ENTRYPOINT
- CMD và ENTRYPOINT được sử dụng để chỉ định lệnh mà container sẽ chạy khi được bật. Điểm khác biệt chính giữa CMD và ENTRYPOINT là cách chúng xử lý các đối số được truyền vào khi container được khởi động
- CMD được sử dụng để chỉ định một lệnh mặc định cho container. Nếu một lệnh khác được cung cấp khi container chạy, nó sẽ thay thế CMD ban đầu. CMD thường được sử dụng để chỉ định lệnh mặc định cho container và đơn giản hóa việc chạy container.
- ENTRYPOINT được sử dụng để chỉ định một lệnh chính cho container và đối số được cung cấp khi khởi động container sẽ được truyền vào như đối số cho lệnh chính đó. ENTRYPOINT thường được sử dụng để chỉ định một lệnh chính không thể thay đổi và cung cấp các đối số tùy ý khi container được khởi động

## Phần 2: Thiết lập ứng dụng web 3 tầng hiển thị thông tin sinh viên

### 1. Yêu cầu:
- Sử dụng các base image :  
     - nginx:1.22.0-alpine
     - python:3.9
     - mongo:5.0
- Kích cỡ của image sau khi build chênh lệch không quá lớn so với base image
### 2. Thực hành
