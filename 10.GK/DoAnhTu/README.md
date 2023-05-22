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

Kết quả khi chạy 1 CI bất kỳ khi em commit lên git

