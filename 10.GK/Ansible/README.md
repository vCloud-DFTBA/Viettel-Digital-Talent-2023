## Ansible hands-on lab

### I, Install ansible

- Install virtualenv
  ```
  VPS : sudo apt install python3-venv
  Local: sudo apt install python3-virtualenv
  ```

- Activate virtualenv
  ```
  VPS: python3 -m venv venv
  ---
  virtualenv venv && source venv/bin/activate
  ```

- Install ansible inside virtualenv
  ```
  VPS:
    pip install --upgrade pip
    pip install cryptography 
    pip install ansible
    pip install requests
    pip show requests
  ---
  pip install ansible
  ```

- Test ansible installation:
  ```
  ansible --version
  ```

### II, Install collection

- Install community.docker
  ```
  ansible-galaxy collection install community.docker
  ```

### III, How to use

To execute each playbook, cd to the corresponding directory and run this command (with flag --ask-become-pass you must be enter your root password):

```
- Ask become password
ansible-playbook -i inventory.yaml --ask-become-pass setup.yaml
- Ask vault password
ansible-playbook -i inventory.yaml setup.yaml --ask-vault-pass
```

<b>1,</b> You can configure this file (./setup/setup.yaml) to specify which roles should be run:

<img src= images/file_setup.png>

<b>2,</b> Run role common:

<img src= images/common_rs.png>

<b>3,</b> Run role db:

<img src= images/db_rs.png>

<b>4,</b> Run role api:

<img src= images/api_rs.png>

<b>5,</b> Run role web:

<img src= images/web_rs.png>

### IV, Result

<b>1,</b> Containers:

<img src= images/containers.png>

<b>2,</b> App:

<img src= images/list_sv.png>

### IV, Note
<b>1,</b> VPS config:
<i>- Đặt password cho root, user. Sau đó sửa file /etc/ssh/sshd_config trường PasswordAuthentication thành "yes" để đăng nhập được qua user bằng password</i>

<i>Dùng lệnh sau để add user vào sudoers</i>
  ```
  sudo visudo
  - Thêm dòng này vào dưới dòng root    ALL=(ALL:ALL) ALL :
  long22263    ALL=(ALL:ALL) ALL
  ```

<b>2,</b> Ansible config:
<i>Dùng lệnh sau để vault password</i>
  ```
  ansible-vault encrypt_string --ask-vault-pass '123456aA@' --name 'vaulted_password'
  ```

<b>3,</b> Docker config:
<i>Khi chạy nginx container, nếu proxy_pass thì cần đặt ip của container đích hoặc container_name (cùng network) của ip đích</i>