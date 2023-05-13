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
ansible-playbook -i inventory.yaml --ask-vault-password --ask-become-pass setup.yaml
```

<b>1,</b> You can configure this file to specify which roles should be run:

<img src= images/file_setup.png>