## `Important Information:` This document includes `multiple gif files` that describe the process of `testing some API connections`. Wait for the gif files to download completely before viewing all instruction.



# Multi-tier web application Deployment in Kubernetes

# Table of contents:
- [1. Requirements](#1-requirements)
- [2. Knowledge](#2-knowledge)
  - [2.1. What is Kubernetes?](#21-what-is-kubernetes)
  - [2.2. What are the benefits of Kubernetes?](#22-what-are-the-benefits-of-kubernetes)
  - [2.3. What is Kubernetes used for?](#23-what-is-kubernetes-used-for)
  - [2.4. Kubernetes Architecture](#24-kubernetes-architecture)
  - [2.5. Deploy using Docker-compose](#25-deploy-using-docker-compose)
- [3. Getting started](#3-getting-started)
  - [3.1. Pre-requisites ](#31-pre-requisites)
- [4. Deploying the application on Kubernetes](#4-deploying-the-application-on-kubernetes)
  - [4.1. Application architecture](#41-application-architecture)
  - [4.2. Deploy backend and frontend](#42-deploy-backend-and-frontend)
  - [4.3. Deploy database - MongoDB](#43-deploy-database---mongodb)
  - [4.4. Thoroughly check the operation of the application.](#44-thoroughly-check-the-operation-of-the-application)
- [5. References](#5-references)


## 1. Requirements:

[Assignment: Deploy a Multi-tier Application on Kubernetes - It's here](https://github.com/phamchien94/k8s-hands-on-lab/tree/main)

1. Design and create the necessary YAML files to deploy the following components:
   - Frontend Deployment and Service: Deploy a frontend web server (e.g., Nginx) with multiple replicas. Expose the frontend service to access it from outside the cluster.
   - Backend Deployment and Service: Deploy a backend API server (e.g., Node.js, Flask, or any other framework) with multiple replicas. Expose the backend service within the cluster.
   - Database Deployment and Service: Deploy a database (e.g., MySQL or PostgreSQL) with persistent storage for data persistence. Expose the database service within the cluster.

2. Configure the appropriate networking between the frontend, backend, and database components.
   - The frontend should be able to communicate with the backend API server.
   - The backend API server should be able to access the database for data storage and retrieval.

3. Test the application by accessing the frontend web server from outside the cluster and verifying that it communicates with the backend API server and retrieves data from the database.

4. Document the steps followed to deploy the application, including the YAML files created and any necessary configuration details.

5. Submit the documentation and the YAML files as the assignment deliverables.



## 2. Knowledge
### 2.1 What is Kubernetes?
<div align="center">
  <img width="1500" src="images/k8s-Application.png" alt="k8s-archi">
</div>

<div align="center">
<i>
        Kubernetes Terminology
    </i>
</div>

- Kubernetes is one of the leading container orchestration tools, but for larger and more complex application workloads. It offers much more flexibility, scalability, reliability, and specificity on how to deploy workloads.

- With the widespread adoption of containers among organizations, Kubernetes, the container-centric management software, has become the de facto standard to deploy and operate containerized applications. 

### 2.2. What are the benefits of Kubernetes?

Automated operations

- Kubernetes has built-in commands to handle a lot of the heavy lifting that goes into application management, allowing you to automate day-to-day operations. You can make sure applications are always running the way you intended them to run.

Infrastructure abstraction

- When you install Kubernetes, it handles the compute, networking, and storage on behalf of your workloads. This allows developers to focus on applications and not worry about the underlying environment.

Service health monitoring
- Kubernetes continuously runs health checks against your services, restarting containers that fail, or have stalled, and only making available services to users when it has confirmed they are running.

### 2.3. What is Kubernetes used for?

Increasing development velocity
- Kubernetes helps you to build cloud-native microservices-based apps. It also supports containerization of existing apps, thereby becoming the foundation of application modernization and letting you develop apps faster.

Deploying applications anywhere
- Kubernetes is built to be used anywhere, allowing you to run your applications across on-site deployments and public clouds; as well as hybrid deployments in between. So you can run your applications where you need them.

Running efficient services
- Kubernetes can automatically  adjust the size of a cluster required to run a service. This enables you to automatically scale your applications, up and down, based on the demand and run them efficiently.


### 2.4. Kubernetes Architecture

<div align="center">
  <img width="1500" src="images/k8s-cluster.png.webp" alt="k8s-archi">
</div>

<div align="center">
<i>
        Kubernetes Architecture
    </i>
</div>

`Kubernetes control plane:` Also known as the master machine, is the container orchestration layer that exposes the API and interfaces to define, deploy, and manage the lifecycle of containers aswell as the nodes that hold the containerized applications. It ensures that every cluster is kept in its desired state.

`API Server:` The Application Programming Interface also know as API is the front end of Kubernetes. It is where clients make an initial request for an object or a collection and it determines if the request is valid and then it will process it. The API server also is what is used to transmit, create, and configure data within K8 clusters.

`K8s scheduler:` The scheduler is what watches and manages pods that are newly created and assigns them to a node so they can run on it smoothly.

`Controller manager:` Within the Control Plane there are multiple controllers, they are the control loops designed to watch the state of your cluster and make or request changes as they are needed.

`Etcd:` Is a data base where all your container storage is stored. It is a strongly consistent, distributed key-value store that holds and manages the critical information that systems need to run.

`Cluster`

`NODE:`(also known as a minion, or worker)is a machine on which containers are deployed. Each node must run a container runtime such as Docker, CoreOS rkt, Containerd, etc. Multiple Nodes can be grouped into Clusters.

`Pod:` are the base element in Kubernetes. A Pod consists of one or more containers and are co-located on  nodes.

## 3. Getting started

### 3.1. Pre-requisites
* [`kubectl`](https://kubernetes.io/docs/tasks/tools/)
* [`minikube`](https://minikube.sigs.k8s.io/docs/)
* [`jq`](https://github.com/stedolan/jq/)


`Minikube` is a tool that runs a single-node Kubernetes cluster in a VM on your local machine. It can be used to try out Kubernetes, learn about its features, and develop and test Kubernetes applications. Minikube is available for Linux, macOS, and Windows.

`Kubectl` is a command-line tool for managing Kubernetes clusters. It allows you to create, delete, list, and describe Kubernetes resources. kubectl can be used to manage a cluster that is running locally or in the cloud.

`jq` is a lightweight and flexible command-line JSON processor. `jq` is like `sed` for JSON data - we can use it to slice and filter and map and transform structured data with the same ease that sed, awk, grep and friends let we play with text.


## 4. Deploying the application on Kubernetes

### 4.1. Application architecture

This application employs a three-tier application architecture, and our Kubernetes cluster will be configured as follows:

To quickly summarize this layout, we have a back end with a deployment that guarantees we always have two pods active, and the same is true for our front end. Our ingress redirects and configures traffic, so /api requests go to our back end while all other requests go to the front end. The connection to the database, where we use MongoDB, is made by our application's back end.

<div align="center">
  <img width="1500" src="images/application_architecture.png" alt="app-archi">
</div>

<div align="center">
<i>
        Application architecture
    </i>
</div>


To simplify the installation process of the application, we can use a single `kubectl` command to deploy our demo application on Kubernetes. The single file we’ll use includes all of the deployments and services for the back end and front end of our application, and uses containers created with the Dockerfiles in the folder. 

- Build and push docker images to the docker registry:

```sh
cd src/back

docker build . -t trongminhjr/mern-k8s-back

docker push trongminhjr/mern-k8s-back

cd ..

cd front

docker build . -t trongminhjr/mern-k8s-front

docker push trongminhjr/mern-k8s-back

```

<div align="center">
  <img width="1500" src="images/images_on_registry.png" alt="k8s-archi">
</div>

<div align="center">
<i>
        Docker images
    </i>
</div>

Launch minikube

```sh
minikube start
```

<div align="center">
  <img width="1500" src="images/minikube_start.png" alt="k8s-archi">
</div>

<div align="center">
<i>
        Minikube start
    </i>
</div>

We need to run `minikube tunnel` to access our services at `localhost`.

```sh
minikube tunnel
```

### 4.2. Deploy backend and frontend

`Backend deployment file`
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mern-k8s-back
  labels:
    app: mern-k8s
    component: back # Selects Pods with the label "component: back" to be associated with the Deployment
spec:
  replicas: 2 # Defines the number of deployed application instances is 2.
  selector: 
    matchLabels:
      component: back
  template:
    metadata: 
      labels:
        app: mern-k8s
        component: back
    spec:
      containers:
        - name: mern-k8s-back
          image: trongminhjr/mern-k8s-back
          ports: 
            - containerPort: 3000
          env: # Defines the environment variables passed to the container.
            - name: PORT
              value: "3000"
            - name: CONN_STR # store the connection string to the MongoDB database
              value: "mongodb://admin:admin@mongo:27017"
```

`Backend service file`

```yaml
apiVersion: v1 
kind: Service 
metadata:
  name: mern-k8s-back 
  labels:
    app: mern-k8s 
    component: back
spec:
  type: LoadBalancer # Specifies the type of the Service as LoadBalancer
  selector:
    component: back # Selects Pods with the label "component: back" to be associated with the Service
  ports:
    - port: 3000 # Specifies the port on which the Service will listen
      targetPort: 3000 # Specifies the port on the Pods to which the requests will be forwarded
      protocol: TCP # Specifies the TCP protocol to be used for the port 
      name: http

```
`Frontkend deployment file`
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mern-k8s-front
  labels:
    app: mern-k8s
    component: front
spec:
  replicas: 2
  selector: 
    matchLabels:
      component: front
  template:
    metadata: 
      labels:
        app: mern-k8s
        component: front
    spec:
      containers:
        - name: mern-k8s-front
          image: trongminhjr/mern-k8s-front:v1
          ports: 
            - containerPort: 80
          env: 
            - name: BASE_URL
              value: "http://localhost:3000"

```

`Frontkend service file`
```yaml
apiVersion: v1
kind: Service
metadata:
  name: mern-k8s-front
  labels:
    app: mern-k8s
    component: front
spec:
  type: LoadBalancer
  selector:
    component: front
  ports:
    - port: 80
      targetPort: 80
      protocol: TCP
      name: http
```
Now, let’s go ahead and deploy frontend and backend in our Kubernetes cluster by applying the following code:

```shell
cd k8s

kubectl apply -f .
 ```
 Hoặc
 ```sh
 cd k8s

kubectl apply -f aio_app.yaml
```

<div align="center">
  <img width="1500" src="images/deploy_wt_db.png" alt="dl_front and back">
</div>

<div align="center">
<i>
        Checking frontend and backend deployment
    </i>
</div>


<div align="center">
  <img width="1500" src="images/test_deploy_without_db.gif" alt="dl_front and back">
</div>

<div align="center">
<i>
        Checking website
    </i>
</div>

The website can be accessed from outside the cluster, however, information cannot be saved because it is not connected to the database yet


### 4.3. Deploy database - MongoDB

`Create MongoDB Persistent Volume`

`PersistentVolumes (PV):` are objects which map to a storage location. It’s a piece of storage in the cluster that has been provisioned by an administrator.

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: mo-data-pv
spec:
  accessModes:
  - ReadWriteOnce
  capacity:
    storage: 1000Mi
  hostPath:
    path: /data/standard/default/mo-data-pv
    type: ""
  persistentVolumeReclaimPolicy: Retain
  storageClassName: standard
  volumeMode: Filesystem
```

`Create MongoDB Persistent Volume Claims`

`Persistent Volume Claims (PVC):` are Kubernetes objects that act as requests for storage. Kubernetes looks for a PV from which space can be claimed and assigned for a PVC. PVC works only if you have dynamic volume provisioning enabled in the Kubernetes cluster.

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: mo-data-pvc
spec:
  storageClassName: standard
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 1000Mi
```

Deployment MongoDB
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mongo
  labels:
    app.kubernetes.io/name: mongo
    app.kubernetes.io/component: backend
spec:
  selector:
    matchLabels:
      app.kubernetes.io/name: mongo
      app.kubernetes.io/component: backend
  replicas: 2
  template:
    metadata:
      labels:
        app.kubernetes.io/name: mongo
        app.kubernetes.io/component: backend
    spec:
      containers:
      - name: mongo
        volumeMounts:
          - mountPath: /data/db
            name: mo-data
        image: mongo:6.0
        args:
          - --bind_ip
          - 0.0.0.0
        resources:
          requests:
            cpu: 100m
            memory: 100Mi
        ports:
        - containerPort: 27017
        env:
          - name: MONGO_INITDB_ROOT_USERNAME
            value: "admin"
          - name: MONGO_INITDB_ROOT_PASSWORD
            value: "admin"
      volumes:
      - name: mo-data
        persistentVolumeClaim:
          claimName: mo-data-pvc
      restartPolicy: Always

```


Service MongoDB

```yaml
apiVersion: v1
kind: Service
metadata:
  name: mongo
  labels:
    app.kubernetes.io/name: mongo
    app.kubernetes.io/component: backend
spec:
  ports:
  - port: 27017
    targetPort: 27017
  selector:
    app.kubernetes.io/name: mongo
    app.kubernetes.io/component: backend

```


let’s deploy MongoDB in our Kubernetes cluster by applying the following code:

```shell
cd mongo

kubectl apply -f .
 ```

<div align="center">
  <img width="1500" src="images/deploy_db.png" alt="dl_front and back">
</div>

<div align="center">
<i>
        Deploy DB
    </i>
</div>


<div align="center">
  <img width="1500" src="images/health_check_db.png" alt="dl_front and back">
</div>

<div align="center">
<i>
        Check connection between backend and database
    </i>
</div>

### 4.4. Thoroughly check the operation of the application.

<div align="center">
  <img width="1500" src="images/test_deploy_with_database.gif" alt="dl_front and back">
</div>

<div align="center">
<i>
        Checking website
    </i>
</div>


Everything works as expected. Data is stored into Databsae and can be deleted from the user interface.






## 5. References

- https://devopscube.com/deploy-mongodb-kubernetes/
- https://mazzine.medium.com/create-mongodb-server-on-kubernetes-with-persistentvolume-6cab32dde2fc
- https://kubernetes.io/docs/home/
- https://www.mirantis.com/cloud-native-concepts/getting-started-with-kubernetes/what-are-kubernetes-secrets/
- https://github.com/kubernetes/minikube












