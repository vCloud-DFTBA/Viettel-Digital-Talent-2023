# Bài tập Ansible

Đây là cấu trúc file:
```
.
├── inventories
│   └── inventory.yaml
├── roles
│   ├── api
│   │   ├── files
│   │   │   ├── app.py
│   │   │   ├── Dockerfile
│   │   │   ├── requirements.txt
│   │   │   ├── static
│   │   │   ├── templates
│   │   │   │   ├── create.html
│   │   │   │   ├── get.html
│   │   │   │   ├── index.html
│   │   │   │   └── update.html
│   │   │   └── wsgi_app.py
│   │   ├── tasks
│   │   │   └── main.yaml
│   │   └── vars
│   │       └── main.yaml
│   ├── common
│   │   ├── tasks
│   │   │   └── main.yaml
│   │   └── vars
│   │       └── main.yaml
│   ├── db
│   │   ├── files
│   │   │   └── init-db.js
│   │   ├── tasks
│   │   │   └── main.yaml
│   │   └── vars
│   │       └── main.yaml
│   └── web
│       ├── files
│       │   ├── Dockerfile
│       │   └── nginx.conf
│       ├── tasks
│       │   └── main.yaml
│       └── vars
│           └── main.yaml
└── setup.yaml
```
## Demo
Run câu lệnh sau:
```
ansible-playbook -i inventories/inventory.yaml setup.yaml
```
Chi tiết logs:
```
PLAY [Setup Docker and Docker Compose] *****************************************

TASK [common : Install aptitude] ***********************************************
ok: [localhost]

TASK [common : Install required system packages] *******************************
ok: [localhost]

TASK [common : Add Docker GPG apt Key] *****************************************
ok: [localhost]

TASK [common : Add Docker Repository] ******************************************
ok: [localhost]

TASK [common : Update apt and install docker-ce] *******************************
ok: [localhost]

TASK [common : Install Docker Module for Python] *******************************
ok: [localhost]

TASK [common : Download Docker Compose binary] *********************************
ok: [localhost]

TASK [common : Create frontend network] ****************************************
ok: [localhost]

TASK [common : Create backend network] *****************************************
ok: [localhost]

TASK [common : Create appdata volume] ******************************************
```
Sau khi chạy thành công:
![alt](./md_images/main_page.jpg)
