# Docker instructions
## ARG vs ENV
* Cả hai instruction ARG và ENV đều được sử dụng để định nghĩa các biến trong quá trình xây dựng Docker image, tuy nhiên chúng có sự khác nhau như sau:
- ARG: Được sử dụng để định nghĩa các biến môi trường trong quá trình xây dựng Docker image và chúng được đặt giá trị trong quá trình build. Điều này có nghĩa là giá trị của ARG chỉ có hiệu lực trong quá trình build và không có giá trị trong quá trình runtime của container.
- ENV: Được sử dụng để định nghĩa các biến môi trường trong quá trình runtime của container. Chúng được đặt giá trị trong quá trình build và được sử dụng trong quá trình runtime của container. Điều này có nghĩa là giá trị của ENV có thể được truyền vào container và sử dụng trong quá trình chạy của nó.
- Ví du: 
# sử dụng ARG trong Dockerfile
ARG APP_PORT=5000
ENV APP_PORT=$APP_PORT
EXPOSE $APP_PORT

- # sử dụng ENV trong Dockerfile
ENV APP_PORT=5000
EXPOSE $APP_PORT
- Ở ví dụ trên, cả hai instruction đều định nghĩa biến môi trường APP_PORT và sử dụng nó trong lệnh EXPOSE. Tuy nhiên, với ARG, giá trị của nó chỉ có hiệu lực trong quá trình build và được truyền vào ENV để sử dụng trong quá trình runtime của container. Trong khi đó, với ENV, giá trị của nó được sử dụng trực tiếp trong quá trình runtime của container.

## COPY vs ADD
* Cả hai instruction COPY và ADD trong Dockerfile đều được sử dụng để sao chép file từ máy host vào bên trong container Docker, tuy nhiên chúng có sự khác biệt như sau:

* Giống nhau:
- Cả hai đều hỗ trợ sao chép một tập tin hoặc một thư mục từ host vào trong container Docker.
- Cả hai đều hỗ trợ sử dụng đường dẫn tương đối và đường dẫn tuyệt đối để chỉ định nguồn và đích.

* Khác biệt:
- ADD có thể xử lý các URL ngoài cùng host, tải về và giải nén chúng tự động trong quá trình sao chép, trong khi đó COPY chỉ hỗ trợ sao chép các file và thư mục từ host tới container.
- ADD còn hỗ trợ các tính năng bổ sung như giải nén tập tin tar hoặc tải xuống từ URL SSL. Trong khi đó, COPY chỉ có thể sao chép file và thư mục.
- COPY được coi là an toàn hơn vì nó rõ ràng và đơn giản hơn ADD, trong khi ADD có thể làm cho quá trình build của Dockerfile phức tạp hơn.
- Do đó, COPY là một instruction phổ biến được sử dụng trong hầu hết các trường hợp, trong khi ADD thường được sử dụng khi cần giải nén hoặc tải xuống tập tin trong quá trình sao chép.
## CMD vs ENTRYPOING

* Cả hai lệnh CMD và ENTRYPOINT đều được sử dụng để chỉ định một lệnh mà container sẽ chạy khi được khởi động. Tuy nhiên, chúng có những sự khác biệt sau:
- CMD: chỉ định một lệnh mặc định mà container sẽ chạy khi không có lệnh được chỉ định trong lệnh khởi chạy. Nếu có nhiều lệnh được chỉ định, chỉ có lệnh cuối cùng được thực thi. CMD có thể được ghi đè khi khởi động container bằng cách sử dụng tham số docker run hoặc bằng cách sử dụng một Docker Compose file.
- ENTRYPOINT: chỉ định lệnh cố định sẽ được thực thi khi container được khởi động. Nếu có các tham số được truyền vào khi khởi động container, chúng sẽ được thêm vào cuối của lệnh được chỉ định trong ENTRYPOINT. ENTRYPOINT được sử dụng để chỉ định một chương trình hoặc một script như một entrypoint cho container và không bị ghi đè bởi các tham số khác.

- Ví dụ, nếu trong Dockerfile có lệnh CMD ["python3", "server.py"], khi container được khởi động, nếu không có lệnh được truyền vào, container sẽ thực thi lệnh python3 server.py. Nếu chạy container với lệnh docker run myapp python3 test.py, lệnh python3 test.py sẽ được thực thi thay vì lệnh CMD.Trong khi đó, nếu sử dụng ENTRYPOINT ["python3"], container sẽ luôn chạy lệnh python3, và nếu chạy container với lệnh docker run myapp test.py, lệnh được thực thi sẽ là python3 test.py.

