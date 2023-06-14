## Bài tập lớn Giữa Kỳ

### Lê Tùng Lâm

### Phát triển một 3-tier web application

- Mã nguồn backend APIs: [main.py](./Containerization/app/main.py)
- Mã nguồn frontend (static file): [index.html](./Containerization/nginx/index.html)
- Mã nguồn frontend (rendered by APIs): [attendees.html](./Containerization/app/templates/attendees.html)
- Mã nguồn Unit Tests cho các chức năng APIs: [test_main.py](./Containerization/tests/app/test_main.py)

- MongoDB database được sử dụng thông qua Docker image, database khởi tạo được thực hiện bằng file [init-mongo.js](./Containerization/db/mongo-init.js)

- Web server sử dụng Nginx thông qua Docker image, file cấu hình Nginx tại [nginx.conf](./Containerization/nginx/nginx.conf)

- CRUD APIs endpoints:
  ![alt](./images/api-endpoints.png)

- Static webpage triển khai ở cổng 81 trên Nginx:
  ![alt](./images/static-webpage.png)

- Rendered webpage được triển khai thông qua python backend APIs:
  ![alt](./images/rendered-webpage.png)

### Triển khai web application sử dụng các DevOps tools & practices

#### 1. Containerization

##### Dockerfile cho từng dịch vụ:

- [APIs](./Containerization/app/Dockerfile)

  ```Dockerfile
    FROM python:3.9-alpine

    WORKDIR /app

    COPY . .

    RUN pip install "fastapi[all]" pymongo --no-cache-dir

    CMD uvicorn main:app --reload --host 0.0.0.0 --port 8000
  ```

- Nginx sử dụng lại [Docker image](https://hub.docker.com/_/nginx) trên Docker Hub mà không cần build image mới. [File cấu hình Nginx](./Containerization/nginx/nginx.conf):

  ```
  events {
      worker_connections 1000;
  }

  http {
      server {
          listen 80;
          server_name app;

          location / {
              proxy_pass http://app:8000;
          }
      }

      server {
          listen 81;
          server_name 127.0.0.1;

          location / {
              root    /usr/share/nginx/html;
              index   index.html;
          }
      }
  }
  ```

- MongoDB database sử dụng lại Docker image trên Docker Hub mà không cần build image mới. File khởi tạo database [mongo-init.js](./Containerization/db/mongo-init.js):

  ```js
  /* Phiên bản demo rút gọn chỉ có 1 bản ghi */

  db = db.getSiblingDB("vdt");

  db.createCollection("attendees");

  db.attendees.insertMany([
    {
      id: 1,
      name: "Bùi Minh Sơn",
      username: "sonbm",
      birthyear: "2002",
      gender: "Nam",
      university: "Đại học Công nghệ - Đại học Quốc gia Hà Nội",
      major: "Công nghệ thông tin",
    },
  ]);
  ```

##### Output câu lệnh build và thông tin docker history của từng image

- APIs

  ![alt](./images/build-api-image-1.png)

  ![alt](./images/build-api-image-2.png)

  ![alt](./images/api-image-history.png)

- Nginx (không build lại nên chỉ có history)
  ![alt](./images/nginx-history.png)

- MongoDB (không build lại nên chỉ có history)
  ![alt](./images/mongo-history.png)

#### 2. Continuous Integration

- File setup công cụ CI:

```yaml
name: CI/CD

on:
  push:
    branches: 
      - '*' 
  pull_request:
    branches: [ "main" ]

permissions:
  contents: read

jobs:
  unit-testing:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3
    - name: Set up Python 3.9.16
      uses: actions/setup-python@v3
      with:
        python-version: "3.9.16"
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install flake8 pytest
        if [ -f ./10.GK/Containerization/requirements.txt ]; then pip install -r ./10.GK/Containerization/requirements.txt; fi
    - name: Lint with flake8
      run: |
        # stop the build if there are Python syntax errors or undefined names
        flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
        # exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
        flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
    - name: Turn on database
      run: |
        docker compose -f ./10.GK/Containerization/docker-compose-db.yaml up -d
    - name: Test with pytest
      run: |
        pytest 10.GK/Containerization/tests/app/test_main.py
```

- Output log của luồng CI

  ![alt](./images/CI-log-1.png)
  ![alt](./images/CI-log-2.png)
  ![alt](./images/CI-log-4.png)

#### 3. Continuous Delivery

##### Viết luồng release dịch vụ bằng công cụ CI/CD của GitHub/GitLab, thực hiện build docker image và push docker image lên Docker Hub khi có event một tag mới được developer tạo ra trên GitHub.

- File set up CD:

  ```yaml
  name: Build and push image to Docker Hub

  on:
    push:
      tags:
        - '*'

  permissions:
    contents: read

  jobs:
    build-and-push:
      runs-on: ubuntu-latest
      steps:
        -
          name: Checkout
          uses: actions/checkout@v3
        -
          name: Login to Docker Hub
          uses: docker/login-action@v2
          with:
            username: ${{ secrets.DOCKERHUB_USERNAME }}
            password: ${{ secrets.DOCKERHUB_TOKEN }}
        -
          name: Set up Docker Buildx
          uses: docker/setup-buildx-action@v2
        -
          name: Build and push
          uses: docker/build-push-action@v4
          with:
            context: 10.GK/Containerization/app
            file: 10.GK/Containerization/app/Dockerfile
            push: true
            tags: ${{ secrets.DOCKERHUB_USERNAME }}/vt_app:${{  github.ref_name }}
  ```


##### Viết ansible playbook thực hiện các nhiệm vụ:
- Setup môi trường: Cài đặt docker trên các node triển khai dịch vụ:

  ![alt](./images/ansible-docker.png)

  Role [common](./Ansible/roles/common/tasks/main.yaml) cài đặt Docker:
  ```yaml
  - name: Update the apt package index
    ansible.builtin.package:
      update_cache: "{{ update_cache }}"

  - name: Install packages to allow apt to use a repository over HTTPS
    ansible.builtin.package:
      name: "{{ item }}"
      state: present
    loop:
      - ca-certificates
      - curl
      - gnupg

  - name: Add Docker GPG apt Key
    apt_key:
      url: https://download.docker.com/linux/ubuntu/gpg
      state: present

  - name: Add Docker Repository
    apt_repository:
      repo: deb https://download.docker.com/linux/ubuntu jammy stable
      state: present

  - name: Update apt and install docker-ce
    apt:
      name: docker-ce
      state: latest
      update_cache: true

  - name: Create docker group
    group:
      name: docker

  - name: Add user to the docker group
    user:
      name: "{{ ansible_user }}"
      group: docker
  ```

- Deploy các dịch vụ sử dụng Docker:
  ![alt](./images/ansible-deployment.png)
  Role [deployment](./Ansible/roles/deployment/tasks/main.yaml) để đơn giản hóa tác vụ triển khai dịch vụ:
  ```yaml
  - name: Copy deployment directory
    ansible.builtin.copy:
      src: /home/lamle/VDT-Cloud/Viettel-Digital-Talent-2023/10.GK/Deployment/
      dest: ~/Deployment/

  - name: Deploy
    command: chdir=/home/lamle/Deployment/ docker compose up -d
  ```

##### Đảm bảo tính HA cho web và api:
- Mô hình trên một host:

  ![alt](./images/kientruc.png)

- Mô hình đảm bảo tính HA:
  ![alt](./images/HA.png)
  Trong đó MongoDB sẽ chạy trên một host riêng, Nginx webser + FastAPI sẽ được scale thành 2 hosts để đảm bảo tính HA. Còn Nginx load balancer sẽ chạy trên máy chính để cân bằng tải cho 2 host webserver + fastapi.

  Do giới hạn về tài nguyên nên em chỉ thực hiện mô hình trên một host, nhưng vẫn đảm bảo tính HA cho web và api. Mô hình này hoàn toàn có thể dễ dàng triển khai trên nhiều host khác nhau. Sau đây là video demo mô hình HA:
  ![alt](./images/HA.gif)

  Có thể thấy khi thực hiện call API get hostname thì lần lượt các host sẽ được Load Banlancer phân phối request tới (ở đây mặc định sử dụng chiến lược Round Robin).

  Thư mục [HA/Deployment](./HA/Deployment/) chứa file docker-compose.yaml cũng như các cấu hình của DB và Nginx để triển khai mô hình HA.

  - File [docker-compose.yaml](./HA/Deployment/docker-compose.yaml):
  ```Dockerfile
  version: '3.8'

  services:

    app-1:
      build: app
      restart: always
      expose:
        - "8000"
      links:
        - db

    nginx-1:
      image: nginx:1.22.0-alpine
      container_name: nginx-1
      restart: always
      volumes:
        - ./nginx-1/nginx.conf:/etc/nginx/nginx.conf:ro
        - ./nginx-1/index.html:/usr/share/nginx/html/index.html:ro
      depends_on:
        - app-1
        - db


    app-2:
      build: app
      restart: always
      expose:
        - "8000"
      links:
        - db

    nginx-2:
      image: nginx:1.22.0-alpine
      container_name: nginx-2
      restart: always
      volumes:
        - ./nginx-2/nginx.conf:/etc/nginx/nginx.conf:ro
        - ./nginx-2/index.html:/usr/share/nginx/html/index.html:ro
      depends_on:
        - app-2
        - db

    db:
      image: mongo:5.0-focal
      hostname: mongodb
      container_name: vt_db
      restart: always
      volumes:
        - ./db/mongo-init.js:/docker-entrypoint-initdb.d/mongo-init.js:ro

  # Load balancer
    nginx-lb:
      image: nginx:1.22.0-alpine
      container_name: lb
      restart: always
      volumes:
        - ./lb/nginx.conf:/etc/nginx/nginx.conf:ro
      depends_on:
        - nginx-1
        - nginx-2
      ports:
        - "80:80"
  ```
  - File [nginx.conf](./HA/Deployment/lb/nginx.conf):
  ```Conf
  # events are used to set general configurations on how
  # nginx will handle the connection requests
  events {}

  http {
      # Define the group of servers available
      upstream app {
          # server app;
          server nginx-1:80;
          server nginx-2:80;
      }
      server {
          # Server group will respond to port 80
          listen 80;
          server_name app.com;
          location / {
              proxy_pass http://app;
          }
      }
  }
  ```


- Hướng dẫn sử dụng `ansible playbook` để triển khai các thành phần hệ thống

  Cây thư mục Ansible:

  ![alt](./images/ansible-tree.png)

  - Danh sách các roles:
    - [common](./Ansible/roles/common/tasks/main.yaml)
    - [web](./Ansible/roles/web/tasks/main.yaml)
    - [api](./Ansible/roles/api/tasks/main.yaml)
    - [db](./Ansible/roles/db/tasks/main.yaml)
    - [lb](./Ansible/roles/lb/tasks/main.yaml)
    - [deployment](./Ansible/roles/deployment/tasks/main.yaml)

  Chạy ansible playbook sử dụng lệnh:
  ```bash
  ansible-playbook -i inventories.yaml setup.yaml --extra-vars "ansible_sudo_pass=0"
  ```

- Output log triển khai hệ thống
  
    ![alt](./images/ansible-deployment.png)


#### 4. Monitoring
  - Code [role monitoring](./Ansible/roles/monitoring)
  ```shell
  ansible-playbook -i inventories.yaml setup.yaml --extra-vars "ansible_sudo_pass=YOUR_REMOTE_PASSWORD"
  ```
  - Kết quả:
    ![image](./images/prom-1.png)
    ![image](./images/prome-2.png)

  - File cấu hình Prometheus:
    ```conf
    global:
      scrape_interval: 15s
      evaluation_interval: 15s

      # Attach these labels to any time series or alerts when communicating with
      # external systems (federation, remote storage, Alertmanager).
      external_labels:
          username: lamlt

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
      name: lamlt
    ```
#### 5. Logging
  - Code [role logging](./Ansible/roles/logging)
  ```shell
  ansible-playbook -i inventories.yaml setup.yaml --extra-vars "ansible_sudo_pass=YOUR_REMOTE_PASSWORD"
  ```
  - Kêt quả chạy thành công logging role playbook:
    ![image](./images/logging.png)
  - Kết quả sample log lấy từ Kibana

    ![image](./images/kibana-0.png)
