# Mục lục
[I. Chuẩn bị](#i-chuẩn-bị)  
[II. Sử dụng Ansible](#ii-sử-dụng-ansible)
# I. Chuẩn bị
# II. Sử dụng Ansible
## 1. Inventory và Site:
[`inventory.yaml`](./inventory.yaml) là file cấu hình gồm các cấu hình về host và user. Ở đây em sử dụng một host duy nhất.  
[`site.yaml`](./site.yaml) là file ghi rõ thứ tự deploy của các role: common -> db -> back end -> front end

## 2. Role:
Trong mỗi role ta sẽ có 2 directory chính.   
- Một là files nơi lưu giữ các các file để build thành docker image cùng với docker-compose.yaml để deploy.   
- Hai là tasks nơi có những instruction của ansible để cài đặt và deploy ứng dụng.
### 2.1 Files:
#### Docker compose: 
- Trong docker compose của mongodb, ta sẽ tạo một external network để các container trong các docker compose project có thể giao tiếp với nhau.  
#### Docker file:
- Để xử lí dữ liệu đầu vào của mongodb, em đã thêm file import-data.sh vào trong /docker-entrypoint-initdb.d/ để import data.
- Các Dockerfile còn lại không thay đổi đáng kể.
### 2.2: Tasks:
Mỗi tasks chỉ chứa một file main.yaml. Cấu trúc của những file này giống nhau và đều gồm các task:  
- Tạo directory của service
- Copy các file cần thiết
- Sử dụng docker compose module của ansible để deploy các service.
```yaml
---
- name: Create Flask directory
  file:
    path: /etc/flask
    state: directory

- name: Copy file to Node
  copy:
    src: "{{ item }}"
    dest: /etc/flask/
  loop:
    - docker-compose.yaml
    - Dockerfile
    - app.py
    - requirements.txt
  
- name: Run docker compose to Deploy
  community.docker.docker_compose:
    project_src: /etc/flask/
```