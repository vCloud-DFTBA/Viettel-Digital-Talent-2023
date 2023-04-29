## Build and Deploy a 3-Tier Web Application using Docker
### Table of Contents
  - [1. What is Container?](#1-what-is-container)
  - [2. What is Docker?](#2-what-is-docker)
  - [3. Docker Architecture](#3-docker-architecture)
  - [4. What is Docker Compose?](#4-what-is-docker-compose)
  - [5. What is Docker Swarm?](#5-what-is-docker-swarm)
  - [6. Homework Questions](#6-homework-questions)
  - [7. Layer Caching](#7-layer-caching)
  - [8. 3-tier Web Application](#8-3-tier-web-application)
  - [9. Deploy Documentations](#9-deploy-documentations)
  - [10. Application Demo](#10-application-demo)
  - [11. References](#11-references)
### Introduction to Docker

### **1. What is Container?**

A container is an isolated environment for your code. This means that a container has no knowledge of your operating system, or your files. It runs on the environment provided to you by Docker Desktop. This is why a container usually has everything that your code needs in order to run, down to a base operating system. You can use Docker Desktop to manage and explore your containers.

### **2. What is Docker?**

<div align="center">
  <img src="./asserts/docker.png" width="210" height="200" />
</div>


Docker is a containerization platform that packages your application and all its dependencies together in the form of containers so as to ensure that your application works seamlessly in any environment be it development or test or production. Docker containers, wrap a piece of software in a complete filesystem that contains everything needed to run: code, runtime, system tools, system libraries etc. anything that can be installed on a server. This guarantees that the software will always run the same, regardless of its environment.
  - **Docker Engine** is the open source containerization technology that powers Docker. Docker Engine is a client-server application with these major components:
    - A server which is a type of long-running program called a daemon process (the dockerd command).
    - A REST API which specifies interfaces that programs can use to talk to the daemon and instruct it what to do.
    - A command line interface (CLI) client (the docker command).
  - [**Docker Hub**](https://hub.docker.com/) is a cloud-based registry service which stores Docker images. Docker Hub offers both free and paid accounts. You can use Docker Hub to store and distribute your images. You can also use Docker Hub to create automated builds, which build an image whenever you push new code to a GitHub or Bitbucket repository.
  - **Docker Images** are the building blocks of Docker. An image is a read-only template with instructions for creating a Docker container. Images are used to create containers. Docker provides a simple way to build new images or update existing images, or you can download and use images that other people have already created.
  - [**Dockerfile**](https://docs.docker.com/engine/reference/builder/) is a text document that contains all the commands a user could call on the command line to assemble an image. Using `docker build` users can create an automated build that executes several command-line instructions in succession.
  - **Docker Registry** is a storage and content delivery system, holding named Docker images, available in different tagged versions. The registry is a stateless, highly scalable server side application that stores and lets you distribute Docker images. The registry is open-source, under the permissive Apache license. You can freely install your own instance and store your images on it, for free. You can also use a commercial Docker registry service, such as Docker Hub, Quay.io, or Google Container Registry.

### **3. Docker Architecture**

<div align="center">
  <img src="./asserts/architecture.svg" width="800"/>
</div>

Docker uses a client-server architecture. The Docker client talks to the Docker daemon, which does the heavy lifting of building, running, and distributing your Docker containers. The Docker client and daemon can run on the same system, or you can connect a Docker client to a remote Docker daemon. The Docker client and daemon communicate using a REST API, over UNIX sockets or a network interface.

  - **Docker Daemon** (`dockerd`) is a persistent process that manages Docker containers on the host system. The daemon is the process that runs in the operating system to which clients talk to.
  - **Docker Client** is the primary way that many Docker users interact with Docker. When you use commands such as `docker run`, the client sends these commands to `dockerd`, which carries them out. The docker command uses the Docker API. The Docker client can communicate with more than one daemon.
  - **Docker Registries** is a place where you can store and distribute Docker images. The default registry is Docker Hub. You can even run your own private registry. If you use Docker Datacenter (DDC), it includes Docker Trusted Registry (DTR).

### **4. What is Docker Compose?**

[Docker Compose](https://docs.docker.com/compose/) is a tool for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application’s services. Then, with a single command, you create and start all the services from your configuration. To learn more about the Compose file, see the Compose file reference.

### **5. What is Docker Swarm?**

[Docker Swarm](https://docs.docker.com/engine/swarm/) is a native clustering tool for Docker. It turns a pool of Docker hosts into a single, virtual Docker host. Because Docker Swarm serves the standard Docker API, any tool that already communicates with a Docker daemon can use Swarm to transparently scale to multiple hosts: Compose, Swarm mode, Kubernetes, and any other tool that already uses Docker can use Swarm to scale to multiple hosts. Docker Swarm is natively integrated into Docker Engine, so you can use it with any Docker application.

### **6. Homework Questions**
    
What are the differences between these instructions?

`ARG` vs. `ENV`
  - `ARG` is used to pass the build-time variables to the Dockerfile.
    ``` Dockerfile 
    ARG <name>[=<default value>]
    ```

  - `ENV` is used to set the environment variables inside the container.
    ``` Dockerfile
    ENV <key> <value>
    ```

`COPY` vs. `ADD`
  - `COPY` is used to copy the files from the host machine to the container.
    ``` Dockerfile
    COPY <src>... <dest>
    ```
  - `ADD` is used to copy the files from the host machine to the container and also used to download the files from the URL and copy it to the container.
    ``` Dockerfile
    ADD <src>... <dest>
    ```
`CMD` vs. `ENTRYPOINT`
  - `CMD` The main purpose is to provide defaults for an executing container. These defaults can include an executable, or they can omit the executable, in which case you must specify an `ENTRYPOINT` instruction as well
    ``` Dockerfile
    CMD ["executable","param1","param2"] # exec form
    CMD command param1 param2 # shell form
    CMD ["param1","param2"] # as default parameters to ENTRYPOINT
    ```
  - `ENTRYPOINT` The main purpose is to configure a container that will run as an executable. The `ENTRYPOINT` instruction allows you to configure a container that will run as an executable. This is different from the `CMD` instruction, which specifies default arguments for the `ENTRYPOINT` instruction or for an executable that you specify in the `CMD` instruction.
    ``` Dockerfile
    ENTRYPOINT ["executable", "param1", "param2"] # exec form
    ENTRYPOINT command param1 param2 # shell form
    ```

**How many way to optimize Dockerfile?**
  ``` Dockerfile
  # 1. Use multi-stage builds
  FROM golang:1.16.5-alpine3.14 AS builder
  WORKDIR /app
  COPY . .
  RUN go build -o main .

  FROM alpine:3.14
  WORKDIR /app
  COPY --from=builder /app/main .
  CMD ["./main"]
  ```
  ``` Dockerfile
  # 2. Use .dockerignore
  .git
  .vscode
  .idea
  .env
  .DS_Store
  node_modules
  npm-debug.log
  ...
  ```
  ``` Dockerfile
  # 4. Minimal base image
  FROM alpine:3.14
  ```
  ``` Dockerfile
  # 5. Use COPY instead of ADD
  COPY . .
  ```
  - Use the COPY instruction over the ADD instruction: The COPY instruction is faster and less powerful than the ADD instruction.
  ``` Dockerfile
  # 6. Minimize the number of layers
  RUN apt-get update && apt-get install -y \
      aufs-tools \
      automake \
      build-essential \
      curl \
      dpkg-sig \
      libcap-dev \
      libsqlite3-dev \
      mercurial \
      reprepro \
      ruby1.9.1 \
      ruby1.9.1-dev \
      s3cmd=1.1.* \
      && rm -rf /var/lib/apt/lists/*
  ```

### **7. Layer caching**

Docker uses a caching mechanism to save time when building images. When you build an image, Docker creates a series of layers that represent the instructions in the Dockerfile. Each layer is only recreated if the instructions that created it have changed. This means that if you change the `RUN` command in your Dockerfile, all subsequent layers after that command are recreated. However, if you change the `COPY` command, all subsequent layers after that command are recreated. This is because the `COPY` command affects the filesystem, which is represented by the layers that follow it.

### **8. 3-tier Web Application**
<div align="center">
  <img src="./asserts/app.jpg" width="800"/>
</div>

**More details:**
- Onpremise Server:
  - [Ubuntu 22.04.2 LTS](https://ubuntu.com/download/server): Ubuntu is an open source software operating system that runs from the desktop, to the cloud, to all your internet connected things.
  - [Docker Standalone](https://docs.docker.com/engine/install/ubuntu/): Docker is a set of platform as a service (PaaS) products that use OS-level virtualization to deliver software in packages called containers.
  - 4 Core CPU, 4GB RAM, 20GB SSD, 500GB HDD
- Frontend:
  - [ReactJS](https://react.dev/): A JavaScript library for building user interfaces
  - [Material-UI](https://material-ui.com/): React components for faster and easier web development. Build your own design system, or start with Material Design.
  - [NodeJS](https://nodejs.org/en/): Node.js® is a JavaScript runtime built on Chrome's V8 JavaScript engine.
  - [Nginx](https://www.nginx.com/): Nginx is a web server that can also be used as a reverse proxy, load balancer, mail proxy and HTTP cache.
- Backend:
  - [Flask](https://flask.palletsprojects.com/en/1.1.x/): Flask is a lightweight WSGI web application framework.
  - [Python3.9](https://www.python.org/downloads/): Python is an interpreted, high-level and general-purpose programming language.
- Database:
  - [MongoDB](https://www.mongodb.com/): MongoDB is a general purpose, document-based, distributed database built for modern application developers and for the cloud era.
- Reverse Proxy:
  - [Traefik](https://doc.traefik.io/traefik/): Traefik is a modern HTTP reverse proxy and load balancer made to deploy microservices with ease.
- Monitoring:
  - [Prometheus](https://prometheus.io/): Prometheus is an open-source systems monitoring and alerting toolkit originally built at SoundCloud.
  - [Grafana](https://grafana.com/): Grafana is the open platform for beautiful analytics and monitoring.
  - [MongoDB Exporter](https://hub.docker.com/r/bitnami/mongodb-exporter/): MongoDB Exporter is a Prometheus exporter for MongoDB metrics.
  - [Node Exporter](https://hub.docker.com/r/prom/node-exporter/): Node Exporter is a Prometheus exporter for hardware and OS metrics exposed by *NIX kernels, written in Go with pluggable metric collectors.
  - [cAdvisor](https://hub.docker.com/r/google/cadvisor/): cAdvisor (Container Advisor) provides container users an understanding of the resource usage and performance characteristics of their running containers.
- Domain:
  - My free domain: [hoangndst.freeddns.org](http://hoangndst.freeddns.org/) point to `Traefik`.

### **9. Deploy Documentations**

**Project Architecture:**
  ``` bash
  NguyenDinhHoang
  ├── asserts
  ├── backend
  │   ├── Dockerfile
  │   ├── .dockerignore
  │   ├── .gitignore
  │   ├── requirements.txt
  │   ├── config.py
  │   ├── app
  ├── frontend
  │   ├── Dockerfile
  │   ├── .dockerignore
  │   ├── .gitignore
  │   ├── .env
  │   ├── package.json
  │   ├── package-lock.json
  │   ├── public
  │   ├── src
  ├── docker-compose.yaml
  ├── docker-compose-local.yaml
  ├── README.md
  ```



**Understand `Dockerfile`**:

- **[Frontend Dockerfile](./frontend/Dockerfile)**:
  - Using multi-stage build to reduce the image size.
  - Using `nginx` as the web server.
    ``` Dockerfile
    FROM node:18.16.0-alpine3.17 AS build
    ```
    This means that the first stage of the build is named `build` and is based on the `node:18.16.0-alpine3.17` image.
    ``` Dockerfile
    WORKDIR /app
    ```
    This means that all subsequent commands will be run from the `/app` directory.
    ``` Dockerfile
    COPY package*.json ./
    RUN npm install
    ```
    This means that the `package.json` and `package-lock.json` files are copied from the host machine to the container and the `npm install` command is run to install the dependencies.
    ``` Dockerfile
    COPY . .
    RUN npm run build
    ```
    This means that the rest of the files are copied from the host machine to the container and the `npm run build` command is run to build the application. [`.dockerignore`](./frontend/.dockerignore) file is used to exclude files and directories from the build context.
    ``` Dockerfile
    COPY --from=build /app/build /usr/share/nginx/html
    ```
    This means that the `build` stage is used to build the application and the output is copied to the `/usr/share/nginx/html` directory in the `nginx` image.
    ``` Dockerfile
    COPY nginx.conf /etc/nginx/conf.d/default.conf
    EXPOSE 80
    ```
    This means that the [`nginx.conf`](./frontend/nginx.conf) file is copied to the `/etc/nginx/conf.d/default.conf` directory in the `nginx` image and port `80` is exposed.
    ``` Dockerfile
    CMD ["nginx", "-g", "daemon off;"]
    ```
    This means that the `nginx` command is run when the container starts.
- [**Backend Dockerfile**](./backend/Dockerfile)
  ``` Dockerfile
  FROM python:3.9
  WORKDIR /app
  COPY . .
  RUN pip3 install -r requirements.txt
  CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
  ```

**Config own variables in docker-compose file**:
- **Database Mongo**:
  ``` yaml
  mongo:
    ...
    environment:
      MONGO_INITDB_ROOT_USERNAME: hoangndst
      MONGO_INITDB_ROOT_PASSWORD: Hoang2002
    ...
  ```
  You can change `MONGO_INITDB_ROOT_USERNAME` and `MONGO_INITDB_ROOT_PASSWORD` to your own username and password.
- **Backend**
  ``` yaml
  backend:
    ...
    environment:
      - MONGO_HOST=mongo
      - MONGO_PORT=27017
      - MONGO_USERNAME=hoangndst
      - MONGO_PASSWORD=Hoang2002
    ...
  ```
  You can change `MONGO_HOST`, `MONGO_PORT`, `MONGO_USERNAME` and `MONGO_PASSWORD` to your own variables to connect to your database.
- **MongoDB Exporter**
  ``` yaml
  mongodb-exporter:
    ...
    environment:
      - MONGODB_URI=mongodb://hoangndst:Hoang2002@mongo:27017
    ...
  ```
  You can change `MONGODB_URI` to your own variables to connect to your database.

**Deploy on local machine:**
  - Change `REACT_APP_BACKEND_URL` in [`frontend/.env`](./frontend/.env) to your backend url `http://localhost:5000`.
    ``` bash
    REACT_APP_BACKEND_URL=http://localhost:5000
    ```
  - If you run on your local machine, use file [`docker-compose-local.yaml`](./docker-compose-local.yaml).
    ``` bash
    docker compose -f docker-compose-local.yaml up -d
    ```
    Image will be built and run on your local machine.
  - All ports are exposed to the host machine, so you can access the application via `http://localhost:3000`

**Deploy on server:**
  - You have a domain point to your `Traefik`.
  - Change `REACT_APP_BACKEND_URL` in [`frontend/.env`](./frontend/.env) to your backend url.
  In my case:
    ``` bash
    REACT_APP_BACKEND_URL=https://vdt-backend.hoangndst.freeddns.org
    ```
  - Make `Traefik` routes your app with labels, this depends on how you configure your `Traefik`.
  
    In my case:
    ``` yaml
    frontend:
      ...
      labels:
      - "traefik.enable=true"
      - "traefik.http.routers.vdt-frontend.entrypoints=websecure"
      - "traefik.http.routers.vdt-frontend.rule=Host(`vdt-frontend.hoangndst.freeddns.org`)"
      - "traefik.http.routers.vdt-frontend.service=vdt-frontend"
      - "traefik.http.services.vdt-frontend.loadbalancer.server.port=80"
      - "traefik.docker.network=traefik_default"
      - "traefik.http.routers.vdt-frontend.tls=true"
      - "traefik.http.routers.vdt-frontend.tls.certresolver=production"
      ...
    backend:
      ...
      labels:
      - "traefik.enable=true"
      - "traefik.http.routers.vdt-backend.entrypoints=websecure"
      - "traefik.http.routers.vdt-backend.rule=Host(`vdt-backend.hoangndst.freeddns.org`)"
      - "traefik.http.routers.vdt-backend.service=vdt-backend"
      - "traefik.http.services.vdt-backend.loadbalancer.server.port=5000"
      - "traefik.docker.network=traefik_default"
      - "traefik.http.routers.vdt-backend.tls=true"
      - "traefik.http.routers.vdt-backend.tls.certresolver=production"
      ...
    ```
  - Ports is no need to expose to the host machine, so you can access the application via [`https://vdt-frontend.hoangndst.freeddns.org`](https://vdt-frontend.hoangndst.freeddns.org).
  - If you run on your server, use file [`docker-compose.yaml`](./docker-compose.yaml)
    ``` bash
    docker compose -f docker-compose.yaml up -d
    ```
    Image will be automatically built and run on your server.

**Preview Deployment**:
  <div align="center">
    <img src="./asserts/deploy.png" width="800"/>
  </div>

### **10. Application Demo**
- Access [`https://vdt-frontend.hoangndst.freeddns.org`](https://vdt-frontend.hoangndst.freeddns.org) to see the application demo.
- Access [`https://grafana.hoangndst.freeddns.org/`](https://grafana.hoangndst.freeddns.org/) to see the Monitoring Dashboard.
  - Username: `admin`
  - Password: `Hoang2002`

**Frontend**:
  <div align="center">
    <img src="./asserts/demo1.png" width="800"/>
  </div>

**Backend**:  
  <div align="center">
    <img src="./asserts/demo2.png" width="800"/>
  </div>


### **11. References**
- [Docker Documentation](https://docs.docker.com/)
- [Flask Documentation](https://flask.palletsprojects.com/en/latest/)
- [React Documentation](https://react.dev/)
- [Traefik Documentation](https://doc.traefik.io/traefik/)
- [Prometheus Documentation](https://prometheus.io/docs/introduction/overview/)
- [Grafana Documentation](https://grafana.com/docs/grafana/latest/)
- [MongoDB Documentation](https://docs.mongodb.com/)