# Ansible Assignment

> Deploy application in the docker-compose homework using ansible:
>
> - Setup docker for your target environments in role “common”
> - Split your application into 3 roles: “web”, “api” and “db”

To deploy on multiple hosts, I use 2 VMs with following IPs:

- 198.19.249.24
- 198.19.249.113

Additionally, I take advantage of `docker compose` in the previous assignment to build images and run 3 containers which are mongodb, api, and web with [`be-compose.yaml`](), [`fe-compose.yaml`](), and [`db-compose.yaml`]().

## Ansible

### 1. Setup

#### a. Inventory

[`inventory.yaml`](): automates tasks on managed nodes or “hosts” in the infrastructure, using a list or group of lists.

```yaml
webapp:
  hosts:
    localhost:
      ansible_connection: local
      ansible_become_user: kilinh

    Kilinh-Node1:
      ansible_host: 198.19.249.24

    Kilinh-Node2:
      ansible_host: 198.19.249.113

  vars:
    ansible_user: kilinh
    ansible_ssh_private_key_file: /home/kilinh/.ssh/id_rsa
    ansible_python_interpreter: /usr/bin/python3
    ansible_become: true
    ansible_become_method: sudo
```

#### b. Roles

- [common](https://github.com/khanhlinhh/Viettel-Digital-Talent-2023/blob/ansible-lab/2.%20Ansible/PhamThiKhanhLinh/roles/common/tasks/main.yaml): Set up environment such as installing Docker, Docker Compose Plugin, etc.
- [db](https://github.com/khanhlinhh/Viettel-Digital-Talent-2023/blob/ansible-lab/2.%20Ansible/PhamThiKhanhLinh/roles/db/tasks/main.yaml): Pull MongoDB image and run container using `docker compose`.
- [api](https://github.com/khanhlinhh/Viettel-Digital-Talent-2023/blob/ansible-lab/2.%20Ansible/PhamThiKhanhLinh/roles/api/tasks/main.yaml): Build Python Back-End image and run container using `docker compose`.
- [web](https://github.com/khanhlinhh/Viettel-Digital-Talent-2023/blob/ansible-lab/2.%20Ansible/PhamThiKhanhLinh/roles/web/tasks/main.yaml): Build Front-End image and run container using `docker compose`.

### 2. Deployment

Run `ansible-playbook`:

```
ansible-playbook -i inventory.yaml site.yaml --ask-vault-pass -K
```

After entering the password, all tasks will be executed.
![Ansible Logs](./images/ansible-logs.png)

Testing on the browser:

From localhost
![Localhost Test](./images/localhost-test.png)

From VM with 198.19.249.24 IP Address
![Kilinh-Node1 Test](./images/kilinh-node1-test.png)

From VM with 198.19.249.113 IP Address
![Kilinh-Node2 Test](images/kilinh-node2-test.png)
