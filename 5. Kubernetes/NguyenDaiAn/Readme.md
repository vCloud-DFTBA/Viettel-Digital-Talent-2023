# Viettel k8s Handonlab Homework
## About
Tested on Minikubes and Kind.
The default config is:
- Deployments of web and api with a ReplicaSet of 3 each.
- Db in a StatefulSet with a PersistentVolume and PersistentVolumeClaim.
- A ConfigMap to add the initial database records init file.
- 3 services with one ClusterIP for accessing db and 2 NodePort for exposing web and api.
## Images
Screenshot including cluster's overview can be seen in the img directory.
## Codes
The project directory (k8s) is included.

A semi-implementation of Ansible orchestration is also present, though it lacks environment setup steps and also require entering password and username of one's own (I haven't tried using a vault, sorry), but I really enjoyed using it during development since it automates a lot of the process.
