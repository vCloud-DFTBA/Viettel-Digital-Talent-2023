## Build and Deploy a 3-Tier Web Application using Docker
### Table of Contents


### Introduction to Docker

**1. What is Container?**

A container is an isolated environment for your code. This means that a container has no knowledge of your operating system, or your files. It runs on the environment provided to you by Docker Desktop. This is why a container usually has everything that your code needs in order to run, down to a base operating system. You can use Docker Desktop to manage and explore your containers.

**2. What is Docker?**

<div style="text-align:center">
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

**3. Docker Architecture**

<div style="text-align:center">
  <img src="./asserts/architecture.svg" width="600"/>
</div>

Docker uses a client-server architecture. The Docker client talks to the Docker daemon, which does the heavy lifting of building, running, and distributing your Docker containers. The Docker client and daemon can run on the same system, or you can connect a Docker client to a remote Docker daemon. The Docker client and daemon communicate using a REST API, over UNIX sockets or a network interface.

  - **Docker Daemon** (`dockerd`) is a persistent process that manages Docker containers on the host system. The daemon is the process that runs in the operating system to which clients talk to.
  - **Docker Client** is the primary way that many Docker users interact with Docker. When you use commands such as `docker run`, the client sends these commands to `dockerd`, which carries them out. The docker command uses the Docker API. The Docker client can communicate with more than one daemon.
  - **Docker Registries** is a place where you can store and distribute Docker images. The default registry is Docker Hub. You can even run your own private registry. If you use Docker Datacenter (DDC), it includes Docker Trusted Registry (DTR).

**4. What is Docker Compose?**

[Docker Compose](https://docs.docker.com/compose/) is a tool for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application’s services. Then, with a single command, you create and start all the services from your configuration. To learn more about the Compose file, see the Compose file reference.

**5. What is Docker Swarm?**

[Docker Swarm](https://docs.docker.com/engine/swarm/) is a native clustering tool for Docker. It turns a pool of Docker hosts into a single, virtual Docker host. Because Docker Swarm serves the standard Docker API, any tool that already communicates with a Docker daemon can use Swarm to transparently scale to multiple hosts: Compose, Swarm mode, Kubernetes, and any other tool that already uses Docker can use Swarm to scale to multiple hosts. Docker Swarm is natively integrated into Docker Engine, so you can use it with any Docker application.

**6. Homework Questions**
    
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

**7. Layer caching**

Docker uses a caching mechanism to save time when building images. When you build an image, Docker creates a series of layers that represent the instructions in the Dockerfile. Each layer is only recreated if the instructions that created it have changed. This means that if you change the `RUN` command in your Dockerfile, all subsequent layers after that command are recreated. However, if you change the `COPY` command, all subsequent layers after that command are recreated. This is because the `COPY` command affects the filesystem, which is represented by the layers that follow it.

**8. 3-tier Web Application**

