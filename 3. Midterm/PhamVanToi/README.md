
### Phát triển một 3-tier web application đơn giản

- DB: Mongodb
- Web: HTML, CSS, Javascript
- API: Python (Flask)

Mã nguồn dịch vụ API: `roles/api/files/app.py`

```
from flask import Flask, jsonify, render_template, request, redirect, url_for
import pymongo
from pymongo import MongoClient
import os
import json
from dao import get_db, insert_data, delete_data, update_data

app = Flask(__name__)


@app.route('/api/attendees', methods=['GET'])
def read():
    db=""
    try:
        db = get_db()
        all_attendees = db.internees.find()

        api_json = []

        for attendee in all_attendees:
            api_json.append({k: v for k, v in attendee.items() if k != '_id'})

        return json.dumps(api_json, ensure_ascii=False).encode('utf-8')
        
    except:
        pass
    finally:
        if type(db)==MongoClient:
            db.close()


@app.route('/api/create', methods=['POST'])
def creat_post():
    try:
        data = request.get_json()
        insert_data(
            data['id'], data['name'], data['username'], data['birth'], data['sex'], data['university'], data['major']
        )

        return jsonify(data)
    except:
        return "Error!"
    

    
@app.route('/api/update', methods=['POST'])
def update_post():
    try:
        data = request.get_json()
        update_data(
            data['id'], data['name'], data['username'], data['birth'], data['sex'], data['university'], data['major']
        )

        return jsonify(data)
    except:
        return "Error!"

@app.route('/api/delete/<int:id>')
def delete_post(id):

    id = str(id)
    try:    
        if id != '29':
            delete_data(id)
        return redirect("http://localhost:8000/")
    except:
        return "Error!"

@app.route('/api/read/<int:id>')
def read_post(id):

    id = str(id)
    try:
        db = get_db()
        students = []
        students.append(db.internees.find_one({"id": id}))

        api_json = []
        for attendee in students:
            api_json.append({k: v for k, v in attendee.items() if k != '_id'})

        
        return json.dumps(api_json, ensure_ascii=False).encode('utf-8')
    
    except:
        return "Error!"

if __name__=='__main__':
    # app.run(host="0.0.0.0", port=5000)
    app.run(host='0.0.0.0', port=9090, debug=True)
```

- Demo: 
![](images/three_tiers_web/demo_api.png)

 Mã nguồn dịch vụ Web `roles/web/files/frontend/`  
`index.html`: Giao diện thông tin thực tập sinh (dạng bảng)  
`update.html`: Form update thông tin thực tập sinh  
`create.html`: Form taọ mới thông tin thực tập sinh  

- Demo: 
![](images/three_tiers_web/demo_web.png)

### Triển khai web application sử dụng các DevOps tools & practices
## 1. Containerization
1. File Dockerfile cho từng dịch vụ

`roles\api\files\Dockerfile`: Dockerfile dịch vụ api  
`roles\web\files\Dockerfile`: Dockerfile dịch vụ web  
`roles\db\files\Dockerfile`: Dockerfile dịch vụ db  

2. Output câu lệnh build
 Build Mongodb Image
 ![](images/1.Containerization/docker_build_db.png)

  Build API Image
 ![](images/1.Containerization/docker_build_api.png)

  Build Web Image
 ![](images/1.Containerization/docker_build_web.png)


3. Thông tin docker history của từng image

 Mongodb Image History
 ![](images/1.Containerization/docker_history_db.png)

 API Image History
 ![](images/1.Containerization/docker_history_api.png)

 Web Image History
 ![](images/1.Containerization/docker_history_web.png)

 ## 2. CI
 1. File set up công cụ CI `github\workflows\ci.yml`

 ```
 name: Run unnittest automatically with PR on main and Push commit
on:
  pull_request:
    branches:
      - main
  push:
jobs:
  unit-test-CI:
    runs-on: ubuntu-latest
    steps:
    # Set up Enviroment
    - uses: actions/checkout@v3
    - uses: actions/setup-python@v4

    # Update your existing list of packages
    - name: Install docker
      run: |
        sudo apt-get update
        sudo apt install apt-transport-https ca-certificates curl software-properties-common
        curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
        sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
        sudo docker --version
        sudo apt install docker-ce

    # Pull image from DockerHub
    - name: Pull image from DockerHub
      run: |
        sudo docker pull crvt4722/my_db
        sudo docker pull crvt4722/my_flask
        sudo docker pull crvt4722/my_nginx

    # Create the network and run container
    - name: Run container
      run: |
        sudo docker network create mongodb_flask_nginx_network
        sudo docker run -d --name mongodb-server --network mongodb_flask_nginx_network crvt4722/my_db 
        sudo docker run -d --name flask_app --network mongodb_flask_nginx_network crvt4722/my_flask 
        sudo docker run -d -p 80:80 --link flask_app:flask --network mongodb_flask_nginx_network crvt4722/my_nginx

    - name: Run unittest
      run: python3 3.\ Midterm/PhamVanToi/roles/web/files/unit_test.py
 ```

2. Output luồng CI

https://github.com/crvt4722/Viettel-Digital-Talent-2023/actions/runs/5012132574/jobs/8983719684

![](images/2.CI/CI.png)

![](images/2.CI/log1.png)
![](images/2.CI/log2.png)
![](images/2.CI/log3.png)
![](images/2.CI/log4.png)
![](images/2.CI/log5.png)

## 3. CD And Ansible
1. Ảnh minh hoạ kiến trúc triển khai và mô tả

![](images/3.CD_and_Ansible/architecture.jpg)

Mô tả kiến trúc triển khai:

- Dịch vụ web và api được triển khai trên 2 container khác nhau.
- Requests đến dịch vụ web được cân bằng tải thông qua nginx.
- Request đến dịch vụ api và web cũng được cân bằng tải thông qua nginx.

2. File set up CD `.github/workflows/cd.yml`
```
name: Release service.
on:
  push:
    tags:
      - '*'

jobs:
  docker:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout
      uses: actions/checkout@v2
    
    - name: Login DockerHub
      uses: docker/login-action@v2
      with:
        username: ${{ secrets.DOCKERHUB_USERNAME }}
        password: ${{ secrets.DOCKERHUB_ACCESS_TOKEN }}

    - name: Setup Docker Buildx
      uses: docker/setup-buildx-action@v2
      id: buildx
    
    - name: Build and Push Mongodb Image
      uses: docker/build-push-action@v2
      env:
        VERSION: ${{ steps.extract_version.outputs.version }}
      with:
        context: ./3. Midterm/PhamVanToi/roles/db/files
        builder: ${{ steps.buildx.outputs.name }}
        tags: ${{ secrets.DOCKERHUB_USERNAME }}/my_db:${{ env.VERSION }}
        push: true
    
    - name: Build and Push Flask API Image
      uses: docker/build-push-action@v2
      env:
        VERSION: ${{ steps.extract_version.outputs.version }}
      with:
        context: ./3. Midterm/PhamVanToi/roles/api/files
        builder: ${{ steps.buildx.outputs.name }}
        tags: ${{ secrets.DOCKERHUB_USERNAME }}/my_flask:${{ env.VERSION }}
        push: true
    
    - name: Build and Push Web Nginx Image
      uses: docker/build-push-action@v2
      env:
        VERSION: ${{ steps.extract_version.outputs.version }}
      with:
        context: ./3. Midterm/PhamVanToi/roles/web/files
        builder: ${{ steps.buildx.outputs.name }}
        tags: ${{ secrets.DOCKERHUB_USERNAME }}/my_nginx:${{ env.VERSION }}
        push: true

```
3. Output của luồng CD và dockerhub 

https://github.com/crvt4722/Viettel-Digital-Talent-2023/actions/runs/5012154539/jobs/8983768256

![](images/3.CD_and_Ansible/cd_log.png)
![](images/3.CD_and_Ansible/db_log1.png)
![](images/3.CD_and_Ansible/db_log2.png)
![](images/3.CD_and_Ansible/api_log1.png)
![](images/3.CD_and_Ansible/api_log2.png)
![](images/3.CD_and_Ansible/api_log3.png)
![](images/3.CD_and_Ansible/web_log1.png)
![](images/3.CD_and_Ansible/web_log2.png)
![](images/3.CD_and_Ansible/db_tag.png)
![](images/3.CD_and_Ansible/flask_tag.png)
![](images/3.CD_and_Ansible/nginx_tag.png)

4. Hướng dẫn sử dụng ansible playbook để triển khai hệ thống

Install virtualenv
  ```
  sudo apt install python3-virtualenv
  ```

Activate virtualenv
  ```
  virtualenv venv && source venv/bin/activate
  ```

Install ansible inside virtualenv
  ```
  pip install ansible
  ```

Test ansible installation:
  ```
  ansible --version
  ```

Install community.docker
  ```
  ansible-galaxy collection install community.docker
  ```
Run the command:
  ```
  ansible-playbook -i inventory.yml playbooks/ansible.yml
  ```
5. Output log triển khai hệ thống

![](images/3.CD_and_Ansible/ansible_common_log.png)

## 4. Monitoring

1. Hướng dẫn sử dụng ansible playbook để triển khai monitoring

Run the command:
  ```
  ansible-playbook -i inventory.yml playbooks/monitoring.yml
  ```

2. Ảnh chụp dashboard giám sát nodes & containers

 
![](images/4.Monitor/prometheus.png)
![](images/4.Monitor/dashboard1.png)
![](images/4.Monitor/dashboard2.png)
![](images/4.Monitor/dashboard3.png)
![](images/4.Monitor/dashboard4.png)
![](images/4.Monitor/dashboard5.png)

## 5.Logging
1. Ảnh chụp sample log từ Kibana 171.236.38.100:5601

- Index management.
![](images/5.Logging/index_management.png)

- Kibana log
![](images/5.Logging/kibana_log.png)




