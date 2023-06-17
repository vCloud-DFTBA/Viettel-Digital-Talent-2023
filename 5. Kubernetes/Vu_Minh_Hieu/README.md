# Kubernetes

## _Deploy a Multi-tier Application on Kubernetes._

The objective of this assignment is to apply the concepts learned in the hands-on labs and deploy a multi-tier application on Kubernetes. The application consists of a frontend web server, a backend API server, and a database.

## I. Environment and Resource

The environment I used for this assignment was on macOS(arm64) with docker, kubectl, and minikube pre-installed.
For the resource, I reused the 3-tier app from the previous sections.

-   Database: MongoDB - Image: mongo:5.0
-   Backend: Fastapi - Image: hieuminhvuu/k8s_backend_v3:latest
-   Frontend: ReactJS-Nginx - Image: hieuminhvuu/k8s_frontend:latest

## II. Installation and Deployment

### 1. K8s cluster

I chose minikube for setup a cluster k8s

```
minikube start --driver=docker
```

<img src= images/minikube-start.png>
<img src= images/minikube-ip.png>

#### 2. Database

-   Create secret for username and password of database. Encode by base64

```
echo -n "admin" | base64
#result : YWRtaW4=
```

-   File db-secrets.yaml:

```
apiVersion: v1
kind: Secret
metadata:
    name: mongo-secrets
type: Opaque
data:
    password: YWRtaW4=
    username: YWRtaW4=
```

-   PersistentVolumes (PV) and Persistent Volume Claims (PVC):

To have Persistent Storage, I used PersistentVolumes and Persistent Volume Claims.

PersistentVolumes (PV): a type of data storage resource. PV is completely independent of pods and managed by K8s. Because it is independent of the pods, if the pod crashes or is deleted, the data will not be lost.

Persistent Volume Claims (PVC): When we want to use PV, we need to create PVC - a k8s object used to request storage from 1 PV.

-   File db-pvc.yaml:

```
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
    name: mongo-pvc
spec:
    storageClassName: standard
    accessModes:
        - ReadWriteOnce
    resources:
        requests:
            storage: 1000Mi
```

-   File db-pv.yaml:

```
apiVersion: v1
kind: PersistentVolume
metadata:
    name: mongo-pv
spec:
    accessModes:
        - ReadWriteOnce
    capacity:
        storage: 1000Mi
    hostPath:
        path: /data/standard/default/mongo-pv
        type: ""
    persistentVolumeReclaimPolicy: Retain
    storageClassName: standard
    volumeMode: Filesystem
```

-   Deployment and Service

File db.yaml

```
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
                        name: mongo-data
                  image: mongo:5.0
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
                                name: mongo-secrets
                                key: username

                      - name: MONGO_INITDB_ROOT_PASSWORD
                        valueFrom:
                            secretKeyRef:
                                name: mongo-secrets
                                key: password
            volumes:
                - name: mongo-data
                  persistentVolumeClaim:
                      claimName: mongo-pvc
            restartPolicy: Always
---
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

-   Deploy database:

```
cd k8s/database
kubectl apply -f .
```

<img src= images/database.png>
<img src= images/database-running.png>

#### 3. Backend

File api.yaml :

```
apiVersion: apps/v1
kind: Deployment
metadata:
    name: backend
    labels:
        app: backend
        component: backend
spec:
    replicas: 3
    selector:
        matchLabels:
            component: backend
    template:
        metadata:
            labels:
                app: backend
                component: backend
        spec:
            containers:
                - name: backend
                  image: hieuminhvuu/k8s_backend_v3
                  ports:
                      - containerPort: 80
                  env:
                      - name: MONGODB_HOST
                        value: "mongo"
                      - name: MONGODB_USER
                        valueFrom:
                            secretKeyRef:
                                name: mongo-secrets
                                key: username
                      - name: MONGODB_PASSWORD
                        valueFrom:
                            secretKeyRef:
                                name: mongo-secrets
                                key: password
---
apiVersion: v1
kind: Service
metadata:
    name: backend-service
    labels:
        app: backend
        component: backend
spec:
    selector:
        component: backend
    ports:
        - port: 80
          targetPort: 80
          protocol: TCP

```

-   Deploy backend:

```
cd k8s/api
kubectl apply -f .
```

<img src= images/api.png>
<img src= images/api-running.png>

#### 4. Frontend

-   File web.yaml :

```
apiVersion: apps/v1
kind: Deployment
metadata:
    name: frontend
    labels:
        app: frontend
        component: frontend
spec:
    replicas: 3
    selector:
        matchLabels:
            component: frontend
    template:
        metadata:
            labels:
                app: frontend
                component: frontend
        spec:
            containers:
                - name: frontend
                  image: hieuminhvuu/k8s_frontend
                  resources:
                      requests:
                          cpu: 100m
                          memory: 100Mi
                  ports:
                      - containerPort: 9333
---
apiVersion: v1
kind: Service
metadata:
    name: frontend-service
    labels:
        app: frontend
        component: frontend
spec:
    type: NodePort
    selector:
        component: frontend
    ports:
        - port: 9333
          targetPort: 9333
          protocol: TCP
          nodePort: 30100
```

-   Deploy frontend:

```
cd k8s/web
kubectl apply -f .
```

<img src= images/web.png>
<img src= images/web-running.png>

### 4. Result

So, I have finished deploying 3-tier app on K8S cluster.

-   Open port-forward for service frontend and backend:
    <img src= images/port-forward-backend.png>
    <img src= images/port-forward-frontend.png>
-   Here is my result :
    <img src= images/result2.png>
    <img src= images/result.png>
