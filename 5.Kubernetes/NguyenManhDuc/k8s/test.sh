# deploy the mongo database
kubectl apply -f db/db_volume_pv.yaml
kubectl apply -f db/db_volume_pvc.yaml
kubectl apply -f db/db_configmap.yaml
kubectl apply -f db/db_deployment.yaml
kubectl apply -f db/db_service.yaml
# deploy the api 
kubectl apply -f api/api_deployment.yaml
kubectl apply -f api/api_service.yaml
# deploy web ui
kubectl apply -f web/web_deployment.yaml
kubectl apply -f web/web_service.yaml