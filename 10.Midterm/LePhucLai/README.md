# BÀI TẬP LỚN GIỮA KỲ

# 1. Phát triển một 3-tier web application đơn giản
Mã nguồn:
* [web](Docker/nginx/conf.d/app.conf)
* [api](Docker/app/app.py)
* [unitest](Docker/app/test.py)

![ảnh web](img/webapp.gif)

# 2. Containerization
* [File dockercompose](Docker/docker-compose.yml)
* [Dockerfile cua api](Docker/app/Dockerfile)
* [Dockerfile cua web](Docker/nginx/Dockerfile)
* [File log của câu lệnh docker compose build](logs/dockercompose_build_logs.txt)
* [Docker history của python image](logs/history_python.txt)
* [Docker history của nginx image](logs/history_nginx.txt)
* [Docker history của mongo image](logs/history_mongo.txt)

Chạy câu lệnh docker compose up:
![anh ket qua docker compose up](img/dockercompose_up.gif)


# 3. Continuous Integration
* [File setup công cụ CI](../.github/workflows/CI.yaml)
* [Output log của luồng CI](logs/CI.txt)

![ảnh kết quả chạy CI](img/CI_result.png)

# 4. Continuous Delivery
## 4.1 CD
* [File setup công cụ CD](../.github/workflows/CD.yaml)
* [Output log của luồng CD](logs/CD.txt)
![Kết quả của luồng CD](img/CD_result.png)

## 4.2 Cách triển khai load balance:
![loadbalance](img/loadbalance.png)

## 4.3 Ansible
Thư mục Ansible:
```
.
├── inventories
│   └── inventory.yaml
├── roles
│   ├── api
│   │   └── tasks
│   │       └── main.yaml
│   ├── common
│   │   └── tasks
│   │       └── main.yaml
│   ├── db
│   │   ├── files
│   │   │   └── attendees.json
│   │   └── tasks
│   │       └── main.yaml
│   ├── lb
│   │   ├── files
│   │   │   ├── app.conf
│   │   │   └── Dockerfile
│   │   └── tasks
│   │       └── main.yaml
│   ├── logging
│   │   ├── files
│   │   │   ├── docker-compose.yml
│   │   │   └── fluentd
│   │   │       ├── conf
│   │   │       │   └── fluent.conf
│   │   │       └── Dockerfile
│   │   └── tasks
│   │       └── main.yaml
│   ├── monitor
│   │   ├── files
│   │   │   ├── docker-compose.yml
│   │   │   └── prometheus.yml
│   │   └── tasks
│   │       └── main.yaml
│   └── web
│       └── tasks
│           └── main.yaml
└── setup.yaml
```
* Output log triển khai hệ thống:
[Output log triển khai hệ thống] (logs/ansible_log.txt)
![ảnh output log triển khai hệ thống](img/Ansible_output.png)
* Do ở localhost docker đã được cài đặt trước đó bằng gói containerd.io, gói này xung đột với gói containered được thiết lập để cài ở trong playbook. Do đó task này báo lỗi. Ở trên node khác thì việc cài đặt Docker diễn ra bình thường

# 5. Monitoring
[Role monitor chứa playbook và cấu hình giám sát hệ thống](Ansible/roles/monitor)

![ảnh monitoring](img/prometheus.png)

# 6. Logging
[Role logging triển khai các dịch vụ collect log](Ansible/roles/logging)
* Để có thể lấy được log từ các Container, ta sẽ phải thêm `log_driver: fluentd` vào trong các task build container trong ansible playbook

![ảnh log](img/logging.png)