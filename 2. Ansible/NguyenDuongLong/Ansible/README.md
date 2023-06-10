## Ansible hands-on lab

### I, Install ansible

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

### II, Install collection

- Install community.docker
  ```
  ansible-galaxy collection install community.docker
  ```

### III, How to use

To execute each playbook, cd to the corresponding directory and run this command (with flag --ask-become-pass you must be enter your root password):

```
ansible-playbook -i inventory.yaml --ask-become-pass setup.yaml
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