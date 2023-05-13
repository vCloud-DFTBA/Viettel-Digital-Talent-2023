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

### Install collection

- Install community.docker
  ```
  ansible-galaxy collection install community.docker
  ```

### How to use

To execute each playbook, cd to the corresponding directory and run this command (with flag --ask-become-pass you must be enter your root password):

```
ansible-playbook -i inventory.yaml --ask-vault-password --ask-become-pass setup.yaml
```
