# Lab 1: Containerization

Editor: **Do Bao Hoang**

---
## Mục lục
[I. Kiến thức chung](#intro)
- [1. Containerization](#containerization)
- [2. Docker](#docker)
- [3. Docker-compose](#compose)
- [4. Câu hỏi bài tập](#questions)

[II. System requirements](#requirements)

[III. Thực hành](#deployment)
- [1. Webserver](#webserver)
- [2. Web application](#webapp)
- [3. Database](#database)
- [4. Run Result](#result)

[IV. Encountered Errors](#errors)

[V. References](#references)

---
## I. Introduction <a name='intro'></a>

### 1. Containerization <a name='containerization'></a>
`Containerization` là một giải pháp ảo hóa với khả năng đóng gói mã của ứng dụng cùng tất cả các tệp và thư viện cần thiết giúp ứng dụng có thể chạy trên bất kỳ cơ sở hạ tầng nào.

Trước khi công nghệ container xuất hiện, máy ảo (`virtualization`) là công nghệ được dùng để tối ưu hoạt động của máy chủ. Máy ảo mô phỏng các thiết bị vật lý. Các ứng dụng chạy trên 2 máy ảo khác nhau sẽ được cô lập ở lớp vật lý. 

<div align="center">
  <img width="1000" src="imgs/virtualize_containerize.png">
</div>

<div align="center">
  <i>Pic. 1 - Quá trình phát triển của công nghệ</i>
</div>

Tuy máy ảo tối ưu hóa tài nguyên của máy chủ khá hiệu quả nhưng song song với đó cũng còn rất nhiều `nhược điểm` cần khắc phục:

- `Tốn thời gian` cài đặt ứng dụng: mỗi khi tạo máy ảo mới phải cài lại từ đầu, mỗi bước cài đặt khác nhau theo từng phiên bản, update, downgrade khó khăn, ...
- `Dễ xảy ra conflict`: các ứng dụng nằm trên cùng 1 máy ảo vẫn sẽ cạnh tranh nhau về mặt tài nguyên (CPU, RAM, bộ nhớ, ...) và có thể xảy ra xung đột giữa các phiên bản khác nhau. Ngoài ra việc sử dụng nhiều máy ảo cũng không hiệu quả vì phải dành ra dung lượng để cài hệ điều hành trên mỗi máy.

Để khắc phục tình trạng trên, công nghệ `Containerization` với ý tưởng về việc cô lập các tiến trình (ứng dụng) trên hệ điều hành được đề xuất. 

- Không phải tốn dung lượng cho hệ điều hành nên ứng dụng dễ dàng được đóng gói, `tự động hóa việc cài đặt ứng dụng`.
- Vì chung 1 hệ điều hành nên có thể tạo ra nhiều instance mà không sợ tốn bộ nhớ. Mỗi ứng dụng được cô lập trong 1 container nên `không sợ xảy ra conflict` nữa.

`Container` hoạt động dựa trên 2 công cụ của Linux là `Namespace` và `Cgroup`.

<div align="center">
  <img width="1000" src="imgs/namespace.png">
</div>

<div align="center">
  <i>Pic. 2 - Namespace in Linux</i>
</div>

`Namespace` xuất hiện lần đầu tiên trong Linux kernel năm 2002. Namespace giới hạn những gì 1 hoặc 1 nhóm tiến trình `có thể nhìn thấy và tương tác`. Cũng giống như trong `ngôn ngữ lập trình C`, 2 biến thuộc cùng 1 namespace nếu đặt tên trùng nhau sẽ bị lỗi nhưng thuộc 2 namespace khác nhau lại hoàn toàn bình thường. 

`Namespace` trong Linux gồm có:

- `users`: user namespace phân tách các user khác nhau sử dụng user IDs và group IDs
- `PID`: process ID gán cho mỗi tiến trình 1 mã PID riêng.
- `net`: mỗi network namespace có 1 network stack riêng (routing table, IP address, socket listing, ...)
- `mount`: mỗi mount namespace có riêng 1 danh sách mount point, có thể mount, unmount mà không ảnh hưởng đến hệ thống bên ngoài.
- `ipc`: interprocess communication namespace - ví dụ điển hình về ipc là POSIX message queues: mỗi ipc có 1 POSIX queue message filesystem riêng. 
- `uts`: UNIX time-sharing namespace cho phép cùng 1 hệ thống có thể có nhiều hosts và domain names khác nhau. 

<div align="center">
  <img width="1000" src="imgs/cgroup.png">
</div>

<div align="center">
  <i>Pic. 3 - Cgroup in Linux</i>
</div>

`Cgroup` giới hạn tài nguyên (CPU, RAM, bộ nhớ, ...) 1 hoặc 1 nhóm tiến trình có thể sử dụng.

`Cgroup` cung cấp 4 tính năng chính:

- Resource limit: giới hạn tài nguyên sử dụng
- Prioritization: quy định mức ưu tiên sử dụng tài nguyên giữa các group
- Acounting: theo dõi và báo cáo những giới hạn tài nguyên 
- Control: tùy ý thay đổi trạng thái của tiến trình bên trong group (frozen, stopped, restarted)

`Namespace` và `Cgroup` là 2 công cụ dành riêng cho Linux nên các nền tảng khác (windows, apple) không thể chạy trực tiếp dẫn đến hiệu suất không bằng Linux thậm chí có thể gặp lỗi. 


### 2. Docker <a name='docker'></a>

<div align="center">
  <img width="1000" src="imgs/docker.png">
</div>

<div align="center">
  <i>Pic. 4 - Docker</i>
</div>

`Docker` được tạo ra năm `2013` bởi công ty cùng tên viết bằng ngôn ngữ Go. Từ đó đến nay Docker vẫn luôn là công cụ tốt nhất để làm việc với container. 

`Docker` là một `PaaS` (dịch vụ nền tảng) sử dụng ảo hóa ở cấp độ hệ điều hành để đóng gói phần mềm vào các package gọi là `container`. 

Ý tưởng chính của Docker là `Build once, run everywhere` giúp cho quá trình vận hành phần mềm đơn giản hơn trước rất nhiều. 

<div align="center">
  <img width="1000" src="imgs/docker_architect.png">
</div>

<div align="center">
  <i>Pic. 5 - Cấu trúc của Docker </i>
</div>

`Cấu trúc của Docker` gồm có 3 thành phần chính:

- `Docker Daemon` (dockerd) 
- `Docker Client`
- `Docker Registry`

### 3. Docker-compose <a name='compose'></a>

### 4. Câu hỏi bài tập <a name='questions'></a>

## II. Yêu cầu đề bài <a name='requirements'></a>

Cài đặt một ứng dụng web 3 lớp để hiển thị thông tin các học viên trên trình duyệt sử dụng docker-compose.

Base images:

- `nginx:1.22.0-alpine`
- `python:3.9`
- `mongo:5.0`


## III. Thực hành <a name='deployment'></a>

<div align="center">
  <img width="1000" src="imgs/3_tier_app.png">
</div>

<div align="center">
  <i>Pic. 5 - Cấu trúc ứng dụng web 3 lớp </i>
</div>

Ứng dụng web 3 lớp gồm có:

- Lớp `Presentation`: hiện thị các thành phần giao diện để tương tác với người dùng. Tương ứng với lớp này trong bài tập ta xây dựng 1 `static webserver` trả về html, css, js file bằng `Nginx`
- Lớp `Businesss Logic`: thực hiện các hành động tính toán, đánh giá, xử lý thông tin. Tương ứng với lớp này trong bài tập ta xây dựng 1 `ứng dụng web` chạy bằng `flask` trả về dữ liệu dạng json.
- Lớp `Data`: lưu trữ và trích xuất dữ liệu từ CSDL. Tương ứng với lớp này trong bài tập ta xây dựng 1 `CSDL MongoDB` cho phép truy xuất qua cổng 27017.

### 1. Webserver <a name='webserver'></a>

### 2. Web application <a name='webapp'></a>

### 3. Database <a name='database'></a>

### 4. Run Result <a name='result'></a>

## IV. Encountered Errors <a name='errors'></a>

## V. References <a name='references'></a>

