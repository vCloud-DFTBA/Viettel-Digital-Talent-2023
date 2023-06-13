# Kubernetes Homework

# Table of contents
## [1. Kubernetes Overview](#1-kubernetes-overview)

-   ### [1.1 Introduction to Kubernetes](#11-introduction-to-kubernetes)
-   ### [1.2 Kubernetes Components](#12-kubernetes-components)
-   ### [1.3 Kubernetes Architecture](#13-kubernetes-architecture)

## [II. Homework](#2-homework)


# 1. Kubernetes Overview

## 1.1 Introduction to Kubernetes

**Kubernetes**, developed by Google, is an **open-source container orchestration tool** that facilitates the **management of containerized applications** across various deployment environments such as physical machines, virtual machines, cloud environments, and even hybrid deployments.

The trend towards *microservices*, the *increased usage of containers*, and the need to manage *large numbers of containers* efficiently have all driven the demand for container orchestration tools.

Kubernetes offers a wide range of features that facilitate the management and operation of containerized applications:

- High availability or no downtime
- Scalability or high performance
- Disaster recovery - backup and restore
- Load balancing and service discovery
- Rolling updates and rollbacks

## 1.2 Kubernetes Components

- **Node**: A server, either physical or virtual, that acts as a basic unit in Kubernetes.
- **Pod**: The smallest unit in Kubernetes, serving as an **abstraction over a container**. A Pod creates a runtime environment or layer on top of the container. Typically, each Pod runs a single application. Pods can communicate with each other using these IP addresses. If a Pod fails or is terminated, a new Pod is automatically created to replace it, and the new Pod will be assigned a new IP address during recreation.
- **Service**: Provides a static or **permanent IP address** for Pods. The lifecycle of Pods and Services is independent of each other. Services allow for stable network access to Pods, even if the Pods are replaced or relocated.
- **Ingress**: *Manages external access* to services within a cluster by routing incoming requests based on defined rules. It serves as an entrypoint for external traffic to reach services running in the cluster, allowing for load balancing, SSL termination, and URL-based routing.
- **ConfigMap**: Used to store **external configurations** for applications. It typically contains data such as database URLs or other service configurations. ConfigMaps provide a way to decouple application configurations from the container image, making it easier to manage and update configuration settings without modifying the application itself.
- **Secret**: Used to **store secret data** (in base64 encoded format)
- **Volumes**: Attaches a physical storage on hard drive to Pod and that storage could be either on a local machine or remote storage
- **Deployment**: In Kubernetes, a Deployment serves as a **blueprint** for creating and managing Pods. It allows you to define the desired number of replicas and provides the ability to scale the replicas up or down as needed. Deployments provide a higher-level **abstraction over Pods**, making it easier to interact with, replicate, and configure them.
- **StatefulSet**: Manages stateful applications like databases by handling Pod replication and scaling while ensuring synchronized database operations to maintain data consistency.

## 1.3 Kubernetes Architecture

**Worker Node**
In a Kubernetes cluster, each node hosts multiple Pods. The three essential processes installed on every node are:
  - **Container runtime**: Manages the execution of containers.
  - **Kubelet**: Interacts with the container and node, starting Pods with assigned resources.
  - **Kube-proxy**: Forwards requests from services to Pods, optimizing communication with low overhead. For example, if an application replica named "my-app" initiates a request to a database, Kube-proxy ensures that the request is forwarded to the replica running on the same node as the requesting Pod, minimizing network overhead.
  
Worker nodes perform the actual work in the Kubernetes cluster, requiring these processes to be installed.

<p align = "center">
<img src = "./images/worker_node.png" width = 400 height = 400> 
<br>Picture 1. Worker Nodes with 3 processes (container runtime, kubelet and kube-proxy)
</p>

**Master Node**
4 processes run on every master node
- **API server**: The API server is the cluster gateway, receiving requests for updates or queries. Also it acts as a gatekeeper for authentication. To deploy a new application in a Kubernetes cluster, users interact with the API server using clients like the Kubernetes dashboard, Kubectl, or the Kubernetes API.
- **Scheduler**: Assigns Pods to specific worker nodes based on factors like resource availability and affinity rules. When a request to schedule a new Pod is received by the API server, it is passed to the scheduler, which decides on the optimal node for deployment. The actual process of starting the Pod and its containers is handled by the Kubelet.
- **Controller manager**: Detects pod failures and requests the scheduler to reschedule them on available nodes to restore the cluster's desired state.
- **etcd**: A key-value store that maintains the state of a Kubernetes cluster, storing changes such as pod scheduling and failures. It does not store application data.

In practice, a Kubernetes cluster is composed of multiple Master nodes, each running its own set of processes. The API server is load balanced, and the etcd store is distributed across all the Master nodes for reliable storage.

<p align = "center">
<img src = "./images/master_node.png" width = 250 height = 400> 
<br>Picture 2. Master Nodes with 4 processes (api server, scheduler, controller manager and etcd)
</p>

<p align = "center">
<img src = "./images/master_node.png" width = 250 height = 400> 
<br>Picture 2. Master Nodes with 4 processes (api server, scheduler, controller manager and etcd)
</p>

<p align = "center">
<img src = "./images/cluster_setup.png" width = 800 height = 500> 
<br>Picture 3. Example cluster set-up
</p>

**Still working on README :v**