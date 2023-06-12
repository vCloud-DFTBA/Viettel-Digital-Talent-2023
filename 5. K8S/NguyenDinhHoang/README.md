## Deploy a Multi-tier Application on Kubernetes
**Objective**: The objective of this assignment is to apply the concepts learned in the hands-on labs and deploy a multi-tier application on Kubernetes. The application consists of a frontend web server, a backend API server, and a database.

## **`Setup the Environment`**
### **1. Create a Kubernetes cluster with one master and three worker nodes.**
- This is not included in this assignment. For more information, please refer to this [**`ansible project`**](https://github.com/hoangndst/stuffops/tree/master/kubernetes/cluster) link.
- I use Helm for genarating deployment files. For more information, please refer to this [**`helm project`**](https://helm.sh/)
### **2. Seup nfs server, nfs client on all nodes.**
- Setup nfs server like previous [**`Ansible Assignment`**](https://github.com/hoangndst/Viettel-Digital-Talent-2023/tree/practice2/2.%20Ansible/NguyenDinhHoang#create-nfs-server-for-sharing-data-between-nodes)

### **3. Deploy nfs external provisioner**
- Create a namespace for the NFS provisioner:
  ```bash
  kubectl create namespace storage
  ```
- We have 2 types of reclaim policy: `Retain` and `Delete`. In this assignment, we use `Retain` policy.
  - Retain: The Retain reclaim policy allows for manual reclamation of the resource. When the PersistentVolumeClaim is deleted, the PersistentVolume still exists and the volume is considered “released”. But it is not yet available for another claim because the previous claimant’s data remains on the volume. An administrator can manually reclaim the volume with the following steps.
  - Delete: The Delete reclaim policy allows for automatic reclamation of the resource. When the PersistentVolumeClaim is deleted, the associated PersistentVolume is also deleted. Deleting the PersistentVolume reclaims its resources. This means that a new PersistentVolumeClaim can be created, and the volume will have the same data, once the volume has been dynamically provisioned again.
- File Apply:
  - [**serviceaccount.yaml**](./nfs-external-provisioner/retain/serviceaccount.yaml): Defines a ServiceAccount named `nfs-client-provisioner` in the `storage` namespace. This ServiceAccount will be used to create a RoleBinding in the next step.
  - [**`role.yaml`**](./nfs-external-provisioner/retain/role.yaml): Defines a Role named `nfs-client-provisioner-runner` in the `storage` namespace. This Role will be used to create a RoleBinding in the next step.
  - [**`rolebinding.yaml`**](./nfs-external-provisioner/retain/rolebinding.yaml): Applies the Role created in the previous step to the ServiceAccount created in the first step.
  - [**`clusterrole.yaml`**](./nfs-external-provisioner/retain/clusterrole.yaml): This file creates a ClusterRole named `nfs-client-provisioner-runner` in the `storage` namespace. This ClusterRole will be used to create a ClusterRoleBinding in the next step.
  - [**`clusterrolebinding.yaml`**](./nfs-external-provisioner/retain/clusterrolebinding.yaml): This file creates a ClusterRoleBinding named `run-nfs-client-provisioner` in the `storage` namespace. This ClusterRoleBinding binds the ClusterRole created in the previous step to the ServiceAccount created in the first step.
  - [**`deployment.yaml`**](./nfs-external-provisioner/retain/deployment.yaml): This file creates a Deployment named `nfs-client-provisioner` in the `storage` namespace. This Deployment uses the ServiceAccount, Role, and RoleBinding created in the previous steps. This Deployment also defines the NFS server address and export path, as well as the reclaim policy for the PersistentVolumes that it creates.
  - [**`storageclass.yaml`**](./nfs-external-provisioner/retain/storageclass.yaml): This file creates a StorageClass named `nfs-client-retain`. This StorageClass defines the reclaim policy for the PersistentVolumes that it creates.
- Apply all files:
  ```bash
  kubectl apply -f nfs-external-provisioner/retain/
  ```
- Check status:
  ```bash
  kubectl get sc
  kubectl get pv
  kubectl -n monitoring get pvc
  ```
  <div align="center">
    <img src="./assets/k8s_sc.png" width="1200" />
  </div>
### **4. Deploy Load Balancer**
- In On-premise environment, we use MetalLB for Load Balancer. For more information, please refer to this [**`link`**](https://metallb.universe.tf/).
- But it doesn't support on Cloud environment. So, we use [**`Traefik`**](https://doc.traefik.io/traefik/) like an external load balancer, routing traffic to the correct NodePort.
- Deployment and config file here: [**`traefik`**](./traefik)

### **5. Label nodes**
- Label nodes for deploying application:
  ```bash
  kubectl label nodes <node-name> <label-key>=<label-value>
  ```
  - Worker1: frontend, backend, monitoring
  - Worker2: frontend, backend
  - Worker3: frontend, backend
  ``` bash
  NAME            STATUS   ROLES                         AGE     VERSION
  control-plane   Ready    control-plane                 5d16h   v1.27.2
  worker1         Ready    backend,frontend,monitoring   5d16h   v1.27.2
  worker2         Ready    backend,frontend              5d15h   v1.27.2
  worker3         Ready    backend,frontend              5d16h   v1.27.2
  ```
## **`Deploy the Application`**

<div align="center">
  <img src="./assets/project.png" width="1000" />
</div>

### **1. Deploy the database**
- I use MongoDB Community Kubernetes Operator to deploy MongoDB. For more information, please refer to this [**`link`**](https://docs.mongodb.com/kubernetes-operator/master/tutorial/install-k8s-operator/)
- Create Custom Resource Definition (CRD) MongoDBCommunity: [**`crds.yaml`**](./mongodb/crds.yaml)
  ```bash
  kubectl create -f crds.yaml
  ```
- Create a namespace for the MongoDB:
  ```bash
  kubectl create namespace mongodb
  ```
- Create a secret for MongoDB admin password: [**`secret.yaml`**](./mongodb/secret.yaml)
  ```bash
  kubectl create secret.yaml
  ```
- Create operator role: [**`operator_roles.yaml`**](./mongodb/operator_roles.yaml). Include ServiceAccount, Role, RoleBinding.
  ```bash
  kubectl create -f operator_roles.yaml
  ```
- Create database role: [**`database_roles.yaml`**](./mongodb/database_roles.yaml). Include ServiceAccount, Role, RoleBinding.
  ```bash
  kubectl create -f database_roles.yaml
  ```
- Deploy MongoDB Kubernetes Operator: [**`operator.yaml`**](./mongodb/operator.yaml).
  - Config resource limit:
    ``` yaml
      ...
      resources:
        limits:
          cpu: 1100m
          memory: 1Gi
        requests:
          cpu: 500m
          memory: 200Mi
      ...
    ```
    - `limits`: The maximum amount of compute resources allowed.
    - `requests`: The minimum amount of compute resources required.
  - Deploy MongoDB Community Kubernetes Operator:
    ```bash
    kubectl create -f operator.yaml
    ```
- Deploy MongoDB ReplicaSet: [**`mongodbcommunity_cr_with_tls.yaml`**](./mongodb/mongodbcommunity_cr_with_tls.yaml)
  - Config password for admin user:
    ```yaml
    ...
    spec:
      users:
      - db: admin
        name: admin
        passwordSecretRef:
          name: admin-password
        roles:
        - db: admin
          name: clusterAdmin
        - db: admin
          name: userAdminAnyDatabase
        - db: admin
          name: readWriteAnyDatabase
        - db: admin
          name: dbAdminAnyDatabase
    ...
    ```
  - Deploy MongoDB ReplicaSet:
    ```bash
    kubectl create -f mongodbcommunity_cr_with_tls.yaml
    ```
- Create NodePort service in port `30007` for MongoDB ReplicaSet Test Purpose: [**`service.yaml`**](./mongodb/service.yaml)
  ```bash
  kubectl create -f service.yaml
  ```
- Check status:
  ```bash
  kubectl -n mongodb get all
  kubectl -n mongodb get pvc
  ```
  <div align="center">
    <img src="./assets/mongodb_all.png" width="1200" />
  </div>
- Try to connect to MongoDB ReplicaSet:
  ```bash
  mongosh mongodb://admin:Hoang2002@10.114.0.5:30007
  ```
  <div align="center">
    <img src="./assets/mongodb_connect.png" width="1200" />
  </div>
### **2. Deploy backend**
- Create namespace for vdt application:
  ```bash
  kubectl create namespace vdt
  ```
- Create [**`secret.yaml`**](./3-tier/backend/secret.yaml) for backend, this is mongodb password:
  ```bash
  kubectl create -f secret.yaml
  ```
- Deploy [**`backend-deployment.yaml`**](./3-tier/backend/backend-deployment.yaml) for backend:
  - Image: **`hoangndst/vdt-backend:latest`**
  - Replica: 3
  - Mongodb host:
    ```yaml
    - name: MONGO_HOST
      value: "mongodb://mongodb-replica-set-svc.mongodb"
    ```
  - Mongodb password from secret created in previous step:
    ```yaml
    - name: MONGO_PASSWORD
      valueFrom:
        secretKeyRef:
          name: admin-password
          key: password
    ```
  - nodeSelector: Select node to deploy backend:
    ```yaml
    nodeSelector:
      node-role.kubernetes.io/backend: ""
    ```
  - Resource: Based on data available from resource monitoring for several days. With few users, the backend does not need much resources.
    <div align="center">
      <img src="./assets/backend_rs.png" width="1200" />
    </div>

    ```yaml
    resources:
      requests:
        memory: "64Mi"
        cpu: "250m"
      limits:
        memory: "128Mi"
        cpu: "500m"
    ```
  - Deploy backend:
    ```bash
    kubectl create -f backend-deployment.yaml
    ```
- Create NodePort `30005` [**`service.yaml`**](./3-tier/backend/service.yaml) for backend:
  ```bash
  kubectl create -f service.yaml
  ```
- Config Load Balancer for backend:
  ``` yaml
  http:
    routers:
      vdt-backend:
        rule: Host(`vdt-backend.hoangnd.freeddns.org`)
        entryPoints:
          - websecure
        service: vdt-backend
        tls:
          certResolver: production
    services:
      vdt-backend:
        loadBalancer:
          healthCheck:
            path: /test
            port: 30005
          servers:
            - url: http://10.114.0.5:30005
            - url: http://10.114.0.6:30005
            - url: http://10.114.0.7:30005
  ```
- URL: [**`https://vdt-backend.hoangnd.freeddns.org`**](https://vdt-backend.hoangnd.freeddns.org/test)
  <div align="center">
    <img src="./assets/backend.png" width="1200" />
  </div>
### **3. Deploy frontend**
- Deploy [**`frontend-deployment.yaml`**](./3-tier/frontend/frontend-deployment.yaml) for frontend:
  - Image: **`hoangndst/vdt-frontend:latest`**
  - Replica: 3
  - nodeSelector: Select node to deploy frontend:
    ```yaml
    nodeSelector:
      node-role.kubernetes.io/frontend: ""
    ```
  - Resource: Based on data available from resource monitoring for several days. With few users, the frontend does not need much resources.
    <div align="center">
      <img src="./assets/frontend_rs.png" width="1200" />
    </div>

    ```yaml
    resources:
      requests:
        memory: "64Mi"
        cpu: "250m"
      limits:
        memory: "128Mi"
        cpu: "500m"
    ```
  - Deploy frontend:
    ```bash
    kubectl create -f frontend-deployment.yaml
    ```
- Create NodePort `30003` [**`service.yaml`**](./3-tier/frontend/service.yaml) for frontend:
  ```bash
  kubectl create -f service.yaml
  ```
- Config Load Balancer for frontend:
  ``` yaml
  http:
    routers:
      vdt-frontend:
        rule: Host(`vdt-frontend.hoangnd.freeddns.org`)
        entryPoints:
          - websecure
        service: vdt-frontend
        tls:
          certResolver: production
    services:
      vdt-frontend:
        loadBalancer:
          healthCheck:
            path: /test
            port: 30003
          servers:
            - url: http://10.114.0.5:30003
            - url: http://10.114.0.6:30003
            - url: http://10.114.0.7:30003
- URL: [**`https://vdt-frontend.hoangnd.freeddns.org`**](https://vdt-frontend.hoangnd.freeddns.org)
  <div align="center">
    <img src="./assets/frontend.png" width="1200" />
  </div
### **4. Check namespace vdt**
```bash
kubectl -n vdt get all
```
<div align="center">
  <img src="./assets/vdt_all.png" width="1200" />
</div>

## **Deploy Monitoring Stack**
- This part is not include in K8S assignment, I will go through it quickly.
- Create namespace `monitoring`:
  ```bash
  kubectl create namespace monitoring
  ```
- Create [**`Custom Resource Definition`**](./monitoring/crds/).
  ```bash
  kubectl create -f crds/
  ```
- Create [**`Pesistent Volume Claim`**](./monitoring/) for Prometheus and Grafana:
  ```bash
  kubectl create -f prometheus-pvc.yaml
  kubectl create -f grafana-pvc.yaml
  ```
- Deploy Prometheus Operator, Prometheus, Grafana, Alertmanager: [**`monitoring.yaml`**](./monitoring/monitoring.yaml)
  - nodeSelector: Select node to deploy Grafana and Prometheus:
    ```yaml
    nodeSelector:
      node-role.kubernetes.io/monitoring: ""
    ```
  - Deploy:
    ```bash
    kubectl create -f monitoring.yaml
    ```
- Apply Grafana Dashboard (ConfigMap): [**`grafana-dashboardK8s.yaml`**](./monitoring/grafana-dashboardK8s.yaml)
  ```bash
  kubectl create -f grafana-dashboardK8s.yaml
  ```
- Create Prometheus, Grafana NodePort Service: [**`prometheus-service.yaml`**](./monitoring/prometheus-service.yaml), [**`grafana-service.yaml`**](./monitoring/grafana-service.yaml)
  ```bash
  kubectl create -f grafana-service.yaml
  kubectl create -f prometheus-service.yaml
  ```
- Config Load Balancer for Grafana, Prometheus:
  ``` yaml
  http:
    routers:
      prometheus:
        rule: Host(`prometheus.hoangnd.freeddns.org`)
        entryPoints:
          - websecure
        service: prometheus
        tls:
          certResolver: production
      grafana:
        rule: Host(`grafana.hoangnd.freeddns.org`)
        entryPoints:
          - websecure
        service: grafana
        tls:
          certResolver: production
    services:
      grafana:
        loadBalancer:
          servers:
            - url: http://10.114.0.6:30002
      prometheus:
        loadBalancer:
          servers:
            - url: http://10.114.0.6:30001
- Screenshots of some dashboards:
  
  <div align="center">
    <img src="./assets/gdb_global.png" width="1200" />
  </div>
  <div align="center">
    <img src="./assets/gdb_namespaces.png" width="1200" />
  </div>
  <div align="center">
    <img src="./assets/gdb_coredns.png" width="1200" />
  </div>

- Access to [**`https://grafana.hoangnd.freeddns.org`**](https://grafana.hoangnd.freeddns.org) to see all dashboards.
  - **`Username`**: viewer
  - **`Password`**: Hoang1999
## **All Project Website**
- **`Frontend`**: [**`https://vdt-frontend.hoangnd.freeddns.org`**](https://vdt-frontend.hoangnd.freeddns.org)
- **`Backend`**: [**`https://vdt-backend.hoangnd.freeddns.org`**](https://vdt-backend.hoangnd.freeddns.org/test)
- **`Prometheus`**: [**`https://prometheus.hoangnd.freeddns.org`**](https://prometheus.hoangnd.freeddns.org)
- **`Grafana`**: [**`https://grafana.hoangnd.freeddns.org`**](https://grafana.hoangnd.freeddns.org)
  - **`Username`**: viewer
  - **`Password`**: Hoang1999


## **References**
- [**`Kubernetes Documentation`**](https://kubernetes.io/docs/home/)
- [**`MongoDB Kubernetes Operator`**](https://github.com/mongodb/mongodb-kubernetes-operator)
- [**`Prometheus Operator`**](https://github.com/prometheus-operator/prometheus-operator)

<div align="center">
  <h3>Thank you for reading my assignment! It's my pleasure to receive your feedback!</h3>
</div>
