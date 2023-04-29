Q: What are the differences between these instructions?

- ARG vs ENV:

ARG: được sử dụng để truyền các giá trị đến trong quá trình xây dựng image

ENV: được sử dụng để thiết lập các biến môi trường trong container.


Ví dụ:

// Dockerfile sử dụng ARG để truyền tham số vào trong quá trình build image

ARG NODE_VERSION=14


// Sử dụng ENV để định nghĩa các biến môi trường trong container

ENV APP_HOME=/usr/src/app

ENV NODE_ENV=production


- COPY vs ADD:

COPY: chỉ sao chép các tệp tin từ host machine vào trong image Docker.


ADD: ngoài việc sao chép các tệp tin từ host machine vào trong image Docker như COPY, ADD còn có thể giải nén các tệp tin tar và có thể tải xuống và giải nén các tệp tin từ URL.


Tốc độ: ADD có tốc độ chậm hơn vì có thể phải giải nén các tệp tin và cũng cần nhiều bộ nhớ hơn để xử lý các tệp tin nén.


Ví dụ:

// Sử dụng COPY để sao chép file index.js vào trong image

COPY index.js /app/

// Sử dụng ADD để tải và giải nén file từ URL và sao chép vào trong image

ADD https://example.com/file.tar.gz /app/


- CMD vs ENTRYPOINT:

CMD: thực hiện lệnh mặc định khi chúng ta khởi tạo container từ image, lệnh mặc định này có thể được ghi đè từ dòng lệnh khi khởi tạo container.

ENTRYPOINT: khá giống CMD đều dùng để chạy khi khởi tạo container, nhưng ENTRYPOINT không thể ghi đè từ dòng lệnh khi khi khởi tại container.
...



