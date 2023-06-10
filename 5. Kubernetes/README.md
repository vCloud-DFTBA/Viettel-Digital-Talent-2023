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
  - [4.5. The next direction of development](#45-the-next-direction-of-development)
- [5. Conclusions](#5-conclusions)
- [6. References](#6-references)


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
        Checking website without database (GIF File)
    </i>
</div>


The website can be accessed from outside the cluster, however, information cannot be saved because it is not connected to the database yet


### 4.3. Deploy database - MongoDB

`Create MongoDB Persistent Volume`

`PersistentVolumes (PV):` are objects which map to a storage location. It’s a piece of storage in the cluster that has been provisioned by an administrator.
Simply that the PersistentVolume (PV) is a system resource for storage in the same way that a node is a system resource for compute. PersistentVolumes are administrator-facing objects: system resources to be defined to use. 

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

`Persistent Volume Claims (PVC):` are Kubernetes objects that act as requests for storage. Kubernetes looks for a PV from which space can be claimed and assigned for a PVC. PVC works only if you have dynamic volume provisioning enabled in the Kubernetes cluster. This is essentially your app's voucher for storage utilization.

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

`Create MongoDB Secrets`

Secrets in Kubernetes are the objects used for supplying sensitive information to containers. They are like ConfigMaps with the difference that data is stored in an encoded format.

For the security of our MongoDB instance, it is wise to restrict access to the database with a password. We will use Secrets to mount our desired passwords to the containers.

Save the following manifest as `mongodb_secrets.yaml`

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: mongo-creds
# type: Opaque
data:
  password: YWRtaW4=
  username: YWRtaW4=
```

Decoding contents of Secret objects

Kubernetes stores the content of all secrets in a base 64 encoded format. If you want to see how your string will appear in a base64 format, execute the following.
```sh
echo "VDT2023" | base64 

# after encoding it, this becomes VkRUMjAyMw==
# If you want to decode a base64 string. Run

echo "VkRUMjAyMw==" | base64 --decode
# after decoding it, this will give VDT2023
```



`Deployment MongoDB`
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
  replicas: 1
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
            valueFrom:
              secretKeyRef:
                name: mongo-creds
                key: username

          - name: MONGO_INITDB_ROOT_PASSWORD
            valueFrom:
              secretKeyRef:
                name: mongo-creds
                key: password
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


Let’s deploy MongoDB in our Kubernetes cluster by applying the following code:

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
        Checking website (GIF File)
    </i>
</div>


Everything works as expected. Data is stored into Databsae and can be deleted from the user interface.

### 4.5. `The next direction of development` 
The next direction of development, we will be to use helm chart. Using helm chart will have benefits such as:
* **Application Packaging and Deployment:** Helm charts can be used to package and deploy applications on Kubernetes. This makes it easy to distribute and deploy applications to multiple Kubernetes clusters.
* **Version Control:** Helm charts can be version controlled, making it easy to track changes to the application and roll back to previous versions if needed.
* **Configuration management:** Helm chart can be used to manage the configuration of applications. This makes it easy to change the configuration of the applications without having to manually edit the Kubernetes manifests.
* **Reproducibility:** Helm charts can be used to reproduce application deployments. This makes it easy to deploy the same application on different Kubernetes clusters or restore the application to its original state.

Helm charts also easily assist in autoscaling the application.

#### `Autoscaling`

`Autoscaling` is a feature of Kubernetes that automatically scales the number of pods in a Deployment or StatefulSet based on the observed CPU utilization of the pods. This allows we to ensure that our application has the resources it needs to handle demand without overprovisioning resources and wasting money.

To configure autoscaling in Kubernetes, we need to create a HorizontalPodAutoscaler (HPA) object. An HPA object specifies the desired number of pods in a Deployment or StatefulSet, as well as the minimum and maximum number of pods that can be running. The HPA object also specifies a target CPU utilization for the pods. When the observed CPU utilization of the pods reaches the target CPU utilization, the HPA object will automatically scale the number of pods up or down.

#### `Helm Charts and Autoscaling`

Helm charts can be configured to use HPAs to automatically scale the number of pods in a Deployment or StatefulSet based on the observed CPU utilization of the pods.

To configure autoscaling in a Helm chart, we need to specify the following in the chart's values.yaml file:

* **minReplicas:** The minimum number of pods that should be running in the Deployment or StatefulSet.
* **maxReplicas:** The maximum number of pods that should be running in the Deployment or StatefulSet.
* **targetCPUUtilizationPercentage:** The target CPU utilization percentage for the pods. When the observed CPU utilization of the pods reaches the target CPU utilization percentage, the HPA object will automatically scale the number of pods up or down.

For example, the following values.yaml file specifies that the Deployment named nginx should have a minimum of 1 pod and a maximum of 5 pods. The HPA object will automatically scale the number of pods up or down when the observed CPU utilization of the pods reaches 50%.

```yaml
minReplicas: 1
maxReplicas: 5
targetCPUUtilizationPercentage: 50
```

We can also use the helm autoscale command to configure autoscaling for a Helm chart. For example, the following command will configure autoscaling for the Deployment named nginx:

```bash
helm autoscale nginx --min=1 --max=5 --cpu-percent=50
```

Once we have configured autoscaling for a Helm chart, Kubernetes will automatically scale the number of pods in the Deployment or StatefulSet based on the observed CPU utilization of the pods. This will ensure that our application has the resources it needs to handle demand without overprovisioning resources and wasting money.


## 5. Conclusions

- A simple web app was built to deploy them on Kubernetes. The implementation needs to pay attention to namespaces, labels so that they can be linked together when in the same namespace and labels.
- Database implementation is a challenge. A MongoDB deployment instance was created, a client to connect to it, run basic operations like data entry, and also explore how to connect from outside the Kubernetes cluster.
- Multiple replicas have been created to increase the HA property of the application.
- The database connection also needs attention because the pods communicate with each other via name or internal IP.
- Secrets have also been used to store sensitive database information.

## 6. References

- https://devopscube.com/deploy-mongodb-kubernetes/
- https://mazzine.medium.com/create-mongodb-server-on-kubernetes-with-persistentvolume-6cab32dde2fc
- https://kubernetes.io/docs/home/
- https://www.mirantis.com/cloud-native-concepts/getting-started-with-kubernetes/what-are-kubernetes-secrets/
- https://github.com/kubernetes/minikube












