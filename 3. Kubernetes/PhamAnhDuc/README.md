1. Create cluster with ports mapping to host machine
```sh
kind create cluster --name vdt --config kind-cluster.config.yml
```
![Create Cluster](./images/create-cluster.png)
2. Apply MongoDB deployment

```sh
kubectl apply -f db-deployment.yml 
```
![Apply Mongodb Deployment](./images/apply-mongo-deployment.png)
3. Apply API server deployment

```sh
kubectl apply -f api-deployment.yml 
```
![Apply API deployment](./images/apply-mongo-deployment.png)
4. Apply Nginx WebServer Deployment

```sh
kubectl apply -f config_map/nginx-configmap.yml
kubectl apply -f webserver-deployment.yml
```
![Apply WebServer Deployment](./images/apply-nginx-deployment.png)


5. Truy cập front-end với đường dẫn `http://localhost:80` 

![Kubectl get all](./images/kubectl-get-all.png)