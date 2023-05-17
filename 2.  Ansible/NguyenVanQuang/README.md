# Deploy Webapp using Ansible

---
## Table of contents
[I. Lý thuyết](#intro)
- [1. Ansible](#ansible)
- [2. Ansible Galaxy](#galaxy)

[II. Homework](#requirements)

[III. Deployment](#deployment)
- [1. Setup VM](#vmSetup)
- [2. Ansible role Docker](#common)
- [3. Other roles](#other)
- [4. Deploy Webapp](#deployWeb)


---
## I. Lý thuyết <a name='intro'></a>

### 1. Ansible <a name='ansible'></a>

Việc cài đặt và cấu hình các máy chủ thường được ghi chép lại trong tài liệu dưới dạng các câu lệnh đã chạy, với giải thích kèm theo. Cách thức này gây mệt mỏi cho quản trị viên vì phải làm theo từng bước ở mỗi máy khi thiết lập mới, và có thể dẫn đến sai lầm, thiếu sót.

**Ansible** giúp cấu hình "nhiều" server theo tùy biến rất đa dạng, giảm thiểu thời gian thao tác trên từng server được cài đặt

<div align="center">
  <img width="500" src="/images/ansible.png">
</div>

<div align="center">
  <i>Pic. 1 -Ansible</i>
</div>

```
# Cài đặt trên Ubuntu
apt-add-repository -y ppa:ansible/ansible
apt-get update
apt-get install -y ansible

```
**Một số thuật ngữ cơ bản khi sử dụng Ansible **
**Controller Machine:** Là máy cài Ansible, nó sẽ chịu trách nhiệm quản lý, điều khiển và gửi các task đến những máy con cần quản lý.

**Inventory:** Là file chứa thông tin những server cần quản lý. File này thường nằm tại đường dẫn /etc/ansible/hosts.

**Playbook:** Là file chứa các task được ghi dưới định dạng YAML. Máy controller sẽ đọc các task này trong Playbook sau đó đẩy các lệnh thực thi tương ứng bằng Python xuống các máy con.

**Task:** Một block ghi lại những tác vụ cần thực hiện trong playbook và các thông số liên quan.

**Module:** Trong Ansible có rất nhiều module khác nhau. Ansible hiện có hơn 2000 module để thực hiện các tác vụ khác nhau, bạn cũng có thể tự viết thêm những module của mình khi có nhu cầu. Một số Module thường dùng cho những thao tác đơn giản như: System, Commands, Files, Database, Cloud, Windows,...

**Role: **Là một tập playbook đã được định nghĩa để thực thi 1 tác vụ nhất định. Nếu bạn có nhiều server, mỗi server thực hiện những tasks riêng biệt. Và khi này nếu chúng ta viết tất cả vào cùng một file playbook thì khá là khó để quản lý. Do vậy roles sẽ giúp bạn phân chia khu vực với nhiệm vụ riêng biệt.

**Play:** là quá trình thực thi một playbook.

**Facts:** Thông tin của những máy được Ansible điều khiển, cụ thể sẽ là các thông tin về OS, system, network,…

**Handlers:** Được sử dụng để kích hoạt những thay đổi của dịch vụ như start, stop service.

**Variables:** Được dùng để lưu trữ các giá trị và có thể thay đổi được giá trị đó. Để khai báo biến, người dùng chỉ cần sử dụng thuộc tính vars đã được Ansible cung cấp sẵn.

**Conditions:** Ansible cho phép người dùng điều hướng lệnh chạy hay giới hạn phạm vi để thực hiện câu lệnh nào đó. Hay nói cách khác, khi thỏa mãn điều kiện thì câu lệnh mới được thực thi. 

Ngoài ra, `Ansible` còn cung cấp thuộc tính **Register**, một thuộc tính giúp nhận câu trả lời từ một câu lệnh. Sau đó ta có thể sử dụng chính kết quả đó để chạy những câu lệnh sau.


**Ansible** sử dụng kiến trúc `agentless` không cần đến agent để giao tiếp với các máy khác. Cơ bản nhất là giao tiếp thông qua các giao thức `WinRM` trên Windows, `SSH` trên Linux hoặc giao tiếp qua chính `API` của thiết bị đó cung cấp.



`Playbooks` là file định dạng `YAML` chứa một loạt các mô tả chỉ thị nhằm mục đích tự động hóa chúng trên server từ xa.

```YAML
---
- hosts: centos7
  become: True
  tasks:
  - name: Install httpd
    yum:
      name: httpd
      state: latest
  - name: Start httpd
    service:
      name: httpd
      state: started
      enabled: True
```

Mỗi `playbook` gồm một hoặc nhiều `play`. Như ví dụ về playbook đơn giản bên trên gồm có 1 `play` duy nhất tên là `Play 1`. 

`Playbook` thường chứa các yếu tố như các nhiệm vụ `tasks`, các vai trò `roles`, các biến `variables`, các điều kiện `conditions` và các cấu hình `configurations`. Một playbook có thể được sử dụng để cài đặt phần mềm, cấu hình hệ thống, tạo ra các tài khoản người dùng, và thực hiện nhiều tác vụ khác trong các hệ thống khác nhau. Mỗi Playbook trong Ansible có thể được áp dụng cho một nhóm máy chủ hoặc một máy chủ cụ thể.

Trong playbook, các `tasks` là các hoạt động cụ thể mà Ansible sẽ thực hiện trên các máy chủ đích. Các nhiệm vụ này có thể là các lệnh `shell`, các cài đặt gói phần mềm, cấu hình hệ thống, tạo tệp tin, sao lưu và phục hồi dữ liệu, v.v.

Vai trò `roles` được sử dụng để tổ chức các nhiệm vụ trong playbook thành các phần riêng biệt. Các vai trò cho phép bạn phân chia các nhiệm vụ thành các phần nhỏ hơn và tái sử dụng chúng trong nhiều playbook khác nhau.

Biến `variables` được sử dụng để lưu trữ các giá trị có thể thay đổi trong playbook. Các biến này có thể được sử dụng cho các mục đích như lưu trữ thông tin xác thực, các đường dẫn tệp, tên máy chủ, v.v.

Các điều kiện `conditions` được sử dụng để xác định các điều kiện phải được thỏa mãn trước khi Ansible thực hiện một nhiệm vụ cụ thể. Ví dụ, bạn có thể sử dụng điều kiện để kiểm tra trạng thái của một máy chủ trước khi Ansible tiến hành cài đặt phần mềm mới.

Các cấu hình `configurations` được sử dụng để thiết lập các cấu hình hệ thống cụ thể cho các máy chủ đích trong playbook. Các cấu hình này có thể bao gồm các thiết lập mạng, cấu hình tường lửa, cấu hình bảo mật, v.v.

`Inventory` trong Ansible là một tệp tin hoặc một nhóm tệp tin chứa thông tin về các máy chủ và các nhóm máy chủ mà Ansible sẽ thực hiện các thao tác trên đó. `Inventory` cung cấp cho Ansible thông tin về địa chỉ IP hoặc tên miền của các máy chủ, thông tin xác thực (tên người dùng, mật khẩu, khóa SSH), các nhóm máy chủ và các biến.

```YAML
all:
  hosts:
    webserver:
      ansible_host: 192.168.1.100
      ansible_user: some_user
      ansible_password: some_password
      ansible_ssh_private_key_file: /path/to/private/key
```

Trong `Inventory` có một số nhóm mặc định được định nghĩa sẵn để giúp người dùng quản lý và thực hiện các tác vụ trên các máy chủ. Các nhóm mặc định này bao gồm:

- `all`: Nhóm này chứa tất cả các máy chủ được định nghĩa trong inventory
- `ungrouped`: Nhóm này chứa các máy chủ không thuộc bất kỳ nhóm nào khác trong tệp inventory.
- `localhost`: Nhóm này chứa máy chủ được xác định là máy chủ địa phương (localhost) và đặc biệt không cần liệt kê trong file inventory (implicit defined).
- `ansible`: Nhóm này được sử dụng để định nghĩa các biến số toàn cục cho tất cả các máy chủ được quản lý bằng Ansible.


`Idempotency` là một khái niệm quan trọng trong Ansible, nó đảm bảo rằng các thao tác được thực hiện trên các máy chủ mục tiêu sẽ đem lại kết quả như mong đợi, mà không bị ảnh hưởng bởi trạng thái hiện tại của hệ thống hoặc các lần chạy `playbook` trước đó.

Trong Ansible, `idempotency` được đảm bảo bởi cách kiểm tra trạng thái hiện tại của máy chủ mục tiêu trước khi thực hiện các thao tác mới. Nếu trạng thái của máy chủ đã tương thích với các thao tác cần thực hiện, Ansible sẽ không thực hiện bất kỳ thay đổi nào trên máy chủ đó. Nếu trạng thái của máy chủ không tương thích, Ansible sẽ chỉ thực hiện các thao tác cần thiết để đưa trạng thái của máy chủ về trạng thái mong đợi.

### 2. Ansible Galaxy <a name='galaxy'></a>

`Ansible Galaxy` là một remote repository lưu trữ các vai trò (roles), mô-đun (modules), bản mẫu (playbooks), và các plugin được phát triển bởi cộng đồng Ansible. Nó được tạo ra để giúp người dùng Ansible dễ dàng tìm kiếm, tải về và sử dụng các vai trò, mô-đun và bản mẫu đã được phát triển bởi người khác.

`Ansible Galaxy` cung cấp một kho lưu trữ trực tuyến cho các mô-đun và vai trò được phát triển bởi cộng đồng Ansible. Người dùng có thể tìm kiếm các mô-đun và vai trò trên Ansible Galaxy để thực hiện các tác vụ cụ thể một cách nhanh chóng và hiệu quả.

`community.docker` là module và plugins dành cho việc làm việc với Docker, được phát triển bởi cộng đồng Ansible để cài đặt và quản lý Docker trên các máy chủ đích.

Với `community.docker`, người dùng Ansible có thể dễ dàng cài đặt `Docker` trên các máy chủ đích, tạo ra các `container` Docker,pull images, quản lý các container đã có, và thực hiện các nhiệm vụ khác liên quan đến Docker.

## II. Homework <a name='requirements'></a>

Triển khai một 3-tier web application sử dụng ansible:

- Role `ansible-role-docker` sử dụng để setup docker
- 3 roles `web`, `api`, `db` sử dụng để triển khai web app đến các máy chủ tương ứng. 

## III. Deployment <a name='deployment'></a>
### 1. Setup VM <a name='vmSetup'></a>

Ta tạo 1 máy chứa Ansible để làm Controller và 1 máy chủ tương ứng web server, api, database,chạy hệ điều hành Ubuntu.

Đối với các máy chủ AWS EC2, để thực hiện kết nối SSH, ta cần tải file chưa ssh private key về, tương ứng là itmo.pem.

```INI
[hosts]
localhost ansible_connection=local

[nodes]
ec2-16-16-159-186.eu-north-1.compute.amazonaws.com ansible_ssh_user=ubuntu ansible_ssh_private_key_file=~/Desktop/Cloud/itmo.pem
```

### 2. Ansible role Docker <a name='common'></a>

Nhiệm vụ chính của anible-role-docker roles là cài đặt và khởi tạo môi trường Docker trên các máy chủ.

### 3. Other roles <a name='other'></a>

Ở cả 3 roles này ta đều dùng 1 phương pháp: `pull image` từ `Image Registry` (dockerhub) về máy đích sau đó tiến hành cài đặt, khởi tạo biến môi trường cùng các options khác. Chứ không copy trực tiếp code vào máy đích và build. 

Việc `build image` trước và chỉ tải image về để chạy ở máy đích giúp `giảm thời gian build` xuống mức tối thiểu, ngoài ra còn `hạn chế lỗi`, xung đột xảy ra trong quá trình build ở máy đích. 

<div align="center">
  <img width="500" src="/images/mongo.png">
</div>

<div align="center">
  <i>Pic. 2 -Mongo image</i>
</div>

---

Role `db`

```yaml
---
- name: Create Database network
  community.docker.docker_network:
    name: data

- name: Pull MongoDB image from Docker Hub
  community.docker.docker_image:
    name: mongo:4.4.18
    repository: bititmo16
    source: pull
    state: present
    force_source: true

- name: Run MongoDB container
  community.docker.docker_container:
    name: mongodb
    image: bititmo16/mongo:4.4.18
    restart_policy: unless-stopped
    state: started
    env:
      DB_DATABASE: "vdt2023"
    networks:
      - name: data
```



---
Role `api`

<div align="center">
  <img width="500" src="/images/logic.png">
</div>

<div align="center">
  <i>Pic. 3 -Logicimage</i>
</div>

```yaml
---
- name: Create a network
  community.docker.docker_network:
    name: presentation

- name: Pull api image from Docker Hub
  community.docker.docker_image:
    name: "{{ flask_image }}"
    source: pull
    state: present
    force_source: true

- name: Run api container
  community.docker.docker_container:
    name: "{{ item }}"
    image: "{{ flask_image }}"
    restart_policy: unless-stopped
    state: started
    env:
      MONGO_INITDB_DATABASE: vdt2023
      SERVICE_NAME: mongodb

    networks:
      - name: data
      - name: presentation
  loop:
    - flask_1
    - flask_2
```

Tương tự như role `db` nhưng có 2 env variables là `MONGO_INITDB_DATABASE`, `SERVICE_NAME` chỉ định địa chỉ của máy chủ database và expose ra port 8080:8080. 

Các variables của db được lưu trong file defaults/main.yml
```yml
db_container_name: mongodb
db_database: database
flask_image: "bititmo16/nguyenvanquang-logic_tier_1"
```

Có thể thấy rằng image này không có sẵn mà do tự mình đã build từ source/api và đưa lên docker hub bằng tài khoản bititmo16


Ta để tag lastest để đảm bảo mỗi khi có cập nhật về image ta có thể cài đặt lại mà không cần sửa đổi roles. 

---
Role `web`

<div align="center">
  <img width="500" src="/images/nginx.png">
</div>

<div align="center">
  <i>Pic. 4 -Nginx image</i>
</div>

```yaml
---
# tasks file for web

- name: Pull nginx image from Docker Hub
  community.docker.docker_image:
    name: "{{ nginx_image }}"
    source: pull
    state: present
    force_source: true

- name: Run nginx
  community.docker.docker_container:
    name: nginx
    image: "{{ nginx_image }}"
    recreate: yes
    restart_policy: unless-stopped
    state: started
    ports:
      - "80:80"
    networks:
      - name: presentation
```
Các variables của db được lưu trong file defaults/main.yml
```yml
---
# defaults file for web
nginx_image: "bititmo16/ansible_nginx"
```
Role `web` cũng tương tự như role `api` khi ta phải tự build image từ source/server và tải lên dockerhub trước sau đó chạy role và expose ra port 80:80.

Configuration Nginx file:
```conf
upstream logic_tier {
    server flask_1:5000 weight=7;
    server flask_2:5000 weight=3;
}
server {
    listen 80;
    server_name localhost;

    location / {
        proxy_pass http://logic_tier/;
    }
    location /v1 {
        proxy_pass http://flask_1:5000/;
    }
    location /v2 {
        proxy_pass http://flask_2:5000/;
    }
}
```

<div align="center">
  <img width="500" src="/images/result.png">
</div>

<div align="center">
  <i>Pic. 5 -Result</i>
</div>