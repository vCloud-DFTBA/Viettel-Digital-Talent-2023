 ## Q: What are the differences between these instructions?

**1. ARG vs ENV:**  
- ARG: được sử dụng để truyền các giá trị đến trong quá trình xây dựng image  
- ENV: được sử dụng để thiết lập các biến môi trường trong container.  

- Ví dụ:  
> // Dockerfile sử dụng ARG để truyền tham số vào trong quá trình build image  
> ARG NODE_VERSION=14  

> // Sử dụng ENV để định nghĩa các biến môi trường trong container  
> ENV APP_HOME=/usr/src/app  
> ENV NODE_ENV=production  

**2. COPY vs ADD:**  
- COPY: chỉ sao chép các tệp tin từ host machine vào trong image Docker.  
- ADD: ngoài việc sao chép các tệp tin từ host machine vào trong image Docker như COPY, ADD còn có thể giải nén các tệp tin tar và có thể tải xuống và giải nén các tệp tin từ URL.  
- Tốc độ: ADD có tốc độ chậm hơn vì có thể phải giải nén các tệp tin và cũng cần nhiều bộ nhớ hơn để xử lý các tệp tin nén.  

- Ví dụ:  
> // Sử dụng COPY để sao chép file index.js vào trong image  
> COPY index.js /app/  
> 
> // Sử dụng ADD để tải và giải nén file từ URL và sao chép vào trong image  
> ADD https://example.com/file.tar.gz /app/  

**3. CMD vs ENTRYPOINT:**  
- CMD: CMD được sử dụng để định nghĩa lệnh mặc định khi khởi chạy container, nó có thể được ghi đè khi chạy lệnh docker run. Nếu một Dockerfile có nhiều hơn một chỉ thị CMD, chỉ thị CMD cuối cùng được sử dụng.  
- ENTRYPOINT: ENTRYPOINT được sử dụng để định nghĩa lệnh hoặc script được thực thi khi khởi chạy container và truyền các tham số vào. ENTRYPOINT thường được sử dụng để định nghĩa một ứng dụng chạy khi container được khởi động. Nếu một Dockerfile có nhiều hơn một chỉ thị ENTRYPOINT, tất cả các chỉ thị được thêm vào như là một danh sách được thực thi và chỉ thị cuối cùng được thực hiện là câu lệnh chính.  
- Ví dụ:  
>CMD ["echo", "Xin chào thế giới"]  
>CMD ["echo", "Hello World"]  
> Khi chạy docker run thì câu lệnh echo "Hello World" sẽ được thực thi còn câu lệnh ở trên sẽ bị bỏ qua.   

>ENTRYPOINT ["echo", "Xin chào thế giới"]  
>ENTRYPOINT ["echo", "Hello World"]  
>Khi chạy docker run thì tất cả câu lệnh sẽ được thực thi. Nhưng chỉ thị echo "Hello World" sẽ là lệnh chính khi chạy docker run còn ENTRYPOINT trước đó sẽ bị ghi đè.  





