I. Docker container

Docker container là một đơn vị phần mềm đóng gói có thể chạy độc lập trên hệ điều hành mà không cần cài đặt hoặc cấu hình thêm bất kỳ phần mềm hoặc thư viện nào khác. Mỗi container chứa một ứng dụng và tất cả các thư viện hoặc phụ thuộc cần thiết để chạy ứng dụng đó. Các container được đóng gói bằng cách sử dụng Dockerfile và Docker engine để tạo ra một ảnh Docker, một hình ảnh tĩnh của container.

Một container có thể chạy trên bất kỳ máy tính nào có Docker engine được cài đặt và được cấu hình để chạy container. Các container có thể được triển khai trên các môi trường máy tính khác nhau, bao gồm các máy chủ đám mây và máy tính cá nhân, giúp cho việc triển khai ứng dụng dễ dàng hơn và đảm bảo tính đồng nhất giữa các môi trường khác nhau.

Một container cũng có thể được liên kết với các container khác để tạo thành một ứng dụng phức tạp hơn, hoặc được giới hạn về tài nguyên để đảm bảo tính ổn định của hệ thống. Container cũng có thể được quản lý, theo dõi và cập nhật trên toàn bộ chu trình phát triển và triển khai của ứng dụng.


II. Dockerfile

Dockerfile là một file dạng text không có phần đuôi mở rộng, chứa các đặc tả về một trường thực thi phần mềm, cấu trúc cho Docker Image. Từ những câu lệnh đó, Docker sẽ build ra Docker image (thường có dung lượng nhỏ từ vài MB đến lớn vài GB).

Cú pháp chung của một Dockerfile có dạng:

   INSTRUCTION arguments

INSTRUCTION là tên các chỉ thị có trong Dockerfile, mỗi chỉ thị thực hiện một nhiệm vụ nhất định, được Docker quy định. Khi khai báo các chỉ thị này phải được viết bằng chữ IN HOA. Một Dockerfile bắt buộc phải bắt đầu bằng chỉ thị FROM để khai báo đâu là image sẽ được sử dụng làm nền để xây dựng nên image của bạn. aguments là phần nội dung của các chỉ thị, quyết định chỉ thị sẽ làm gì.

Docker image

Docker image là một file bất biến - không thay đổi, chứa các source code, libraries, dependencies, tools và các files khác cần thiết, và được cấu tạo thành các layer cho một ứng dụng để chạy.

Docker container

Docker container là một run-time environment mà ở đó người dùng có thể chạy một ứng dụng độc lập. Những container này rất gọn nhẹ và cho phép bạn chạy ứng dụng trong đó rất nhanh chóng và dễ dàng.

FROM

Chỉ thị FROM là bắt buộc và phải được để lên phía trên cùng của Dockerfile.

Cú pháp: FROM <image> [AS <name>] FROM <image>[:<tag>] [AS <name>] FROM <image>[@<digest>] [AS <name>]

EXPOSE

Thiết lập cổng mà container lắng nghe, cho phép các container khác trên cùng mạng liên lạc qua cổng này hoặc ánh xạ cổng host vào cổng này.

WORKDIR

Thiết lập thư mục làm việc trong container cho các lệnh COPY, ADD, RUN, CMD, và ENTRYPOINT


4. ARV and ENV

ARG còn được gọi là biến build-time(chỉ hoạt động trong quá trình build images). Chúng chỉ khả dụng kể từ thời điểm chúng được 'công bố' trong Dockerfile trong câu lệnh ARG cho đến khi image được tạo.

Các biến ENV cũng có sẵn trong quá trình xây dựng, ngay khi bạn khai báo chúng với một command của ENV. Tuy nhiên, không giống như ARG, khi build xong image, các container chạy image có thể truy cập giá trị ENV này. Các container chạy từ image có thể ghi đè giá trị của ENV.

Cú pháp:

			ENV <key>=<value> 

5. COPY and ADD

Chỉ thị ADD sẽ thực hiện sao chép các tập, thư mục từ máy đang build hoặc remote file URLs từ src và thêm chúng vào filesystem của image dest.
Cú pháp:

ADD [--chown=<user>:<group>] <src>... <dest>
ADD [--chown=<user>:<group>] ["<src>",... "<dest>"]
Trong đó:

src có thể khai báo nhiều file, thư mục, ...
dest phải là đường dẫn tuyệt đối hoặc có quan hệ chỉ thị đối với WORKDIR.
Chỉ thị COPY cũng giống với ADD là copy file, thư mục từ src và thêm chúng vào dest của container. Khác với ADD, nó không hỗ trợ thêm các file remote file URLs từ các nguồn trên mạng.
Cú pháp:

COPY [--chown=<user>:<group>] <src>... <dest>	       
COPY [--chown=<user>:<group>] ["<src>",... "<dest>"]

6. CMD and ENTRYPOINT

CMD thực hiện lệnh mặc định khi chúng ta khởi tạo container từ image, lệnh mặc định này có thể được ghi đè từ dòng lệnh khi khởi tại container.
CMD cho phép ta set default command, có nghĩa là command này sẽ chỉ được chạy khi run container mà không chỉ định một command.
Nếu docker run với một command thì default command sẽ được ignore. Nếu dockerfile có nhiều hơn một lệnh CMD thì tất cả sẽ bị ignore ngoại trừ lệnh CMD cuối cùng.
Cú pháp:

		 CMD ["executable", "param1", "param2"]   (exec form)
		 CMD ["param1", "param2"]  (đặt các tham số mặc định cho ENTRYPOINT ở dạng exec form)
		 CMD command param1 param2   (shell form)
ENTRYPOINT khá giống CMD đều dùng để chạy khi khởi tạo container, nhưng ENTRYPOINT không thể ghi đè từ dòng lệnh khi khi khởi tại container.
Lệnh ENTRYPOINT cho phép ta cấu hình container sẽ chạy dưới dạng thực thi. Nó tương tự như CMD, vì nó cũng cho phép ta chỉ định một lệnh với các tham số. Sự khác biệt là lệnh ENTRYPOINT và các tham số không bị ignore khi Docker container chạy.
Cú pháp:

		- ENTRYPOINT ["executable", "param1", "param2"] (exec form)
		- ENTRYPOINT command param1 param2 (shell form)

III. Docker-compose

- Docker Compose là một công cụ dùng để định nghĩa và chạy các chương trình Docker sử dụng nhiều container (multi-container). - - Những lợi ích khi sử dụng Compose:
Tạo ra nhiều môi trường độc lập (isolated environments) trong một host: Compose cô lập môi trường của các project để đảm bảo chúng không bị xung đột lẫn nhau, cũng như dễ dàng tạo những bản sao của một môi trường nào đó.

Chỉ tạo lại các container đã thay đổi: Compose sẽ nhận biết được các service chưa thay đổi và sử dụng lại các container tương ứng với service đó.

Điều chỉnh các biến sử dụng cho các môi trường: Compose sử dụng các biến trong Compose file cho các môi trường. Vì vậy với môi trường hay người dùng khác nhau, có thể điều chỉnh các biến khi sử dụng Compose để thiết lập các service.

IV. Docker network

Trong Docker, có bốn loại network mặc định để kết nối các container với nhau và với mạng bên ngoài. Các loại network này bao gồm:

- Bridge network: Đây là network mặc định được tạo ra khi cài đặt Docker. Nó cho phép các container trong cùng một bridge network kết nối với nhau và với máy host. Bridge network cũng có thể được liên kết với các mạng khác để các container có thể kết nối với nhau trên các mạng khác nhau.

- Host network: Khi sử dụng host network, các container sẽ chia sẻ cùng một địa chỉ IP với máy host và sử dụng các port mở trên máy host để kết nối với mạng bên ngoài. Các container có thể truy cập vào tất cả các dịch vụ được cung cấp trên máy host, nhưng không thể chạy trên các port giống nhau.

- Overlay network: Overlay network cho phép các container trên các host khác nhau kết nối với nhau và tạo thành một mạng lớn. Overlay network sử dụng giao thức VXLAN để mã hóa dữ liệu và đảm bảo tính riêng tư và an toàn của mạng.

- Macvlan network: Macvlan network cho phép các container có địa chỉ MAC và IP riêng biệt, giúp các container trông giống như các máy tính vật lý trên cùng một mạng.

Ngoài ra còn có :

- None network: Loại network này không có bất kỳ liên kết nào đến các mạng bên ngoài và không thể truy cập vào Internet. Nó được sử dụng khi bạn muốn chạy container độc lập và không yêu cầu kết nối mạng.

- Network namespace sharing: Network namespace sharing cho phép các container chia sẻ cùng một namespace mạng để chia sẻ các kết nối mạng và tài nguyên. Điều này cho phép các container hoạt động như một ứng dụng duy nhất trên mạng.