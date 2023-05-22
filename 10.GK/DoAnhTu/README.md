# ***Bài tập lớn giữa kì***

## **Phát triển một 3-tier web application đơn giản (2đ)**

### **Viết một CRUD web application đơn giản thực hiện các chức năng**
Dưới đây là kiến trúc web-application của em
```tree
└── DoAnhTu
    ├── app
    │   ├── Dockerfile
    │   ├── requirements.txt
    │   ├── test
    │   │   ├── test_app_api.py
    │   │   └── test_requirements.txt
    │   └── VDT
    │       ├── __init__.py
    │       └── templates
    │           └── VDT.html
    ├── docker-compose.yml
    ├── mongo-entrypoint
    │   └── init-mongo.js
    ├── nginx
    │   └── conf.d
    │       └── default.conf
    └── README.md
```

### 1. Liệt kê danh sách sinh viên tham gia khóa đào tạo chương trình VDT 2023 lĩnh vực cloud dưới dạng bảng
Trong thư mục app bao gồm

1. VDT là thư mục của chương trình chính
```python

#VDT/__init__.py
import os

from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_pymongo import MongoClient


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    # connect to db

    client = MongoClient(
        "mongodb://admin:Admin123@mongodb:27017/", connectTimeoutMS=3000
    )
    VDT_DB = client.VDTuser
    db = VDT_DB.user

    @app.route("/")
    def VDT():
        students = db.find()
        student_data = []

        for student in students:
            person = {
                "name": student["name"],
                "year_of_birth": student["year_of_birth"],
                "university": student["university"],
                "gender": student["gender"],
                "username": student["username"],
                "major": student["major"],
            }
            student_data.append(person)
        return render_template("VDT.html", data_student=student_data)

    @app.route("/members", methods=["GET"])
    def getlistmember():
        students = db.find()
        student_data = []

        for student in students:
            person = {
                "name": student["name"],
                "year_of_birth": student["year_of_birth"],
                "university": student["university"],
                "gender": student["gender"],
                "username": student["username"],
                "major": student["major"],
            }
            student_data.append(person)
        return jsonify(student_data)

    @app.route("/members/<username>", methods=["GET"])
    def get_student(username):
        students = db.find()
        members = []
        for student in students:
            person = {
                "name": student["name"],
                "year_of_birth": student["year_of_birth"],
                "university": student["university"],
                "gender": student["gender"],
                "username": student["username"],
                "major": student["major"],
            }
            if student["username"] == username:
                members.append(person)
        return jsonify(members)

    @app.route("/postdata", methods=["POST"])
    def post_student():
        name = request.json["name"]
        year_of_birth = request.json["year_of_birth"]
        university = request.json["university"]
        gender = request.json["gender"]
        username = request.json["username"]
        major = request.json["major"]

        db.insert_one(
            {
                "name": name,
                "year_of_birth": year_of_birth,
                "university": university,
                "gender": gender,
                "username": username,
                "major": major,
            }
        )
        return jsonify(
            {
                "name": name,
                "year_of_birth": year_of_birth,
                "university": university,
                "gender": gender,
                "username": username,
                "major": major,
            }
        )

    @app.route("/delmember/<username>", methods=["DELETE"])
    def del_mem(username):
        db.delete_one({"username": username})
        return redirect(url_for("getlistmember"))

    @app.route("/updatemember/<username>", methods=["PUT"])
    def up_mem(username):
        name = request.json["name"]
        year_of_birth = request.json["year_of_birth"]
        university = request.json["university"]
        gender = request.json["gender"]
        update_username = request.json["username"]
        major = request.json["major"]

        myquery = {"username": username}
        myupdate = {
            "$set": {
                "name": name,
                "year_of_birth": year_of_birth,
                "university": university,
                "gender": gender,
                "username": update_username,
                "major": major,
            }
        }
        db.update_one(myquery, myupdate)

        return redirect(url_for("getlistmember"))

    return app

```

**kết quả**

1. Trang chính
    <div align="center">
        <img src="./image/homepage.png" width="1000" />
    </div>

**`Vì em chưa làm frontend nên các chức năng thêm sửa xóa em xin phép show bằng api của chương trình`**

2. Xem thông tin tất cả member bằng get method

```python
    @app.route("/members", methods=["GET"])
    def getlistmember():
        students = db.find()
        student_data = []

        for student in students:
            person = {
                "name": student["name"],
                "year_of_birth": student["year_of_birth"],
                "university": student["university"],
                "gender": student["gender"],
                "username": student["username"],
                "major": student["major"],
            }
            student_data.append(person)
        return jsonify(student_data)
```



<div align="center">
        <img src="./image/getmems.png" width="1000" />
    </div>




2. Xem thông tin một member bằng username của họ


```link
http://192.168.60.135:8000/members/tuda
```

```python
    @app.route("/members/<username>", methods=["GET"])
    def get_student(username):
        students = db.find()
        members = []
        for student in students:
            person = {
                "name": student["name"],
                "year_of_birth": student["year_of_birth"],
                "university": student["university"],
                "gender": student["gender"],
                "username": student["username"],
                "major": student["major"],
            }
            if student["username"] == username:
                members.append(person)
        return jsonify(members)
```

<div align="center">
        <img src="./image/onemem.png" width="1000" />
</div>


3. Thêm member 

Member được thêm có data như sau
```json
{
        "name": "Nguyen Thi Thuy Quynh",
        "year_of_birth": "2001",
        "university": "UET",
        "gender": "Female",
        "username": "quynhntt1",
        "major": "computer science",
    }
```

```python
    @app.route("/postdata", methods=["POST"])
    def post_student():
        name = request.json["name"]
        year_of_birth = request.json["year_of_birth"]
        university = request.json["university"]
        gender = request.json["gender"]
        username = request.json["username"]
        major = request.json["major"]

        db.insert_one(
            {
                "name": name,
                "year_of_birth": year_of_birth,
                "university": university,
                "gender": gender,
                "username": username,
                "major": major,
            }
        )
        return jsonify(
            {
                "name": name,
                "year_of_birth": year_of_birth,
                "university": university,
                "gender": gender,
                "username": username,
                "major": major,
            }
        )
```

<div align="center">
        <img src="./image/post1.png" width="1000" />
</div>

Sau đó load lại trang chính để xem data vừa được thêm vào trang chính
<div align="center">
        <img src="./image/post2.png" width="1000" />
</div>


3. Sửa thông tin member

```json
data cũ
{
        "name": "Nguyen Thi Thuy Quynh",
        "year_of_birth": "2001",
        "university": "UET",
        "gender": "Female",
        "username": "quynhntt1",
        "major": "computer science"
    }
```


```json
data mới
{
        "name": "Nguyen Thi Thuy Quynh",
        "year_of_birth": "2002",
        "university": "HUST",
        "gender": "Female",
        "username": "quynhntt1",
        "major": "computer science",
    }
```
```link
http://192.168.60.135:8000/updatemember/quynhntt1
```
```python
    @app.route("/updatemember/<username>", methods=["PUT"])
    def up_mem(username):
        name = request.json["name"]
        year_of_birth = request.json["year_of_birth"]
        university = request.json["university"]
        gender = request.json["gender"]
        update_username = request.json["username"]
        major = request.json["major"]

        myquery = {"username": username}
        myupdate = {
            "$set": {
                "name": name,
                "year_of_birth": year_of_birth,
                "university": university,
                "gender": gender,
                "username": update_username,
                "major": major,
            }
        }
        db.update_one(myquery, myupdate)

        return redirect(url_for("getlistmember"))
```
Kết quả
<div align="center">
        <img src="./image/edit.png" width="1000" />
</div>

4. Xóa members

```python
    @app.route("/delmember/<username>", methods=["DELETE"])
    def del_mem(username):
        db.delete_one({"username": username})
        return redirect(url_for("getlistmember"))
```

```link
http://192.168.60.135:8000/delmember/quynhntt1
```

Kết quả
<div align="center">
        <img src="./image/del1.png" width="1000" />
</div>


### 2. Kiến trúc dịch vụ

- API ở đây được sử dụng bởi framework flask

- DB mongodb

- Nginx có tác dụng là loadbalancer

### 3. Unit test

Pytest là tool được sử dụng để test api

Em chia test ra làm 6 phần
- test truy cập vào homepage
```python
def test_can_access_homepage():
    respone = requests.get(ENDPOINT)
    assert respone.status_code == 200
```

- test api members `http://127.0.0.1:8000/members`

```python
def test_can_call_endpoint():
    respone = requests.get(ENDPOINT + "members")
    assert respone.status_code == 200
    data = respone.json()
    print(data)

```

- test member trên web có khớp với db không `http://127.0.0.1:8000/members`

```python
def test_user_api():
    students = db.find()
    for student in students:
        username = student["username"]
        respone = requests.get(ENDPOINT + f"members/{username}")
        assert respone.status_code == 200

```
Trong đó students em config với db user `mongodb` có sẵn trong server
```python
ENDPOINT = "http://127.0.0.1:8000/"
client = MongoClient("mongodb://admin:Admin123@127.0.0.1:27017/", connectTimeoutMS=3000)
VDT_DB = client.VDTuser
db = VDT_DB.user
```


- test thêm member

```python
def test_can_create_mem():
    payload = {
        "name": "Nguyen Thi Thuy Quynh",
        "year_of_birth": "2001",
        "university": "UET",
        "gender": "Female",
        "username": "quynhntt1",
        "major": "computer science",
    }
    respone = requests.post(ENDPOINT + "postdata", json=payload)

    assert respone.status_code == 200
    data = respone.json()
    print(data)


```


- test sửa member

```python
def test_can_update_mem():
    payload = {
        "name": "Nguyen Thi Thuy Quynh",
        "year_of_birth": "2002",
        "university": "UET",
        "gender": "Female",
        "username": "quynhntt",
        "major": "network and communication",
    }

    username = payload["username"]
    respone = requests.put(ENDPOINT + f"/updatemember/{username}", json=payload)
    assert respone.status_code == 200

    data = respone.json()
    print(data)
```


- test xóa member
```python
def test_can_del_mem():
    username = "quynhntt1"

    respone = requests.delete(ENDPOINT + f"delmember/{username}")
    assert respone.status_code == 200
    print(respone.status_code)
```

#### Kết quả khi chạy test
```cmd
pip install pytest
pytest test_app_api.py
```

<div align="center">
        <img src="./image/test.png" width="1000" />
</div>
 Kết quả pass với 6 test

## **Triển khai web application sử dụng các DevOps tools & practices(8đ)**

### 1. Containerization (1đ)

**Dockerfile for flask app**

```Dockerfile
# Dockerfile for flask app
FROM python:3.9

ENV FLASK_APP=VDT/__init__.py
ENV FLASK_ENV=production



WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt



COPY . .





CMD [ "flask", "run", "--host=0.0.0.0" ]


```

Ở đây em có sử dụng thủ thuật layer caching cho 
```Dockerfile
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt



COPY . .

```
Điều đó nhằm tránh việc tải lại requirements.txt khi có source code thay đổi

Ngoài ra em có thêm file `.dockerignore` để cho docker biết không copy những file không cần thiết vào trong docker


**docker-compose.yml**

```yml
version: '3'
services:
  appuser1:
    build: ./app
    depends_on:
      - mongodb
    ports:
      - 5000:5000
    networks:
      - db
      - app
    
  
  appuser2:
    build: ./app
    depends_on:
      - mongodb
    ports:
      - 5001:5000
    networks:
      - db
      - app
    

    
    
  nginx-production:
    image: nginx:1.22.0-alpine
    ports:
      - 8000:80
    volumes:
      - ./nginx/conf.d/:/etc/nginx/conf.d/
    depends_on:
      - appuser1
      - appuser2
    networks:
      - app


  mongodb:
    image: mongo:5.0 

    environment:
      - MONGO_INITDB_ROOT_USERNAME=admin
      - MONGO_INITDB_ROOT_PASSWORD=Admin123
      - MONGO_INITDB_DATABASE=VDTuser
    
    ports:
      - 27017:27017
    volumes:
      - db1:/data/db
      - ./mongo-entrypoint:/docker-entrypoint-initdb.d
    networks:
      - db
    
volumes:
  db1:

networks:
  db:
    driver: bridge
  app:
    driver: bridge

```

**output**

```cmd
docker compose up -d
```

Do nginx và mongo em sử dụng image default nên em sẽ show history của flask app

history flask app
<div align="center">
        <img src="./image/hisflask.png" width="1000" />
</div>



### 2. Continuous Integration(1đ)
● Tự động chạy unit test khi tạo PR vào branch main (0.5đ)

● Tự động chạy unit test khi push commit lên một branch (0.5đ)
```yml
# This is a basic workflow to help you get started with Actions

name: CI

# Controls when the workflow will run
on:
  # Triggers the workflow on push or pull request events but only for the "main" branch
  push:
    branches: ["*"]
  pull_request:
    branches: ["main"]

  # Allows you to run this workflow manually from the Actions tab
  workflow_dispatch:

# A workflow run is made up of one or more jobs that can run sequentially or in parallel
jobs:
  # This workflow contains a single job called "build"
  build:
    # The type of runner that the job will run on
    runs-on: ubuntu-latest

    # Steps represent a sequence of tasks that will be executed as part of the job
    steps:
      # Checks-out your repository under $GITHUB_WORKSPACE, so your job can access it
      - uses: actions/checkout@v3

      # deploy apllication by docker compose to test
      - name: Docker Compose Action
        uses: isbang/compose-action@v1.4.1
        with:
          compose-file: "./10.GK/DoAnhTu/docker-compose.yml"
          down-flags: "--volumes"

      # Test application run or die
      - name: Test application run or die
        run: |
          curl 127.0.0.1:5000
          curl 127.0.0.1:5001
          curl 127.0.0.1:8000

      - name: Run test by pytest
        run: |
          cd 10.GK/DoAnhTu/app/test
          python3 --version
          pip install pytest
          pip install -r test_requirements.txt
          pytest -s

```


Ở file Ci có hai phần test là test từng container có hoạt động không và test theo unit được code tại phần 1

**Kết quả khi chạy 1 CI bất kỳ khi em commit lên git**

[Kiểm tra output tại đây](https://github.com/batamsieuhang/Viettel-Digital-Talent-2023/actions/runs/5045752582/jobs/9050418679)

CI
<div align="center">
        <img src="./image/CI.png" width="1000" />
</div>


- Test ping to web
<div align="center">
        <img src="./image/CI1.png" width="1000" />
</div>

- Pytest in CI

<div align="center">
        <img src="./image/CI2.png" width="1000" />
</div>


<div align="center">
        <img src="./image/CI3.png" width="1000" />
</div>

### **3. Continuous Delivery (4đ)**

#### **3.1 Viết luồng release dịch vụ bằng công cụ CI/CD của GitHub/GitLab, thực hiện build docker image và push docker image lên Docker Hub khi có event một tag mới được developer tạo ra trên GitHub**

```yml
# file setup CI
name: Release Workflow

on:
  push:
    tags:
      - "*"

jobs:
  build-and-push:
    runs-on: ubuntu-latest

    steps:
      - name: Login to Docker Hub
        run: |
          echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin
        env:
          DOCKER_USERNAME: ${{ secrets.DOCKER_USER}}
          DOCKER_PASSWORD: ${{ secrets.DOCKER_PASSWORD }}

      # Checks-out your repository under $GITHUB_WORKSPACE, so your job can access it
      - uses: actions/checkout@v3

      - name: Build and push Docker images
        run: |
          cd 10.GK/DoAnhTu/
          docker-compose build
          docker images
          docker tag doanhtu_appuser ${{ secrets.DOCKER_USER}}/doanhtu_appuser:${{  github.ref_name }}
          docker push ${{ secrets.DOCKER_USER}}/doanhtu_appuser:${{  github.ref_name }}
        env:
          DOCKER_USERNAME: ${{ secrets.DOCKER_USER }}
          DOCKER_PASSWORD: ${{ secrets.DOCKER_PASSWORD }}

```


**Mô tả**

```yml
on:
  push:
    tags:
      - "*"
```
Khi có 1 tag được tạo trên git thì luồng CD này sẽ tự động được triển khai theo hai bước
- Bước 1 là đăng nhập tài khoản dockerhub
```yml
name: Login to Docker Hub
        run: |
          echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin
        env:
          DOCKER_USERNAME: ${{ secrets.DOCKER_USER}}
          DOCKER_PASSWORD: ${{ secrets.DOCKER_PASSWORD }}
```

- Bước 2: build image rồi push lên docker hub
```yml
- name: Build and push Docker images
        run: |
          cd 10.GK/DoAnhTu/
          docker-compose build
          docker images
          docker tag doanhtu_appuser ${{ secrets.DOCKER_USER}}/doanhtu_appuser:${{  github.ref_name }}
          docker push ${{ secrets.DOCKER_USER}}/doanhtu_appuser:${{  github.ref_name }}
        env:
          DOCKER_USERNAME: ${{ secrets.DOCKER_USER }}
          DOCKER_PASSWORD: ${{ secrets.DOCKER_PASSWORD }}
```


**Output**

Ảnh luồng build and push được chạy trên github action khi tạo 1 tag là v1.1.0
[Kiểm tra output tại đây](https://github.com/batamsieuhang/Viettel-Digital-Talent-2023/actions/runs/5022462629)

<div align="center">
        <img src="./image/CD1.png" width="1000" />
</div>


[Image sau khi build xong được đẩy lên dockerhub](https://hub.docker.com/layers/mr4x2/doanhtu_appuser/v1.1.0/images/sha256-dca2361f5aab59df2d1c248440132de5f15d79d1645cce0e770440d26e41cf15?context=repo)

<div align="center">
        <img src="./image/CD2.png" width="1000" />
</div>

#### **3.2 Viết ansible playbook thực hiện các nhiệm vụ**

**Cấu trúc ansible em sử dụng**
```tree
├── ansible.cfg
├── config.yml
├── hosts-dev
├── roles
│   ├── common
│   │   └── tasks
│   │       └── main.yml
│   ├── loadbalancer
│   │   ├── tasks
│   │   │   └── main.yml
│   │   └── templates
│   │       └── default.conf
│   ├── logging
│   │   ├── tasks
│   │   │   └── main.yml
│   │   └── templates
│   │       ├── conf
│   │       │   └── fluent.conf
│   │       ├── docker-compose.yml
│   │       └── Dockerfile
│   ├── mongo
│   │   └── tasks
│   │       └── main.yml
│   ├── monitor
│   │   ├── tasks
│   │   │   └── main.yml
│   │   └── templates
│   │       ├── docker-compose.yml
│   │       └── prometheus.yml
│   └── webservers
│       └── tasks
│           └── main.yml
└── run.yml
```

Để config các host em sử dụng hai file đó là



Trong đó triển khai web chia làm 4 roles chính
- Setup môi trường tại roles common
```yaml
---
# tasks file for roles/common
- name: updating apt packages
  apt:
    name: "*"
    state: latest
    update_cache: true

- name: instal require packages for docker
  apt:
    pkg:
      - apt-transport-https
      - ca-certificates
      - curl
      - software-properties-common
      - python3-pip
      - python3-setuptools
    state: latest
    update_cache: true

- name: Add Docker GPG apt Key
  apt_key:
    url: https://download.docker.com/linux/ubuntu/gpg
    state: present

- name: Add Docker Repository
  apt_repository:
    repo: deb https://download.docker.com/linux/ubuntu focal stable
    state: present

- name: Update apt and install docker-ce
  apt:
    name: docker-ce
    state: latest
    update_cache: true

- name: Install Docker Module for Python
  pip:
    name:
      - docker
      - docker-compose
- name: add user to Docker group
  shell: "usermod -aG docker vm2"

- name: allow ports 8000, 5000, 5001
  ansible.builtin.shell: ufw allow 8000 && ufw allow 5000 && ufw allow 5001

```

roles common có các task chính như: update package in os, tải docker, mở port cho server

- Cài đặt mongo
```yml
---
# tasks file for roles/mongo
- name: Creates src directory
  file:
    path: /home/data
    state: directory
    mode: "0775"

- name: Copy file with owner and permissions
  ansible.builtin.copy:
    src: ../../../../mongo-entrypoint/init-mongo.js
    dest: /home/data
    mode: "0777"

- name: Create a volume
  community.docker.docker_volume:
    name: db1

- name: Create a network
  docker_network:
    name: network_db

- name: deploy mongo db
  community.docker.docker_container:
    name: mongodb
    image: mongo:5.0
    env:
      MONGO_INITDB_ROOT_USERNAME: "admin"
      MONGO_INITDB_ROOT_PASSWORD: "Admin123"
      MONGO_INITDB_DATABASE: "VDTuser"
    ports:
      - "27017:27017"
    volumes:
      - db1:/data/db
      - /home/data/init-mongo.js:/docker-entrypoint-initdb.d/init-mongo.js:ro
    networks:
      - name: network_db

```
Ở role install mongo tương tự với việc config service mongo tại docker compose

- Cài đặt web app
```yml
---
- name: Creates src directory
  file:
    path: /home/src
    state: directory
    mode: "0775"

- name: copy src to folder remote
  ansible.builtin.copy:
    src: ../../../../app/VDT
    dest: /home/src
- name: copy test to folder remote
  ansible.builtin.copy:
    src: ../../../../app/test
    dest: /home/src
- name: copy dockerfile to folder remote
  ansible.builtin.copy:
    src: ../../../../app/Dockerfile
    dest: /home/src
- name: copy requirements.txt to folder remote
  ansible.builtin.copy:
    src: ../../../../app/requirements.txt
    dest: /home/src

- name: Create a network
  docker_network:
    name: network_app

- name: create docker image flask app
  shell: docker build -t flask_python .
  args:
    chdir: /home/src

- name: create docker container flask app 1
  docker_container:
    name: flask1
    image: flask_python
    state: started
    ports:
      - "5000:5000"
    networks:
      - name: network_db
      - name: network_app
    log_driver: fluentd
    log_options:
      fluentd-address: "0.0.0.0:24224"
      tag: app1

- name: create docker container flask app 2
  docker_container:
    name: flask2
    image: flask_python
    state: started
    ports:
      - "5001:5000"
    networks:
      - name: network_db
      - name: network_app
    log_driver: fluentd
    log_options:
      fluentd-address: "0.0.0.0:24224"
      tag: app2

```
Có 2 điều cần chú ý tại web app đó là sẽ triển khai 2 container để đảm bảo Loadbalancer cho phần sau và có thêm log_driver cho fluentd để fluentd có thể lấy log từ flask app

- Cài đặt nginx loadbalancer

```yml
---
# tasks file for roles/loadbalancer
- name: Creates src directory
  file:
    path: /home/nginx
    state: directory
    mode: "0775"

- name: copy config nginx file to host
  ansible.builtin.copy:
    src: ../templates/default.conf
    dest: /home/nginx/conf.d/

- name: deploy nginx
  community.docker.docker_container:
    name: nginx
    image: nginx:1.22.0-alpine
    ports:
      - "8000:80"
    volumes:
      - /home/nginx/conf.d/:/etc/nginx/conf.d/
    networks:
      - name: network_app
    log_driver: fluentd
    log_options:
      fluentd-address: "0.0.0.0:24224"
      tag: app1

```

Tương tự webapp thì nginx cũng được cải driver fluentd để thuận tiện cho fluentd lấy log về sau

- file inventory của ansible
```conf
host-dev
[vm]
vm1 ansible_host=192.168.60.134
vm1 ansible_ssh_pass=******
vm1 ansible_user=vm1
vm1 ansible_sudo_pass=******

vm2 ansible_host=192.168.60.135
vm2 ansible_ssh_pass=******
vm2 ansible_user=vm2
vm2 ansible_sudo_pass=******
```

```cfg
# ansible.cfg
[defaults]
inventory = ./hosts-dev
host_key_checking = False
retry_files_enabled = False

```

File playbook triển khai cài đặt cơ bản, cài đặt web app, logging and monitor
```yml
# run.yml
---
- name: install configure package
  hosts: vm2
  become: true
  gather_facts: true
  roles:
    - common

- name: install logging and monitoring
  hosts: vm2
  become: true
  gather_facts: true
  roles:
    - monitor
    - logging

- name: install webapp
  hosts: vm2
  become: true
  gather_facts: true
  roles:
    - mongo
    - webservers
    - loadbalancer

```

để triển khai hệ thống vào thư mục ansible 
```cmd
ansible-playbook run.yml
```


**out put**


- output cài đặt common cho server
<div align="center">
        <img src="./image/play1.png" width="1000" />
</div>

- output cài đặt logging and monitoring

<div align="center">
        <img src="./image/play2.png" width="1000" />
</div>




- output cài đặt webapp

<div align="center">
        <img src="./image/play3.png" width="1000" />
</div>

#### **3.3 Load balancers**
Load balancers em sử dụng 2 container và 1 nginx, trong đó nginx có vai trò điều phối luồng cho 2 container.
Việc thực hiện Ha khi triển khai bằng ansible cũng tương tự khi triển khai Ha bằng containerization
Dưới đây là file config của nginx
```conf
upstream localhost {
    server appuser1:5000;
    server appuser2:5000;
}


server {
    listen 80;
    server_name _;

    location / {
        proxy_pass http://localhost;

    }
}



```
Mode load balancer được sử dụng tại nginx là roundrobin tức là luồng traffic sẽ được chia đều cho 2 container chạy web app(flask-app).

**out put khi sử dụng pytest test với localhost:8000(ip của nginx)**
<div align="center">
        <img src="./image/test1.png" width="1000" />
</div>


Khi test request tới nginx, request được chia đều tới cả appuser1 và appuser2




## **4. Monitoring (1đ)**

Cấu trúc của role monitoring
```tree
monitor
├── tasks
│   └── main.yml
└── templates
    ├── docker-compose.yml
    └── prometheus.yml
```


File playbook cấu hình monitor 
```yml
# main.yml
---
# tasks file for roles/monitoring
- name: Creates src directory
  file:
    path: /home/prometheus
    state: directory
    mode: "0775"

- name: Copy file with owner and permissions
  ansible.builtin.copy:
    src: ../templates/
    dest: /home/prometheus/
    mode: "0777"
- name: Run Docker Compose
  community.docker.docker_compose:
    project_src: /home/prometheus/
    build: no
    state: present
```

File playbook được tạo ra để cài đặt prometheus, node-exporter, cadvisor bằng docker compose

File docker compose cài đặt prometheus, node export
```yml
version: '3'
services:
  prometheus:
    image: prom/prometheus:v2.43.0
    container_name: prometheus
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml:ro
    command:
      - "--config.file=/etc/prometheus/prometheus.yml"
      - "--storage.tsdb.path=/prometheus"
      - "--web.console.libraries=/etc/prometheus/console_libraries"
      - "--web.console.templates=/etc/prometheus/consoles"
      - "--storage.tsdb.retention.time=200h"
      - "--storage.tsdb.max-block-duration=5d"
      - "--web.enable-lifecycle"
      - "--web.listen-address=:9090"
    restart: unless-stopped
    network_mode: host
    environment:
      TZ: "Asia/Ho_Chi_Minh"
    labels:
      org.label-schema.group: "monitoring"
  
  nodeexporter:
    image: prom/node-exporter:v1.5.0
    container_name: nodeexporter
    volumes:
      - /proc:/host/proc:ro
      - /sys:/host/sys:ro
      - /:/rootfs:ro
    command:
      - "--path.procfs=/host/proc"
      - "--path.rootfs=/rootfs"
      - "--path.sysfs=/host/sys"
      - "--collector.filesystem.ignored-mount-points=^/(sys|proc|dev|host|etc)($$|/)"
    restart: unless-stopped
    network_mode: host
    environment:
      TZ: "Asia/Ho_Chi_Minh"
    labels:
      org.label-schema.group: "monitoring"
  
  cadvisor:
    image: gcr.io/cadvisor/cadvisor:v0.47.1
    container_name: cadvisor
    privileged: true
    devices:
      - /dev/kmsg:/dev/kmsg
    volumes:
      - /:/rootfs:ro
      - /var/run:/var/run:ro
      - /sys:/sys:ro
      - /var/lib/docker:/var/lib/docker:ro
      #- /cgroup:/cgroup:ro #doesn't work on MacOS only for Linux
    restart: unless-stopped
    network_mode: host
    environment:
      TZ: "Asia/Ho_Chi_Minh"
    labels:
      org.label-schema.group: "monitoring"
```


File cấu hình prometheus
```yml
# prometheus.yml
---
global:
  scrape_interval: 15s
  evaluation_interval: 15s

  # Attach these labels to any time series or alerts when communicating with
  # external systems (federation, remote storage, Alertmanager).
  external_labels:
      username: tuda


alerting:
  alertmanagers:
  - scheme: http
    static_configs:
    - targets: 
      - 'localhost:9093'
      - 'localhost:9094'

# Load and evaluate rules in this file every 'evaluation_interval' seconds.
rule_files:
  - "alert.rules"

# remote_read:
#  - url: http://localhost:9090/api/v1/read

# A scrape configuration containing exactly one endpoint to scrape.
scrape_configs:
  - job_name: 'prometheus'
    static_configs:
    - targets: [
      'localhost:9090',
      'localhost:9091'
    ]


  - job_name: 'node-exporter'
    static_configs:
    - targets: [
      'localhost:9100',
      'demo.do.prometheus.io:9100'
    ]

  - job_name: 'cadvisor'
    static_configs:
    - targets: [
      'localhost:8080',
    ]

remote_write:
- url: 'http://27.66.108.93:9090/api/v1/write'
  name: tuda
```


**output**

Ảnh chụp dashboard
<div align="center">
        <img src="./image/prom1.png" width="1000" />
</div>



<div align="center">
        <img src="./image/prom2.png" width="1000" />
</div>


## **5. Logging (1đ)**


Ở đây e dùng ansible để cài fluentd bằng docker từ đó có thể đầy log lên server tập trung.


File ansible triển khai loggging
```yml
---
# tasks file for roles/logging
- name: Creates src directory
  file:
    path: /home/fluentd
    state: directory
    mode: "0775"

- name: Copy file with owner and permissions
  ansible.builtin.copy:
    src: ../templates/
    dest: /home/fluentd/
    mode: "0777"
- name: Run docker-compose
  shell: cd /home/fluentd/ && docker compose up -d

```



```Dockerfile
#docker file install fluentd
FROM fluent/fluentd:v1.12.0-debian-1.0
USER root
RUN ["gem", "install", "elasticsearch", "--no-document", "--version", "< 8"]
RUN ["gem", "install", "fluent-plugin-elasticsearch", "--no-document", "--version", "5.2.2"]
USER fluent
```

```yml
#docker compose
version: '3'
services:
  fluentd:
    container_name: fluentd
    build: /home/fluentd
    volumes:
        - ./conf:/fluentd/etc
    network_mode: "host"
    ports:
      - 24224:24224
      - 24224:24224/udp
    
```


File config fluentd
```conf
<source>
  @type forward
  port 24224
  bind 0.0.0.0
</source>

<filter *.**>
    @type record_transformer
    <record>
        Hostname ${hostname}
        ip ${record['ip']}
        time ${record['time']}
        action ${record['action']}
        result ${record['result']}
        username "tuda"
    </record>

</filter>

<match *.**>
    @type copy
    <store>
        @type elasticsearch
        host 171.236.38.100
        port 9200
        logstash_format true
        logstash_prefix tuda
        logstash_dateformat %Y%m%d
        include_tag_key true
        flush_interval 1s
    </store>
</match>
```


Lưu ý: cần cài đặt driver ở image của web, api để lấy được log từ conatiner. Vì vậy khi cài đặt web app, nginx thì em có thêm phần log driver của fluentd.


Ví dụ
<div align="center">
        <img src="./image/fluentd1.png" width="1000" />
</div>


**output sample log từ kibana**
<div align="center">
        <img src="./image/kibana1.png" width="1000" />
</div>



<div align="center">
        <img src="./image/kibana2.png" width="1000" />
</div>

**Em xin chân thành cảm ơn anh Lê Trọng Minh và anh Đang(mentee) đã giúp em hoàn thành được phần loggging này ạ!**