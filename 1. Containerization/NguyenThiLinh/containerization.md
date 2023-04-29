# Containerization - Nguyen Thi Linh

- [TABLE OF CONTENT](#table-of-content)
- [1. PHÂN BIỆT CÁC INSTRUCTION](#1-phân-biệt-các-instruction)
  - [1.1. ARG vs ENV](#11-arg-vs-env)
  - [1.2. COPY vs ADD](#12-copy-vs-add)
  - [1.3. CMD vs ENTRYPOINT](#13-cmd-vs-entrypoint)
- [2. THREE-TIER WEB APPLICATION WITH DOCKER](#2-three-tier-web-application-with-docker)

# 1. PHÂN BIỆT CÁC INSTRUCTION

## 1.1. ARG vs ENV

**Giống nhau**: ARG và ENV đều là các instruction dùng để định nghĩa các biến trong Docker nhưng phạm vi các biến khai bảo bởi 2 instruction này là khác nhau.

**Khác nhau**:

- ***ARG*** còn được gọi là biến build-time(chỉ hoạt động trong quá trình build images). Chúng chỉ khả dụng kể từ thời điểm chúng được 'công bố' trong Dockerfile trong câu lệnh ARG cho đến khi image được tạo. Khi chạy container, chúng ta không thể truy cập giá trị của các biến ARG. 

  + Nếu không cung cấp giá trị cho các biến ARG không có giá trị mặc định, chúng ta sẽ nhận được thông báo lỗi.

  + Các giá trị ARG có thể được kiểm tra dễ dàng bằng cách chạy docker history của image sau khi được tạo ra. Vì vậy, ARG không được lựa chọn sử dụng cho các dữ liệu nhạy cảm, mang tính bảo mật cao

- ***ENV*** : không giống như ARG, khi build xong image, các container chạy image có thể truy cập giá trị ENV này. Các container chạy từ image có thể ghi đè giá trị của ENV.

**Cú pháp**:

        ENV variable_name=value
        ARG variable_name=value

Để sử dụng một biến ENV hoặc ARG ta sử dụng:

        $variable_name

Khi build Docker image, có thể đặt các giá trị ARG (thay vì giá trị khai báo trong Dockerfile) bằng cách sử dụng *--build-arg*:

	docker build --build-arg some_variable_name=a_value
        
Nhưng không thể làm như vậy với biến ENV, nhưng ta có thể thay đổi bằng cách set biến ENV bằng 1 biến ARG như sau:

        ARG arg_var = value
        ENV env_var = $arg_var



## 1.2. COPY vs ADD

**Giống nhau**: Đều có tính năng sao chép tập tin/thư mục từ máy local và thêm chúng vào filesystem của image

**Cú pháp**:

	 COPY <src> <dest>
	 ADD <src> <dest>

**Khác nhau**:

- ***ADD*** có thể sao chép file từ remote file URLs vào file system của image
 
  + Nếu tham số *src* của ADD là một kho lưu trữ ở định dạng nén được công nhận, nó sẽ được giải nén
  
  + Trường hợp sử dụng hợp lệ của ADD là khi bạn muốn thực hiện giải nén một local tar file tới một đường dẫn khai báo trong Docker Image.
  
  + Trong hầu hết các trường hợp, nếu bạn sử dụng một URL, ta sẽ download một file zip và thực hiện sử dụng chỉ dẫn lệnh RUN để xử lý nó. Tuy nhiên, ta cũng có thể sử dụng chỉ dẫn RUN với curl để thay thế cho chỉ dẫn ADD. Tuy nhiên, nên gộp các chỉ dẫn lệnh RUN xử lý một mục đích lại để giảm kích thước của Docker Image.
  
- Nếu chỉ thực hiện copy local files tới Docker image thì **nên sử dụng COPY** bởi vì nó **tường minh** hơn so với ADD

Ví dụ, thay vì sử dụng:

	    ADD https://example.com/big.tar.xz /usr/src/things/
	    RUN tar -xJf /usr/src/things/big.tar.xz -C /usr/src/things
	    RUN make -C /usr/src/things all

Ta có thể dùng curl:

	    RUN mkdir -p /usr/src/things \
		&& curl -SL https://example.com/big.tar.xz \
		| tar -xJC /usr/src/things \
		&& make -C /usr/src/things all

## 1.3. CMD vs ENTRYPOINT

**Giống nhau**: CMD và ENTRYPOINT đều dùng để định ra program mà ta muốn thực thi khi mà ta chạy docker run.

**Khác nhau**: 

- ***CMD*** thì khi ta thêm vào đằng sau tên image của lệnh docker run image thì nó sẽ override lệnh CMD này (có thể khai báo nhiều nhưng **chỉ có lệnh CMD cuối cùng được chạy**), ví dụ ta có Dockerfile như sau:

        FROM ubuntu
        CMD  ["echo", "Hello World"]

  + Output sẽ là "Hello World!". Nhưng nếu ta chạy với lệnh 

        docker run getting-started echo "Hello from NTLiinhh" 
        
  + Output sẽ là "Hello from NTLiinhh" thay vì "Hello World" (do lệnh CMD bị ghi đè)


- ***ENTRYPOINT*** sẽ configure khi run container như một lệnh (executable), nói cách khác mọi biến được define sau tên của image sẽ được **append** vào lệnh trong ENTRYPOINT **như một biến**. Ví dụ, khi ta có file Dockerfile:

        FROM ubuntu
        ENTRYPOINT ["echo", "Hello World"]

    + Nếu ta thêm echo "Hello from NTLiinhh" vào thì lệnh này sẽ trả về output Hello World! echo Hello from NTLiinhh do khi append thì nó sẽ thành ["Hello World!", "echo", "Hello from NTLiinhh"] sẽ là argument của lệnh echo:



