

# Ansible Homework
## Table of content

[I. Requirement](#)
Deploy your application in the docker-compose homework using ansible:
○ Setup docker for your target environments in role “common”
○ Split your application into 3 roles: “web”, “api” and “db”

[II. Homework](#)

- [Ansible Homework](#ansible-homework)
  - [Table of content](#table-of-content)
  - [1. Tree-structured directory](#1-tree-structured-directory)
  - [2. Configuration](#2-configuration)
    - [**Setup Docker**](#setup-docker)
      - [Role common:](#role-common)
      - [Role db](#role-db)
      - [Role api](#role-api)
      - [Role web](#role-web)
  - [3. Deployment](#3-deployment)
    

## 1. Tree-structured directory
<a name='tree'></a>

``` text
.
├── inventory.yml
├── README.md
├── result
│   ├── ansible-command.jpg
│   └── result.jpg
├── roles
│   ├── api
│   │   ├── files
│   │   │   ├── app.py
│   │   │   ├── Dockerfile
│   │   │   ├── requirements.txt
│   │   │   └── templates
│   │   │       └── index.html
│   │   └── tasks
│   │       └── main.yml
│   ├── common
│   │   ├── tasks
│   │   │   └── main.yml
│   │   └── vars
│   │       └── main.yml
│   ├── db
│   │   ├── tasks
│   │   │   └── main.yml
│   │   └── templates
│   │       ├── Dockerfile
│   │       └── init-db.js
│   └── web
│       ├── tasks
│       │   └── main.yml
│       └── templates
│           ├── Dockerfile
│           └── nginx.conf
├── secrets.yml
└── setup.yml
```

- `inventory.yml`: This file is used to define the inventory of hosts or servers on which Ansible will perform tasks.
- `result directory`: contain result images
- `roles` directory: This directory contains Ansible roles, which are reusable components that define specific tasks and configurations. 
  - `api`: This role is use for python application. It has a files directory containing application files such as app.py, Dockerfile, requirements.txt, and a templates directory with an index.html file. The `tasks` directory contains the main tasks for this role.
  - `common`: This role define common tasks, create a network to connect all the containers.
  - `db`:  It use for create db images and container.
  - `web`: this role to config nginx for my application.
- `setup.yaml`: this file contains all the tasks we want to execute in order
- `secret.yal`: contains password  after being encrypted with ansible vault.

## 2. Configuration
- The first is `inventory.yaml` file:
  
``` yaml
---

all:
  hosts:
    localhost:
      ansible_connection: local
      ansible_python_interpreter: /home/vinh/Desktop/test3/venv/local/bin/python
      ansible_become_user: root
      ansible_become_password_file: secrets.yml
    
```

- `all`: This indicates that the following configuration applies to all hosts in the inventory.

- `hosts`: This specifies the host or hosts for which the configuration is being defined. In this case, there is a single host named localhost.

- `localhost`: This is the name of the host being configured.

- `ansible_connection: local`: This line sets the connection type for the host to local, indicating that Ansible will execute tasks on the local machine where Ansible is being run.

- `ansible_python_interpreter:` /home/vinh/Desktop/test3/venv/local/bin/python: This line sets the Python interpreter path for Ansible to use when running tasks on the host. It points to the Python interpreter located at /home/vinh/Desktop/test3/venv/local/bin/python.

- `ansible_become_user: root`: This line specifies the user account to become when executing tasks on the host. In this case, Ansible will become the root user.

- `ansible_become_password_file: secrets.yml`: This line indicates the file where the password for the ansible_become_user (root) can be found. The file secrets.yml likely contains the password in an encrypted format.

### **Setup Docker**
#### Role common:
- Because I installed docker on my device, now I just need to create a network by using this module: 

``` text
- name: Create Docker network
  community.docker.docker_network:
    name: homework
    state: present
```
- `name`: This is the name of the task, which in this case is "Create Docker network".
- `community.docker.docker_network`: This is the module being invoked. It belongs to the `docker_collection` provided by the Ansible Community Modules.
- `name: homework`: This parameter specifies the name of the Docker network to be created. In this case, the network will be named "homework".

#### Role db
- `Docker file`: this Dockerfile is based on the mongo:5.0 image and copies an init-db.js file into the appropriate location for database initialization.
``` text
FROM mongo:5.0

COPY ./init-db.js /docker-entrypoint-initdb.d/init-db.js
  ```

- File `main.yml`: when executed in an Ansible playbook, will build the "db_image" Docker image based on the Dockerfile located at ./roles/db/templates and create a Docker container named "db" using that image. The container will have a restart policy of "unless-stopped" and will be connected to the "homework" network.
``` text
---
- name: Build db image
  community.docker.docker_image:
    name: db_image
    build:
      path: ./roles/db/templates
    source: "build"
    force_source: true

- name: Create db container
  community.docker.docker_container:
    name: db
    image: db_image
    restart_policy: "unless-stopped"
    networks:
      - name: homework
```
#### Role api
- `Docker` file: this Dockerfile sets up a Python development environment using the Alpine variant of the Python 3.9 image, installs dependencies from requirements.txt, copies the application code, exposes port 9090, and sets the command to run the app.py script.
``` text
ARG DOCKER_BUILDKIT=1

FROM python:3.9-alpine as builder

WORKDIR /src
COPY requirements.txt /src
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 9090
CMD ["python","-u", "app.py"]
``` 
- File `main.yml:`when executed in an Ansible playbook, will build the "flask_image" Docker image based on the Dockerfile located at ./roles/api/files and create a Docker container named "flask" using that image. The container will have a restart policy of "unless-stopped", port 5000 of the container will be mapped to port 5000 of the host machine for external access, and the container will be connected to the "homework" network
``` text
---
- name: Build flask image
  community.docker.docker_image:
    name: flask_image
    build:
      path: ./roles/api/files
      dockerfile: Dockerfile
    source: build
    force_source: true

- name: Create flask container
  community.docker.docker_container:
    name: flask
    image: flask_image
    restart_policy: "unless-stopped"
    ports:
      - "5000:5000"
    networks:
      - name: homework
``` 
#### Role web
- File `nginx.conf`: Nginx configuration acts as a reverse proxy, forwarding incoming requests to the Flask application running on http://flask:9090. 
``` text
server {
  listen 80;
  server_name localhost;
  
  location / {
    proxy_pass http://flask:9090;
  }
}
```
- `Dockerfile`:this Dockerfile sets up an Nginx container based on the Alpine variant of the Nginx 1.22.0 image, replaces the default Nginx configuration with a custom configuration file, and exposes port 80 within the container.

``` text
FROM nginx:1.22.0-alpine

COPY ./nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

```
- File `main.yml`:when executed in an Ansible playbook, will build the "nginx_image" Docker image based on the Dockerfile located at ./roles/web/templates and create a Docker container named "nginx" using that image. The container will have a restart policy of "unless-stopped", port 80 of the container will be mapped to port 80 of the host machine for external access, and the container will be connected to the "homework" network.
``` text
---
- name: Build nginx image
  community.docker.docker_image:
    name: nginx_image
    build:
      path: ./roles/web/templates
      dockerfile: Dockerfile
    source: build
    force_source: true


- name: Create nginx container
  community.docker.docker_container:
    name: nginx
    image: nginx_image
    restart_policy: "unless-stopped"
    ports:
      - "80:80"
    networks:
      - name: homework
```


## 3. Deployment
Result: 
Run command using secret password
![Command](result/ansible-command.jpg)
This is result
![Result](result/result.jpg)
