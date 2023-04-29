# Containerization

## _Set up a three-tier web application that displays the course attendees’ information on the browser using docker-compose._

---

# **Table of Contents:**

## [I. What is Docker ?](#WhatIsDocker)

-   ### [1. Containerization](#Containerization)
-   ### [2. Docker](#Docker)
-   ### [3. Docker-compose](#DockerCompose)
-   ### [4. ARV and ENV](#AnE)
-   ### [5. COPY and ADD](#CnA)
-   ### [6. CMD and ENTRYPOINT](#CnE)
-   ### [7. How many optimization tricks used in this Dockerfile?](#Question)

## [II. Setting up our three-tier web application](#ThreeTier)

-   ### [1. Install docker and docker-compose](#InstallDocker)
-   ### [2. Build image for frontend by Dockerfile](#FE)
-   ### [3. Build image for backend by Dockerfile](#BE)
-   ### [4. Nginx config](#Nginx)
-   ### [5. Docker-compose](#DCom)
-   ### [6. Running Container](#RC)
-   ### [7. Result](#Result)

## [III. References](#Re)

---

<a name="WhatIsDocker"></a>

# **I. What is Docker ?**:

<img src= images/docker.png>

<a name="Containerization"></a>

### 1. Containerization

-   Containerization is a next-generation virtualization and automation solution after Hypervisor Virtualization, widely applied by leading technology companies such as Google, Facebook, and Amazon, bringing breakthrough efficiency with outstanding advantages that excel in deployment speed, scalability, security, and user experience.

<a name="Docker"></a>

### 2. Docker

-   Docker is a platform to provide an easier way to build, deploy, and run applications using containers (on virtualization platforms). Originally written in Python, now switched to Golang.
-   Difference between Docker container and Virtual Machine

| Docker                                                            | Virtual Machine                                                                                        |
| ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| Lighter weight (think in terms of MB)                             | Much larger (think in terms of GB).                                                                    |
| Limited performance                                               | Native performance                                                                                     |
| The container will use the host's operating system                | Each virtual machine will have its operating system                                                    |
| Virtualizes the operating system                                  | Virtualizes the underlying physical infrastructure                                                     |
| Boot time in milliseconds                                         | Boot time in minutes                                                                                   |
| Requires less memory space                                        | Allocate memory as needed                                                                              |
| Process level isolation, possibly less secure                     | Completely isolated and safer                                                                          |
| Highly scalable. Granular scalability possible with microservices | Scaling can be costly. Requires switching from on-premises to cloud instances for cost-effective scale |

### _Some Concepts in Docker_

-   _Dockerfile_

Dockerfile is a text file with no extension, containing specifications for a software executable field, and structure for Docker Image. From those commands, Docker will build a Docker image (usually from a few MB to a few GB large).

> The general syntax of a Dockerfile is of the form:

```
   INSTRUCTION arguments
```

`INSTRUCTION` is the name of the instructions contained in the Dockerfile, each of which performs a certain task, specified by Docker. When declaring these directives must be written in capital letters.
A Dockerfile must start with the FROM directive to declare which image will be used as the base to build your image. arguments is the body of the directives, which decides what the directive will do.

-   _Docker image_

A Docker image is an immutable - immutable file that contains the source code, libraries, dependencies, tools, and other files needed for an application to run.

-   _Docker container_

A Docker container is a run-time environment in which a user can run a standalone application. These containers are very lightweight and allow you to run applications in them very quickly and easily.

-   _FROM_

        The FROM directive is required and must be placed at the top of the Dockerfile.

        Syntax:
        `	 FROM <image> [AS <name>]

    FROM <image>[:<tag>] [AS <name>]
    FROM <image>[@<digest>] [AS <name>]
    `

-   _EXPOSE_

Set the port on which the container listens, allow other containers on the same network to communicate through this port, or map the host port to this port.

-   _WORKDIR_

Set the working directory in the container for the COPY, ADD, RUN, CMD, and ENTRYPOINT commands.

<a name="DockerCompose"></a>

### 3. Docker-compose

<img src= images/docker-compose.png>

-   Docker Compose is a tool for defining and running Docker programs that use multi-containers.

-   Benefits of using Compose:

-   **Create multiple isolated environments in one host:** Compose isolates projects' environments to ensure they don't conflict with each other, and makes it easy to make copies of an environment.

-   **Recreate only changed containers:** Compose will recognize the services that have not changed and reuse the containers corresponding to that service.

-   **Adjust usage variables for environments:** Compose uses variables in the Compose file for environments. So with different environments or users, it is possible to adjust variables when using Compose to set up services.

<a name="AnE"></a>

### 4. ARV and ENV

-   `ARG` is also known as the `build-time` variable (only works during build images). They are only available from the time they are 'published' in the `Dockerfile` in the `ARG` statement until the image is created.

-   `ENV` variables are also available during build, as soon as you declare them with a command of `ENV`. However, unlike `ARG`, when `image` is built, containers running the image can access this `ENV` value. Containers running from the image can override the value of `ENV`.
    > Syntax:

```
ENV <key>=<value>
```

<a name="CnA"></a>

### 5. COPY and ADD

-   The `ADD` directive will copy files and directories from the machine under construction or remote file URLs from src and add them to the filesystem of the dest image.
    > Syntax:

```
ADD [--chown=<user>:<group>] <src>... <dest>
ADD [--chown=<user>:<group>] ["<src>",... "<dest>"]
```

In there:

-   `src` can declare multiple files, directories, ...
-   `dest` must be an absolute path or have a directive relationship to `WORKDIR`.

*   The `COPY` directive is similar to `ADD` as _copy files_, directories from `src` and add them to the `dest` of the container. Unlike `ADD`, it does not support adding remote file URLs from sources on the network.
    > Syntax:

```
COPY [--chown=<user>:<group>] <src>... <dest>
COPY [--chown=<user>:<group>] ["<src>",... "<dest>"]
```

<a name="CnE"></a>

### 6. CMD and ENTRYPOINT

-   `CMD` executes the default command when we initialize the container from the image, this default command can be overridden from the command line when initializing the container.
-   `CMD` allows us to set a default command, which means that this command will only be run when running the container without specifying a command.
-   If docker runs with a command then the default command will be ignored. If the dockerfile has more than one CMD command, all will be ignored except for the last CMD command.
    > Syntax:

```
CMD ["executable", "param1", "param2"]   (exec form)
CMD ["param1", "param2"]  (set default parameters for ENTRYPOINT in exec form)
CMD command param1 param2   (shell form)
```

-   `ENTRYPOINT` is quite similar to `CMD` which are both used when initializing the container, but `ENTRYPOINT` cannot be overridden from the command line when initializing the container.
-   The `ENTRYPOINT` command allows you to configure the container to run as executable. It is similar to CMD, as it also allows us to specify a command with parameters. The difference is that the `ENTRYPOINT` command and parameters are not ignored when the Docker container runs.
    > Syntax:

```
- ENTRYPOINT ["executable", "param1", "param2"] (exec form)
- ENTRYPOINT command param1 param2 (shell form)
```

<a name="Question"></a>

### 7. How many optimization tricks used in this Dockerfile?

```
FROM alpine:3.5

# Install python and pip
RUN apk add --update py2-pip

# upgrade pip
RUN pip install --upgrade pip

# install Python modules needed by the Python app
COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

# copy files required for the app to run
COPY app.py /usr/src/app/
COPY templates/index.html /usr/src/app/templates/

# tell the port number the container should expose
EXPOSE 5000

# run the application
CMD ["python", "/usr/src/app/app.py"]
```

There are several optimization tricks used in this Dockerfile:

-   Using a lightweight base image: The Dockerfile starts with FROM alpine:3.5, which is a lightweight Linux distribution that is optimized for running containers.

-   Caching dependencies: The requirements.txt file is copied to the Docker image before installing dependencies. This allows Docker to cache the dependencies and avoid re-installing them if the requirements.txt file hasn't changed.

-   Using --no-cache-dir: The pip install command includes the --no-cache-dir flag, which disables the pip cache. This saves disk space and reduces the size of the Docker image.

To further optimize this Dockerfile, we could combine the RUN commands into a single command:

```
FROM alpine:3.5

# Install python and pip
RUN apk add --update py2-pip

# copy files required for the app to run
COPY requirements.txt /usr/src/app/
COPY app.py /usr/src/app/
COPY templates/index.html /usr/src/app/templates/

# upgrade pip & install Python modules needed by the Python app
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r /usr/src/app/requirements.txt

# tell the port number the container should expose
EXPOSE 5000

# run the application
CMD ["python", "/usr/src/app/app.py"]
```

<a name="ThreeTier"></a>

# **II. Setting up our three-tier web application**:

<a name="InstallDocker"></a>

### 1. Install docker and docker-compose

-   Install docker

```
sudo apt install docker
```

-   Install docker-compose

```
sudo apt install docker-compose
```

<a name="FE"></a>

### 2. Build image for frontend by Dockerfile

-   Dockerfile

```
FROM node:18.2.0-alpine
WORKDIR /app
COPY . /app
RUN npm install
EXPOSE 3000
CMD ["npm", "start"]
```

First, select the base image for the Docker image, in this case node:18.2.0-alpine, which is a lightweight version of Node.js 18.2.0 running on Alpine Linux.

```
FROM node:18.2.0-alpine
```

Set the working directory for subsequent commands in the Dockerfile to /app.

```
WORKDIR /app
```

Copy the contents of the current directory (.) into the /app directory of the Docker image.

```
COPY . /app
```

Run the npm install command inside the Docker image, which installs the dependencies specified in the package.json file of the application.

```
RUN npm install
```

This exposes port 3000 on the Docker container to the outside world.

```
EXPOSE 3000
```

Set the default command to run when the Docker container is started to npm start, which starts the application.

```
CMD ["npm", "start"]

```

<a name="BE"></a>

### 3. Build image for backend by Dockerfile

-   Dockerfile

```
FROM python:3.9
WORKDIR /code
COPY . /code
RUN pip install --no-cache-dir --upgrade -r requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
```

First, select the base image for the Docker image, in this case python:3.9.

```
FROM python:3.9
```

Set the working directory for subsequent commands in the Dockerfile to /code.

```
WORKDIR /code
```

Copy the contents of the current directory (.) into the /code directory of the Docker image.

```
COPY . /code
```

This runs the pip install command to install the dependencies specified in the requirements.txt file of the application. The --no-cache-dir option is used to avoid caching the downloaded packages in the Docker image's layers.

```
RUN pip install --no-cache-dir --upgrade -r requirements.txt
```

Set the default command to run when the Docker container is started to uvicorn main:app --host 0.0.0.0 --port 80, which starts the application using the Uvicorn ASGI server on port 80. The main:app argument specifies the Python module and application instance to run.

```
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
```

<a name="Nginx"></a>

### 4. Nginx config

-   config.conf

```
server {
    listen 8888;
    location / {
        proxy_pass http://react:3000/;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

This Nginx configuration file defines a server block that listens on port 8888 and proxies requests to a backend server running on port 3000.
listen 8888; : This specifies that Nginx should listen on port 8888 for incoming connections.
proxy_pass http://react:3000/; : This tells Nginx to proxy requests to http://react:3000/, which is the backend server that will handle the requests. The trailing / after 3000 specifies that Nginx should pass the URI path from the original request to the backend server.

<a name="DCom"></a>

### 5. Docker-compose

-   docker-compose.yml

```
version: '3.9'

services:
  react:
    build: frontend
    container_name: presentation_tier
    hostname: react
    restart: unless-stopped
    ports:
      - "3000:3000"
    links:
      - fastapi

  fastapi:
    build: backend
    container_name: logic_tier
    restart: unless-stopped
    ports:
      - "80:80"
    depends_on:
      - mongodb

  mongodb:
    image: mongo:5.0
    container_name: data_tier
    restart: unless-stopped
    hostname: mongodb
    environment:
      - MONGO_INITDB_DATABASE=vdt2023
    ports:
      - "27017:27017"

  nginx:
    image: nginx:1.22.0-alpine
    container_name: nginx
    restart: unless-stopped
    volumes:
      - ./nginx/config.conf:/etc/nginx/conf.d/default.conf
    ports:
      - "8888:8888"
    links:
      - react
```

<a name="RC"></a>

### 6. Running Container

-   Build docker-compose

```
docker-compose build
```

-   Run the containers in the background

```
docker-compose up -d
```

<img src= images/up.png>

-   Check running containers

```
docker ps
```

<img src= images/containers.png>

-   Check images created

```
docker images
```

<img src= images/images.png>

<a name="Result"></a>

### 7. Result

> http://localhost:8888/

<img src= images/localhost.png>

<a name="Re"></a>

# **III. References**:

-   [What Is Containerization?](https://aws.amazon.com/what-is/containerization/#:~:text=Containerization%20is%20a%20software%20deployment,matched%20your%20machine's%20operating%20system.)
-   [What's The Difference Between Containers And Virtual Machines?](https://aws.amazon.com/compare/the-difference-between-containers-and-virtual-machines/#:~:text=A%20container%20is%20a%20software,copy%20of%20a%20physical%20machine.)
-   [Dockerfile reference](https://docs.docker.com/engine/reference/builder/)
