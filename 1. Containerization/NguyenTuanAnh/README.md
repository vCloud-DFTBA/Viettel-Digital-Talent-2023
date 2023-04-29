# Viettel - Digital-Talent-2023: Cloud - Pratice 1
# Task: docker, docker-compose
# Mục lục
# I. Overview
## 1. Containerization
### 1.1. Containerization
- **Containerization** là giải pháp ảo hóa, tự động hóa thế hệ mới kế tiếp sau Hypervisor Virtualization và được các hãng công nghệ nổi tiếng hàng đầu thế giới như **Google, Facebook, Amazon** áp dụng rộng rãi, đem lại hiệu quả đột phá với các ưu điểm vượt trội về tốc độ triển khai, khả năng mở rộng, tính an toàn và trải nghiệm người dùng. 
- **Containerization** là một **quy trình triển khai phần mềm** với khả năng đóng gói mã ứng dụng cùng với các thư viện, tệp cấu hình và các phụ thuộc cần thiết để ứng dụng chạy đa nền tảng. Với cách tiếp cận đóng gói mã ứng dụng, mã được viết một lần và có khả năng thực thi ở bất cứ đâu, làm cho ứng dụng có tính di động cao. **Docker** là ví dụ về một nền tảng **Containerization**.
### 1.2. Containerization vs. Virtualization
**Sự khác nhau giữa Containerization và Virtualization**

|      Property       | Virtualization |          Containerization          |
|:-------------------:|:--------------:|:----------------------------------:|
|        Size         |  Heavyweight   |            Lightweight             |
|     Performance     |    Limited performance            |         Native performance         |
|  Operating System   |      Each VM runs in its own OS          |   All containers share the host OS                                 |
| Guest Compatibility |           Hardware-level virtualization                               |           OS virtualization                                                         |
|    Startup time     |         Startup time in minutes                                 |                             Startup time in milliseconds                                       |
|    Memory space     |                                 Allocates required memory                                |                             Requires less memory space                                                                   |
|      Isolation      |         Fully isolated and hence more secure                                                                                 |               Process-level isolation, possibly less secure                                                                                                           |


<div align="center">
       <img src="./images/Containerization vs. Virtualization.png">
       <br/>
       <i>Sự khác nhau giữa Containerization và Virtualization.</i>
</div>

Xem thêm chi tiết [tại đây](https://www.backblaze.com/blog/vm-vs-containers/).
## 2. Docker
### 2.1. Tổng quan
- **Docker** là một nền tảng mã nguồn mở cung cấp cho người sử dụng những công cụ để có thể đóng gói, vận chuyển và chạy container một cách đơn giản và dễ dàng trên các nền tảng khác nhau với tiêu chí “Build once, run anywhere”.
- **Docker** thực hiện ảo hóa ở mức hệ điều hành. Mỗi container là cô lập với nhau nhưng đều dùng chung một số bin/lib và kernel của Host OS.
### 2.2. Một số thuật ngữ
#### Docker Image
**Image** là một trong những đơn vị cơ bản nhất trong Docker. 1 image sẽ định nghĩa cho 1 môi trường và những thứ có trong môi trường đó. Ứng dụng muốn chạy được thì cần phải có **Image**.
#### Docker Container
**Container** được tạo ra từ **Image**, là nơi chứa mọi thứ cần thiết để có thể chạy ứng dụng. Từ 1 image chúng ta có thể tạo ra nhiều containers với môi trường bên trong giống hệt nhau.
<div align="center">
       <img src="./images/docker-container.png" width="500"/>
       <br/>
       <i>Docker Container Lifecycle Management.</i>
</div>

#### Dockerfile
**Dockerfile** là một file dạng text không có phần đuôi mở rộng, chứa các đặc tả về một trường thực thi phần mềm, cấu trúc cho **Docker image**. Từ những câu lệnh đó, Docker sẽ build ra Docker image (thường có dung lượng nhỏ từ vài MB đến lớn vài GB).
#### Docker Network
**Docker Network** có nhiệm vụ cung cấp kết nối để các container trên một hoặc nhiều host có thể liên lạc được với nhau.
Với container và service của Docker, chúng ta có thể kết nối chúng lại với nhau hoặc kết nối chúng với các mạng khác nằm ngoài Docker.
##### Docker Volume
**Volume** là cơ chế tạo và sử dụng dữ liệu của docker, có nhiệm vụ lưu trữ dữ liệu độc lập với vòng đời của container.
Chúng ta dùng **Volume** để giữ lại giữ liệu khi một container bị xóa; chia sẻ dữ liệu giữa máy chủ vật lý và docker container hoặc chia sẻ dữ liệu giữa các container.
#### Docker Compose
**Docker Compose** là công cụ dùng để định nghĩa và run multi-container cho Docker application. Với Docker compose chúng ta sử dụng file YAML để config các services cho application. Sau đó dùng command để create và run từ những config đó.
### 2.3. Docker Engine
#### Docker Engine
**Docker Engine** là thành phần cực kỳ quan trọng và không thể thiếu của Docker có nhiệm vụ như một công cụ có khả năng đóng gói các ứng dụng. Công dụng chính của Docker Engine là chạy container, quản lý việc tạo image, kết nối vào container, tải image về hoặc sử dụng những image có sẵn,…
<div align="center">
       <img src="./images/docker-engine.png" width="500"/>
       <br/>
       <i>Các thành phần chính của Docker Engine.</i>
</div>

#### Server
**Server** hay còn được gọi là docker daemon (dockerd): chịu trách nhiệm tạo, quản lý các Docker objects như images, containers, networks, volume.
#### REST API
Docker daemon cung cấp các API cho Client sử dụng để thao tác với Docker.
#### Client
**Client** là thành phần đầu cuối và cung cấp một tập hợp các câu lệnh sử dụng api để người dùng thao tác với Docker. Ví dụ: docker images, docker ps, ...
### 2.4. Docker Architecture
**Docker** sử dụng kiến trúc **client-server**.

<div align="center">
       <img src="./images/docker-architecture.png"/>
       <br/>
       <i>Kiến trúc của Docker.</i>
</div>

#### Docker Daemon
**Docker daemon** chạy trên host, đóng vai trò là **server**, nhận các RESTful request từ Docker Client và thực thi nó. Là một lightweight runtime giúp build, run và quản lý các containers và các thành phần liên quan khác. Docker Daemon quản lý các **Docker objects** (images, containers, network và volume).
#### Docker Client
**Docker client** là phương thức chính để người dùng thao tác với Docker. Docker client có thể giao tiếp và gửi request đến nhiều Docker daemon.
#### Docker Registry
**Docker Registry** là nơi lưu trữ riêng của Docker Images. Images được push vào Registry và client sẽ pull images từ Registry. Nổi tiếng nhất chính là **Docker Hub**, ngoài ra người dùng có thể tự xây dựng một Docker registry cho riêng mình.
## 3. Dockerfile
**Dockerfile** là một file dạng text không có phần đuôi mở rộng, chứa các đặc tả về một trường thực thi phần mềm, cấu trúc cho Docker Image. Từ những câu lệnh đó, Docker sẽ build ra Docker image (thường có dung lượng nhỏ từ vài MB đến lớn vài GB).

Cú pháp chung của một Dockerfile có dạng:
`INSTRUCTION arguments
`
- INSTRUCTION là tên các chỉ thị có trong Dockerfile, mỗi chỉ thị thực hiện một nhiệm vụ nhất định, được Docker quy định. Khi khai báo các chỉ thị này phải được viết bằng chữ IN HOA.
- aguments là phần nội dung của các chỉ thị, quyết định chỉ thị sẽ làm gì.
### 3.1. Dockerfile instructions
- **FROM**: Một Dockerfile bắt buộc phải bắt đầu bằng chỉ thị `FROM`. Chỉ thị `FROM` là base image để chúng ta tiến hành build một image mới. Các image base này sẽ được tải về từ Public Repository hoặc Private Repository riêng của mỗi người tùy theo setup.
- **ARG**: Dùng để định nghĩa các giá trị của biến được dùng trong quá trình **build image**. Biến `ARG` sẽ không bền vững như khi sử dụng `ENV`.
- **ENV**: Chỉ thị `ENV` dùng để khai báo các biến môi trường. Các biến này được khai báo dưới dạng key - value bằng các chuỗi. Khi run container từ image, các biến môi trường này vẫn có hiệu lực.
- **WORKDIR**: Dùng để đặt thư mục đang làm việc cho các chỉ thị khác như: RUN, CMD, ENTRYPOINT, COPY, ADD,...
- **USER**: Có tác dụng set `username` hoặc `UID` để sử dụng khi chạy image và khi chạy các lệnh có trong `RUN`, `CMD`, `ENTRYPOINT` sau nó.
- **EXPOSE**: Chỉ thị `EXPOSE` thông báo cho Docker rằng image sẽ lắng nghe trên các cổng được chỉ định khi chạy. Lưu ý là cái này chỉ để khai báo, chứ ko có chức năng *nat port* từ máy host vào container. 
- **RUN**: Chỉ thị `RUN` dùng để chạy một lệnh nào đó trong quá trình build image và thường là các câu lệnh Linux. Tùy vào image gốc được khai báo trong phần `FROM` thì sẽ có các câu lệnh tương ứng. 
- **ENTRYPOINT**: Chỉ thị `ENTRYPOINT` cho phép cấu hình một container mà chạy như một lệnh thực thi.
- **VOLUME**: Dùng để mount file/directories giữa host và container. Mục đích của `VOLUME` là: giữ được dữ liệu khi container bị remove, chia sẻ dữ liệu giữa host và container, chia sẻ dữ liệu giữa các container với nhau.
- **CMD**: Dùng để truyền một lệnh của Linux mỗi khi thực hiện khởi tạo một container từ image (image này được build từ *Dockerfile*).
- **ADD**: Chỉ thị `ADD` thực hiện sao chép các tập, thư mục từ máy đang build hoặc remote file URLs từ `<src>` và thêm chúng vào filesystem của image `<dest>`. Trong đó `src` có thể khai báo nhiều file, thư mục, ... còn `dest` phải là đường dẫn tuyệt đối hoặc có quan hệ chỉ thị đối với `WORKDIR`.
- **COPY**: Chỉ thị `COPY` cũng giống với `ADD` là copy file, thư mục từ `<src>` và thêm chúng vào `<dest>` của container. Khác với ADD, nó không hỗ trợ thêm các file remote file URLs từ các nguồn trên mạng.

Xem thêm chi tiết [tại đây](https://viblo.asia/p/tim-hieu-ve-dockerfile-va-tao-docker-image-V3m5WWag5O7).
### 3.2. Homework
#### Phân biệt ARG và ENV:
- `ARG` còn được gọi là biến build-time (chỉ hoạt động trong quá trình build images). Biến `ARG` sẽ không bền vững như khi sử dụng `ENV`, chúng chỉ khả dụng cho đến khi image được tạo. Khi chạy container, chúng ta không thể truy cập giá trị của các biến `ARG`. Các giá trị `ARG` có thể được kiểm tra dễ dàng bằng cách chạy `docker history` của image sau khi được tạo ra. Vì vậy, `ARG` không được lựa chọn sử dụng cho các dữ liệu nhạy cảm, mang tính bảo mật cao.
- Các biến `ENV` cũng có sẵn trong quá trình build, ngay khi khai báo chúng với một command của `ENV`. Tuy nhiên, không giống như `ARG`, khi build xong image, các container chạy image có thể truy cập giá trị `ENV` này. Các container chạy từ image có thể ghi đè giá trị của `ENV`.

<div align="center">
       <img src="./images/arg_env.png" width="500"/>
       <br/>
       <i>So sánh <strong> ARG </strong> và <strong> ENV</strong>.</i>
</div>

#### Phân biệt COPY và ADD:
- `COPY` và `ADD` trong Docker phục vụ chung một mục đích đó là copy file từ một nơi nào đó vào trong Image.
- `COPY` nhận vào đối tượng cần copy và đích cần copy tới trong image. Và `COPY` **chỉ cho phép** copy file từ local, từ máy gốc của chúng ta vào trong Image.
- `ADD` cũng làm được điều tương tự nhưng `ADD` có thêm 2 chức năng đó là:
   - có thể copy từ một địa chỉ URL vào trong Image;
   - có thể giải nén một file và copy vào trong Image.
- **Khi nào nên dùng `COPY` hoặc `ADD`:**
  - Trường hợp sử dụng hợp lệ của `ADD` là khi thực hiện giải nén một local tar file tới một đường dẫn khai báo trong Docker Image. Nhưng trong hầu hết trường hợp khi dùng đến URL để download file thì sẽ dùng câu lệnh **`RUN curl/wget`** hoặc muốn giải nén file thì cũng sẽ dùng **`RUN tar -xvzf`**.
  - Nếu thực hiện copy local files tới Docker image thì hãy sử dụng `COPY` bởi vì nó tường minh hơn so với `ADD` (làm rõ việc chúng ta đang muốn thực hiện hành động nào).
#### Phân biệt CMD và ENTRYPOINT:
- Hiện tại Docker chỉ cho phép chạy một `CMD` khi khởi động container, nhưng nếu `CMD` của các chúng ta phức tạp thì có thể dùng tới `ENTRYPOINT`.
- `CMD` và `ENTRYPOINT` có tác dụng tương tự nhau. Nếu một Dockerfile có cả `CMD` và `ENTRYPOINT` thì `ENTRYPOINT` được dùng để làm đối số mặc định cho `CMD`. 
- Lý do dùng `ENTRYPOINT` là để chuẩn bị các điều kiện setup như tạo user, mkdir, change owner... cần thiết để chạy service trong container.
>Trong Dockerfile có thể vừa có ENTRYPOINT vừa có CMD.
#### Phân biệt CMD và RUN: 
- `RUN` được thực thi trong quá trình build. Khi chúng ta build một Docker image, Docker sẽ đọc các câu lệnh trong chỉ dẫn `RUN` và build tới một layer mới trong image sử dụng.
- `CMD` được thực thi trong quá trình run. Điều này cho phép gọi tới một vài quá trình như bash, nginx hay bất cứ quá trình nào mà Docker image runs. Việc thực thi chỉ thị nằm ngay trong layer hiện tại của images.
- Trong Dockerfile có thể có nhiều chỉ thị `RUN` được thực thi nhưng chỉ có duy nhất một chỉ thị `CMD` được thi.
# II. Web Application


    