## Bài tập ansible

*Người thực hiện: Trần Mạnh Dũng*

#### 1. Các thành phần trong project
- **Web frontend:**
  - Ngôn ngữ sử dụng: HTML, CSS, JS
  - Hiển thị các thông tin học viên kèm theo các chức năng cơ bản như: thêm, sửa, xóa học viên.
  - Xây dựng Dockerfile chạy base image nginx làm webserver 
  - Một số hình ảnh demo
  
![alt](images/1-1-web-frontend.jpg)

![alt](images/1-2-web-frontend.jpg)

![alt](images/1-3-web-frontend.png)
- **API backend:**
  - Ngôn ngữ sử dụng: Django(python)
  - Xây dựng các API: GET, LIST, PUT, PATCH, DELETE
  
![alt](images/1-4-api.png)
- **Database:**
  - Hệ quản trị cơ sở dữ liệu: PostgreSQL
#### 2. Ansible
- Thực hiển triển khai 3 dịch vụ đã trình bày tại mục 1 sử dụng công cụ ansible
- Số lượng managed node là 2 trong đó có 1 node vừa làm control node vừa là managed node (đặt là *MN1*) và 1 node có địa chỉ ip là 192.168.238.132 (đặt là *MN2*).
- **Thực hiện xây dựng role common**
  - Nhiệm vụ: Cài đặt và setup docker cho các managed node. Trong bài này em chỉ thực hiện cài đặt trên MN2 do MN1 là control node đã có sẵn môi trường docker.
  - Xây dựng file inventory:
    - Khai báo 2 host đó là localhost và 192.168.238.132, user sử dụng trong quá trình thao tác với các host.
    - NOTE: Mật khẩu để kết nối tới các host ở đây đã được mã hóa nhằm mục đích bảo mật an toàn thông tin sử dụng ansible-vault. Dùng câu lệnh `ansible-vault create <file_name>` để tạo file chứa mật khẩu của host sau đó ansible sẽ yêu cầu tạo mật khẩu để có thể truy cập vào được file đó vào những lần sau hoặc chạy ansible-playbook. Sau khi ghi mật khẩu vào file ta lưu lại file thì trong file lúc này mở ra sẽ được mã hash kiểu AES256 và ta paste mã hash đó vào mục `ansible_password`. Mỗi lần chạy câu lệnh ansible-playbook thì ta phải thêm chỉ thị `--ask-vault-pass` rồi nhập mật khẩu để truy cập vào file ta đã tạo ở trên để chạy thành công.

    ![alt](images/2-1-ansible-.png)

  - Xây dựng playbook:
    - Cài đặt docker thì em để `become: true` tức là sẽ cài đặt với quyền là root user. Nhưng ở task cuối của play này thì em thêm user khác không phải root vào group docker và sử dụng user này để thực thi docker xuyên suốt project.

    ![alt](images/2-2-ansibleplaybook-common.png)
  - Xây dựng role:
    - Tasks:
      - Chạy lần lượt các task từ trên xuống dưới để cài đặt thành công docker.
      - Task cuối như đã trình bày ở trên thì sẽ add user `manhdung5801` vào group docker và thực thi các lệnh của docker từ user `manhdung5801` này.

    ![alt](images/2-3-ansibleplaybook-common.png)

- **Thực hiện xây dựng role db**
  - Nhiệm vụ: Trỏ tới nơi chứa file docker-compose.yml config service postgreSQL và bật service lên.
  - Deploy: trên MN1
  - Xây dựng playbook:
  
    ![alt](images/2-4-ansibleplaybook-db.png)
  - Xây dựng role:
    - Các task liên quan tới docker, khi sử dụng module docker hay docker-compose đề gặp lỗi. Em đã cố gắng search fix bug, cài các library theo version thỏa mãn requirements nhưng vẫn không hết lỗi :

    ![alt](images/db_bug.jpeg)

    ![alt](images/2-6-ansibleplaybook-db.png)
    - Vì vậy, em sử dụng module shell. Đầu tiên là stop và kill docker container db đang chạy, sau đó là chạy lại service bằng câu lệnh `docker-compose up -d`

    ![alt](images/2-5-ansibleplaybook-db.png)
  - Xây dựng var:
    
    ![alt](images/2-7-ansibleplaybook-db.png)
- **Thực hiện xây dựng role api**
  - Nhiệm vụ: Kiểm tra sự tồn tại của container và image version cũ sau đó sẽ xóa đi nếu tồn tại. Tiếp theo pull image từ repo trên docker hub với tag image latest (mới nhất). Cuối cùng là chạy container với image vừa pull về.
  - Deploy: trên MN2
  - Xây dựng playbook:
    - Thực thi với user `manhdung5801` đã thêm vào group docker ở bước trước chứ không thực thi với quyền root.
  
    ![alt](images/2-8-ansibleplaybook-api.png)
  - Xây dựng role:
    - Task 1: Dừng và xóa bỏ container đang chạy version cũ. Trong trường hợp tồn tại container có tên cố định sẵn đang chạy thì sẽ thực thi còn nếu không tồn tại thì sẽ bỏ qua task này.
    - Task 2: Xóa image version cũ nhằm mục đích cải thiện dung lượng lưu trữ của server.
    - Task 3: Pull image version mới nhất từ repo về.
    
    ![alt](images/2-9-ansibleplaybook-api.png)

    ![alt](images/2-11-ansibleplaybook-apidockerhub.jpg)
  - Xây dựng var:

    ![alt](images/2-10-ansibleplaybook-api.png)
- **Thực hiện xây dựng role web-frontend**
  - Xây dựng tương tự như role api.
  - Xây dựng playbook:
  
    ![alt](images/2-12-ansibleplaybook-web.png)
  - Xây dựng role web:

    ![alt](images/2-13-ansibleplaybook-web.png)

    ![alt](images/2-15-ansibleplaybook-webdockerhub.png)
  - Xây dựng var:

    ![alt](images/2-14-ansibleplaybook-web.png)
> *NOTE*: Xây dựng file ansible-playbook.yml sắp xếp các play sao cho thỏa mãn điều kiện của từng dịch vụ do ansible sẽ thực thi tuần tự từng play, từng task từ trên xuống dưới. Đầu tiên sẽ là cài đặt và setup môi trường cho các managed node. Sau đó, database sẽ phải là dịch vụ được deploy đầu tiên, sau đó là tới deploy server api backend và cuối cùng là frontend. Bởi vì server backend sẽ thực hiện query vào database nên database sẽ phải sẵn sàng để server backend kết nối tới, nếu không sẽ gặp lỗi ngay lập tức. Còn phía client frontend sẽ gửi request tới backend nên nó sẽ được sinh ra sau backend.

#### 3. Kết quả
- Chạy các plays và tasks qua lệnh ansible-playbook

  ![alt](images/3-1-result.png)

  ![alt](images/3-2-result.png)

  ![alt](images/3-3-result.png)

- Sau khi chạy, ta thu được kết quả sau

  ![alt](images/3-4-result.png)

  ![alt](images/3-7-result.png)

  ![alt](images/3-5-result.png)

  ![alt](images/3-6-result.png)
