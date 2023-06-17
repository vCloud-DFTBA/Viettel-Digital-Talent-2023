# Commands
```bash
ansible-playbook -i inventory.yaml webapp.yaml
```
# Role common
1. Cài đặt machine như hướng dẫn trên lớp
2. Cài đặt Docker Engine
3. Cài đặt Docker SDK for Python (theo [requirement](https://docs.ansible.com/ansible/2.9/modules/docker_container_module.html) của Ansible module `docker_container`  )
4. Tạo network cho các container.

# Role Web
1. Pull image từ dockerhub 
2. Join vào network 
3. Chạy docker

# Role Api
1. Pull image từ dockerhub
2. Cài đặt một số biến môi trường
3. Join vào network
4. Chạy docker

# Role Db
1. Pull image từ dockerhub
2. Cài đặt volume, network
3. Chạy docker