# Practice 2: Ansible <!-- omit in toc -->

Author: **Le Minh Duc**

## Table of Contents <!-- omit in toc -->

- [1. Requirements](#1-requirements)
- [2. Setting up nodes](#2-setting-up-nodes)
- [3. Setting up docker using role `common`](#3-setting-up-docker-using-role-common)
- [4. Splitting application into 3 roles: `web`, `api` and `db`](#4-splitting-application-into-3-roles-web-api-and-db)
- [5. Conclusion](#5-conclusion)
- [6. References](#6-references)

## 1. Requirements

Deploy the application in the docker-compose homework using ansible:

- Set up docker for the target environments using role "common".
- Split the application into 3 roles: "web", "api" and "db".

## 2. Setting up nodes

- Set up `Ubuntu Server` virtual machine and enable bridged network adapter. I choose `Ubuntu Server` because it is lightweight and easy to use.

- Get IP address of virtual machine:

```shell
$ ip a
...
    inet 192.168.0.x/24 ...
...
```

- Install Ansible for controller node:

```shell
pip3 install -U ansible
sudo apt install openshh-server
```

- Set up SSH connection between controller and target nodes:

```shell
# 1. Generating new SSH key
ssh-keygen -t ed25519 -C "email@example.com"
# 2. Adding SSH key to ssh-agent
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
# 3. Copying SSH key to target nodes
ssh-copy-id -i ~/.ssh/id_ed25519.pub <username>@<target-node-ip>
```

- Add target nodes to `inventory.yml` file:

```yml
---
vm:
  hosts:
    vm01:
      ansible_host: 192.168.0.x
      ansible_python_interpreter: /usr/bin/python3
      ansible_become_user: root
      ansible_become_password: "{{ become_password }}"
      username: vdt01
      hostname: vdt01

local:
  hosts:
    localhost:
      ansible_connection: local
      ansible_python_interpreter: /usr/bin/python3
      ansible_become_user: root
      ansible_become_password: "{{ become_password }}"
      username: duc
      hostname: duc

all:
  children:
    vm:
    local:

```

- Here, passwords are encrypted using `ansible-vault` and stored in `group_vars/vault.yml`:

```shell
$ ansible-vault create group_vars/vault.yml
---
vault_become_password: <secret_password>
```

- Load passwords in vault to `group_vars/vars.yml`:

```yml
---
become_password: "{{ vault_become_password }}"
```

- I can enter vault authentication password using `--ask-vault-pass` option at runtime:

```shell
$ ansible-playbook -i inventory.yml site.yml --ask-vault-pass
Vault password: ...
```

## 3. Setting up docker using role `common`

- Hello

## 4. Splitting application into 3 roles: `web`, `api` and `db`

## 5. Conclusion

## 6. References

[1] [Ansible in 100 Seconds](https://youtu.be/xRMPKQweySE)

[2] [Keep vaulted variables safely visible](https://docs.ansible.com/ansible/latest/tips_tricks/ansible_tips_tricks.html#keep-vaulted-variables-safely-visible)
