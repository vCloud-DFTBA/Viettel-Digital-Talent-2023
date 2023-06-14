# Practice 1: Containerization <!-- omit in toc -->

Author: **Le Minh Duc**

## Table of Contents <!-- omit in toc -->

- [1. Requirements](#1-requirements)
- [2. Comparing Dockerfile instructions](#2-comparing-dockerfile-instructions)
  - [2.1. ARG vs. ENV](#21-arg-vs-env)
  - [2.2. COPY vs. ADD](#22-copy-vs-add)
  - [2.3. CMD vs. ENTRYPOINT](#23-cmd-vs-entrypoint)
- [3. Setting up an application using docker-compose](#3-setting-up-an-application-using-docker-compose)
  - [3.1. Setting up database](#31-setting-up-database)
  - [3.2. Creating Dockerfile for backend](#32-creating-dockerfile-for-backend)
  - [3.3. Creating Dockerfile for frontend](#33-creating-dockerfile-for-frontend)
  - [3.4. Using docker-compose to manage services](#34-using-docker-compose-to-manage-services)
- [4. Conclusion](#4-conclusion)
- [5. References](#5-references)

## 1. Requirements

a. Comparing Dockerfile instructions:

- `ARG` vs. `ENV`
- `COPY` vs. `ADD`
- `CMD` vs. `ENTRYPOINT`

b. Set up a **three-tier** web application that displays the course attendees’ information on the
browser using `docker-compose`.

Base images:

- `nginx:1.22.0-alpine`
- `python:3.9`
- `mongo:5.0`

## 2. Comparing Dockerfile instructions

### 2.1. ARG vs. ENV

- The `ARG` instruction defines a variable that users can pass at build-time to the builder with the `docker build` command using the `--build-arg <varname>=<value>` flag.

  ```dockerfile
  ARG <name>[=<default value>]
  ```

  A default value for `ARG` parameters can be specified in `Dockerfile`, and can be modified during the creation of the build.

- The `ENV` instruction sets the environment variable `<key>` to the value `<value>`. This value will be in the environment for all subsequent instructions in the build stage and can be replaced inline in many as well.

  ```dockerfile
  ENV <key>=<value> ...
  ```

  Like `ARG`, `ENV` values set in a `Dockerfile` can be overridden by providing updated `ENV` values through a `docker-compose.yml` file or Docker CLI.

- Some examples of `ARG` arguments can be a version of Ubuntu, a version of a library, etc.

  ```dockerfile
  ARG UBUNTU_VERSION=latest // Default value provided
  FROM ubuntu:${UBUNTU_VERSION}

  ARG UBUNTU_VERSION // Declare again to use inside build stage
  ARG PYTHON_VERSION=latest // Default value provided

  RUN echo ${UBUNTU_VERSION}
  RUN echo ${PYTHON_VERSION}
  ```

  Here is the result of building the above `Dockerfile` and passing some arguments:

  ```shell
  $ docker build --build-arg UBUNTU_VERSION=20.04 --build-arg PYTHON_VERSION=3.10 .
  ...
  => [1/2] FROM docker.io/library/ubuntu:20.04
  ...
  => [2/3] RUN echo 20.04
  => [3/3] RUN echo 3.10
  ...
  ```

  **Note!** An `ARG` declared before a `FROM` is outside of a build stage, so it can’t be used in any instruction after a `FROM`. To use the default value of an `ARG` declared before the first `FROM` use an `ARG` instruction without a value inside of a build stage.

- **Note!** `ARG` variables are not persisted into the built image as `ENV` variables are, which means the running containers **cannot** access `ARG` values.

- `ENV` variables are usually API keys, database URLs, secret keys, etc.

  ```dockerfile
  FROM mongodb

  ENV CONN_STR=mongodb://user:pass@mongodb
  ...
  ```

- `ARG` variables can also be used to set `ENV` values! :grin:

  ```dockerfile
  FROM ubuntu

  ARG PYTHON_VERSION
  ENV PYTHON_VERSION=${PYTHON_VERSION}
  ...
  ```

### 2.2. COPY vs. ADD

- The `COPY`/`ADD` instruction copies new files, and directories from `<src>` and adds them to the filesystem of the image at the path `<dest>`.

  ```dockerfile
  FROM python

  COPY requirements.txt /tmp/
  RUN pip install --no-cache-dir --requirement /tmp/requirements.txt
  ...
  ```

- Each has two forms. The latter form is required for paths containing whitespace:

  ```dockerfile
  COPY|ADD [--chown=<user>:<group>] [--chmod=<perms>] [--checksum=<checksum>] <src>... <dest>
  COPY|ADD [--chown=<user>:<group>] [--chmod=<perms>] ["<src>",... "<dest>"]
  ```

- Although `COPY` and `ADD` are functionally similar, generally speaking, `COPY` is **preferred**. That’s because it’s more transparent than `ADD`.

- While `COPY` only supports the basic copying of local files into the container, `ADD` has some features like **local-only tar extraction** and **remote URL support** that are not immediately obvious.

- **Note!** The best use for `ADD` is **local tar file auto-extraction** into the image. To fetch packages from remote URLs, use `curl` or `wget` instead so that you can delete the unneeded files later and avoid adding another layer in your image.

### 2.3. CMD vs. ENTRYPOINT

- **Note!** Any Docker image must have an `ENTRYPOINT` or `CMD` declaration for a container to start.

- The `ENTRYPOINT` specifies a command that will **always** be executed when the container starts.

  ```dockerfile
  # Exec form, preferred form
  ENTRYPOINT ["executable", "param1", "param2"]
  # Shell form
  ENTRYPOINT command param1 param2
  ```

- The `CMD` specifies arguments that will be **fed** to the `ENTRYPOINT`. The main purpose of a `CMD` is to **provide defaults** for an executing container.

  ```dockerfile
  # Exec form, preferred form
  CMD ["executable","param1","param2"]
  # Exec form, preferred form, as default parameters to ENTRYPOINT
  CMD ["param1","param2"]
  # Shell form
  CMD command param1 param2
  ```

  You can also override `CMD` when running the container with alternative arguments.

- When the container is run, Docker forms the final execution depending on the values of `ENTRYPOINT` and `CMD`.

  ```dockerfile
  FROM ubuntu

  ENTRYPOINT ["/bin/echo"]
  CMD ["vdt-2023"]
  ```

  The final execution will be `/bin/echo vdt-2023`.

  ```shell
  $ docker run echo-vdt
  vdt-2023
  ```

- The table below shows the final execution for different `ENTRYPOINT`/`CMD` combinations.

  |                                | No ENTRYPOINT              | ENTRYPOINT exec_entry p1_entry | ENTRYPOINT ["exec_entry", "p1_entry"]          |
  |:-------------------------------|:---------------------------|:-------------------------------|:-----------------------------------------------|
  | **No CMD**                     | *error, not allowed*       | **/bin/sh -c** exec_entry p1_entry | exec_entry p1_entry                            |
  | **CMD ["exec_cmd", "p1_cmd"]** | exec_cmd p1_cmd            | **/bin/sh -c** exec_entry p1_entry | exec_entry p1_entry exec_cmd p1_cmd            |
  | **CMD exec_cmd p1_cmd**        | **/bin/sh -c** exec_cmd p1_cmd | **/bin/sh -c** exec_entry p1_entry | exec_entry p1_entry **/bin/sh -c** exec_cmd p1_cmd |

- As can be seen from the table, the *shell* form will **prepend** `bin/sh -c` to the `ENTRYPOINT`/`CMD` when forming the final execution. Moreover, the *shell* form of `ENTRYPOINT` will **ignore** any `CMD` or `docker run` command line arguments.

- **Note!** `CMD [ "echo", "$HOME" ]` will not do variable substitution on `$HOME`. If you want shell processing then either use the *shell* form or execute a shell directly. For example, the *exec* form can be very **flexible**: `CMD [ "sh", "-c", "echo $HOME" ]`.

So what to use? Well, it depends on your use case. As a general rule of thumb:

- Opt for `ENTRYPOINT` instructions when building an **executable** Docker image using commands that **always** need to be executed.
- `CMD` instructions are best for an **additional set of arguments** that act as **default instructions** till there is an explicit command line usage when a Docker container runs.
- If `CMD` is used to provide **default arguments** for the `ENTRYPOINT` instruction, **both** the `CMD` and `ENTRYPOINT` instructions should be specified with the `JSON` array format.

## 3. Setting up an application using docker-compose

### 3.1. Setting up database

- This application uses `MongoDB` for the **Data** tier and makes use of the official `mongo:5.0` image.

- When a container is started for the first time, it will execute files with extensions `.sh` and `.js` that are found in `/docker-entrypoint-initdb.d`. Taking advantage of this, I have created a `init.sh` file with the following content:

  ```sh
  mongoimport --db vdt --collection cloud --ignoreBlanks --type csv --file /docker-entrypoint-initdb.d/attendees.csv --drop --headerline
  ```

- Here, I use `mongoimport` to import the `attendees.csv` file of the same folder as `init.sh` into the `cloud` collection of the `vdt` database.

- I will later use `docker-compose` to mount the `db` folder into the `/docker-entrypoint-initdb.d` folder of the container, so that the `init.sh` file can be executed.

### 3.2. Creating Dockerfile for backend

- The **Logic** tier is written in `Flask`, and I use the official `python:3.9` as the base image.

  ```dockerfile
  FROM python:3.9
  WORKDIR /app
  COPY requirements.txt .
  RUN pip install --no-cache-dir -r requirements.txt
  COPY . .
  EXPOSE 5000
  CMD ["flask", "run", "--host=0.0.0.0"]
  ```

- Here, I first copy the `requirements.txt` file to the working directory and install the dependencies before copying the rest of the files. Doing this results in **fewer cache invalidations** for the `RUN` step, than if I `COPY` all the files at once.

- The `--no-cache-dir` option tells `pip` to not save the downloaded packages locally, therefore reducing the image size significantly if the `requirements.txt` file is large.

### 3.3. Creating Dockerfile for frontend

- The **Presentation** tier is written in `React`, and I use the official `node:18` as the base image.

  ```dockerfile
  FROM node:18 AS build
  WORKDIR /app
  COPY ./package* .
  RUN npm install
  COPY . .
  RUN npm run build

  FROM nginx:1.22.0-alpine
  COPY ./nginx/nginx.conf /etc/nginx/nginx.conf
  COPY --from=build /app/dist /usr/share/nginx/html
  EXPOSE 80
  CMD ["nginx", "-g", "daemon off;"]
  ```

- Using the same strategy as the backend, I first copy the `package.json` and `package-lock.json` files to the working directory and install the dependencies before copying the rest of the files.

- When building `React` applications, we need a `Node` environment to compile the `JS` code (typically `JSX`), and more into static `HTML`, `JS`, and `CSS`.

- However, we don't need the `Node` environment for our production build. Thats why I will only ship the static resources in a static `nginx` container. Here, I have applied multi-stage builds to create the final shippable image:

  ```dockerfile
  COPY ./nginx/nginx.conf /etc/nginx/nginx.conf
  COPY --from=build /app/dist /usr/share/nginx/html
  ```

- Only the previously built static resources are copied to the `nginx` image. And here is the config to serve the static resources:

  ```nginx
  server {
    listen 80;
    server_name  localhost;

    root   /usr/share/nginx/html;
    index  index.html index.htm;
    include /etc/nginx/mime.types;

    gzip on;
    gzip_min_length 1000;
    gzip_proxied expired no-cache no-store private auth;
    gzip_types text/plain text/css application/json application/javascript application/x-javascript text/xml application/xml application/xml+rss text/javascript;

    location / {
      try_files $uri $uri/ /index.html;
    }
  }
  ```

### 3.4. Using docker-compose to manage services

- I have to admit creating a `docker-compose.yml` file is not an easy task. I have to look up a lot and come up with the following:

  ```dockerfile
  services:
    backend:
      build:
        context: ./backend
      depends_on:
        - db
      networks:
        - react-flask
        - flask-mongo
      ports:
        - 5000:5000

    db:
      image: mongo:5.0
      volumes:
        - ./db:/docker-entrypoint-initdb.d
      networks:
        - flask-mongo
      ports:
        - 27017:27017

    frontend:
      build:
        context: ./frontend
      depends_on:
        - backend
      networks:
        - react-flask
      ports:
        - 80:80

  networks:
    react-flask:
    flask-mongo:
  ```

- Here, I create 3 services: `backend`, `db`, and `frontend`.

- Containers in the same network can communicate with each other using their service name as the hostname. For example, the `backend` service can connect to the `db` service using the hostname `db`.

  ```python
  client = MongoClient("db:27017")
  ```

- However, the static resources in the `frontend` service are served by the `nginx` server, which is not aware of the `backend` service when on the client side. Therefore, I have to set up a reverse proxy to redirect requests to the `backend` service.

  ![image](assets/nginx-reverse-proxy.png)
  *Redirect requests to the backend using Nginx*

  ```nginx
  upstream backend {
    server backend:5000;
  }

  server {
    ...

    location /api {
      rewrite /api/(.*) /$1 break;
      proxy_pass http://backend;
    }
  ```

- Here, I also add the location `/api`. So
`api/anything` should redirect to the parameter `/$1`, which is any section of our `Flask` routes such as `/cloud`.

## 4. Conclusion

![image](assets/docker-images.png)
*Sizes of built images vs base images*

- As can be seen from the images, after building and shipping only the static resources, the `frontend` image is approximately of the same size as the base `nginx` image.

- The `backend` image is also quite small, thanks to the `--no-cache-dir` option. The size difference (16MB) is due to the additional `Flask`, `Flask-CORS` and `pymongo` dependencies, which may require their own dependencies during installation.

Here is the final result after using `docker-compose up`. The application runs on `localhost:80`:

![images](assets/docker-compose.png)
*The application built successfully on localhost:80*

During my research, I have stumped across many practices but didn't have the chance to apply them. Therefore, I will list some of them here for future referencing:

- Separate `Dockerfile`s for development and production.
- Use `check_health` for containers and then `depend_on` these health checks.
- Set up environment variables for containers.

After this practice, I have grown to appreciate `Docker` a lot more. It is such a powerful tool that can be used to ship applications in a consistent manner and I cannot wait to apply it to my future projects.

## 5. References

[1] [Dockerfile Reference](https://docs.docker.com/engine/reference/builder/)

[2] [How to Use Docker Build Args and Environment Variables](https://refine.dev/blog/docker-build-args-and-env-vars/)

[3] [What Is the Difference Between CMD and ENTRYPOINT in a Dockerfile?](https://stackoverflow.com/questions/21553353/what-is-the-difference-between-cmd-and-entrypoint-in-a-dockerfile)

[4] [DevOps Blog Docker CMD vs ENTRYPOINT: What’s the Difference & How to Choose](https://www.bmc.com/blogs/docker-cmd-vs-entrypoint/)

[5] [Best Practices for Writing Dockerfiles](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)

[6] [Image-building Best Practices](https://docs.docker.com/get-started/09_image_best/)

[7] [Sample Nginx Config for Vite React](https://github.com/daniellaera/react-vite-docker-fly/blob/main/nginx/nginx.conf)

[8] [Build and Dockerize a React App with Node.js, MySQL and Nginx](https://www.section.io/engineering-education/build-and-dockerize-a-full-stack-react-app-with-nodejs-and-nginx/)

[9] [How to Seed Data into Mongo with Docker](https://time-is-life.fun/how-to-seed-data-into-mongo-with-docker/)
