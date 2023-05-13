## Ansible hands-on lab

### Install ansible

- Install virtualenv
  ```
  sudo apt install python3-virtualenv
  ```

- Activate virtualenv
  ```
  virtualenv venv && source venv/bin/activate
  ```

- Install ansible inside virtualenv
  ```
  pip install ansible
  ```

- Test ansible installation:
  ```
  ansible --version
  ```

### How to use

This repos contain a playbook to setup and hardening a typical Ubuntu server in three different styles:
1. Using shell commands
2. Using modules
3. Factoring tasks into roles

To execute each playbook, cd to the corresponding directory and run this command:

```
ansible-playbook -i inventory.yaml setup.yaml
```


-------------------
1. handlers:
- Các tasks trong handlers chỉ chạy khi có sự thay đổi

2. Chạy playbook với file đã mã hóa vault:
ansible-playbook -i inventory.yaml --ask-vault-password setup.yaml

3. Chạy playbook với tag --ask-become-pass để nhập mật khẩu:
ansible-playbook -i inventory.yaml --ask-vault-password --ask-become-pass setup.yaml

4. Install community.docker:
ansible-galaxy collection install community.docker

5. Config docker
in ~/.docker/config.json change credsStore to credStore