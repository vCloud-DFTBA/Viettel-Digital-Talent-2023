# Hướng dẫn cài đặt 3-tier web application sử dụng Kubernetes
## Giới thiệu
Project này sử dụng 3 image chính: 
- nginx:latest cho frontend webserver
- xuanphu270101/phutx_python_image:k8s_exercise_v2 cho backend Flask app
- mongo:5.0

Việc cài đặt sẽ được thực hiện trên kindest/node:v1.22.0
## Chi tiết cài đặt
### Cài đặt kind và tạo cluster
```commandline
[ $(uname -m) = x86_64 ] && curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.19.0/kind-linux-amd64
[ $(uname -m) = aarch64 ] && curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.19.0/kind-linux-arm64
chmod +x ./kind
sudo mv ./kind /usr/local/bin/kind
kind create cluster --image kindest/node:v1.22.0
```
Xem tên kind container: 
```commandline
docker ps
```
Vào command line của kind container:
```commandline
docker exec -it <kind-container-name> bash
```
### Copy tất cả các file YAML vào kind
Để copy tất cả các file YAML vào kind, sử dụng cú pháp:
```commandline
echo '<file-content>' > <file-name>.yaml
```
### Cài đặt các component
```commandline
kubectl apply -f mongodb-pv.yaml
kubectl apply -f mongodb-pvc.yaml
kubectl apply -f secret.yaml
kubectl apply -f configmap.yaml
kubectl apply -f db-sfs.yaml
kubectl apply -f backend-depl.yaml
kubectl apply -f frontend-depl.yaml
```
Kiểm tra hoạt động các component:
```commandline
kubectl get pods
```
Nếu xuất hiện 3 deployment frontend, 3 deployment backend và 1 statefulset mongo với status running thì việc cài đặt thành công.
```commandline
root@kind-control-plane:/# kubectl get pods
NAME                                  READY   STATUS    RESTARTS   AGE
backend-deployment-56c4f5768c-28rvl   1/1     Running   0          65m
backend-deployment-56c4f5768c-mb5vz   1/1     Running   0          65m
backend-deployment-56c4f5768c-qhrh7   1/1     Running   0          65m
frontend-deployment-576b446c9-k9ctl   1/1     Running   0          8m10s
frontend-deployment-576b446c9-vnjv2   1/1     Running   0          8m10s
frontend-deployment-576b446c9-zzgqg   1/1     Running   0          8m10s
mongodb-0                             1/1     Running   0          6s

```