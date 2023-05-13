# Ansible

## _Deploy your application in the docker-compose homework using ansible:_

-   ### Setup docker for your target environments in role “common”
-   ### Split your application into 3 roles: “web”, “api” and “db”

---

# **Table of Contents:**

## [I. What is Ansible ?](#WhatIsAnsible)

-   ### [1. Infrastructure as Code](#IaC)
-   ### [2. Ansible](#ansible)

## [II. Deploy application using ansible](#Deploy)

-   ### [1. Install ansible](#install)
-   ### [2. Using ansible to deploy common role](#common)
-   ### [3. Using ansible to deploy mongodb role](#mongodb)
-   ### [4. Using ansible to deploy backend role](#backend)
-   ### [5. Using ansible to deploy frontend role](#frontend)
-   ### [6. Using ansible to deploy nginx role](#nginx)
-   ### [7. Using ansible to deploy all roles](#all)

## [III. References](#Re)

---

<a name="WhatIsAnsible"></a>

# **I. What is Ansible ?**:

<a name="IaC"></a>

### 1. Infrastructure as Code

Infrastructure as Code (IaC) is a method of managing IT infrastructure using code to automate the deployment and management process. This means that components of the infrastructure, including servers, networks, storage, and other resources, are described using code and automatically deployed using source code management tools such as Git or CVS.

The goal of IaC is to create a continuous software development cycle (CI/CD) for rapidly deploying infrastructure, meeting the needs of modern applications, and reducing reliance on manual processes and personnel.

IaC has many benefits, including:

-   Automating the deployment and management of infrastructure, reducing time and errors in the deployment process.
-   Providing reusability, allowing reuse of infrastructure patterns already built to create new systems.
-   Providing fast recovery capability, allowing for quick recovery of running infrastructure in case of an incident.
-   Reducing reliance on manual processes and personnel, increasing consistency and reducing the likelihood of errors.

Tools commonly used to implement IaC include Ansible, Puppet, Chef, Terraform, and CloudFormation. These tools allow developers and administrators to describe their infrastructure using configuration files or code, creating templates similar to source code, and automatically deploying those infrastructure resources on different platforms, from servers to cloud computing and web services.

<a name="ansible"></a>

### 2. Ansible

<img src="https://www.freecodecamp.org/news/content/images/2021/09/ansble.png">

Ansible is an open-source configuration management and deployment tool developed by Ansible, Inc. and released under the Apache license. It is capable of automating tasks such as system installation and configuration, application deployment, system updates, and other management tasks.

Ansible uses a distributed system model and does not require any special software to be installed on the target nodes. Instead, Ansible uses SSH to access target nodes and perform tasks.

Tasks are performed using Ansible "modules", Python code that performs specific tasks. Ansible provides over 1000 different modules and can be extended to support specific tasks.

Ansible also has the ability to manage configuration files, called "playbooks". Playbooks are simple YAML files that describe tasks and the desired state of the system that Ansible needs to achieve. Playbooks can be used to create complex deployment workflows and can be shared and reused.

In summary, Ansible is a powerful, simple, and easy-to-use configuration management and deployment tool that can meet the demands of complex systems and is popular in server and cloud computing environments.

<a name="Deploy"></a>

# **II. Deploy application using ansible**:

<a name="install"></a>

### 1. Install ansible

-   Install ansible

```
sudo apt install ansible
```

<img src= images/install_ansible.png>

<a name="common"></a>

### 2. Using ansible to deploy common role

```
sudo ansible-playbook -i inventories/inventory.yml playbook-docker.yml
```

<img src= images/docker_run.png>

<a name="mongodb"></a>

### 3. Using ansible to deploy mongodb role

```
sudo ansible-playbook -i inventories/inventory.yml playbook-mongodb.yml
```

<img src= images/mongodb_run.png>

<a name="backend"></a>

### 4. Using ansible to deploy backend role

```
sudo ansible-playbook -i inventories/inventory.yml playbook-backend.yml
```

<img src= images/backend_run.png>

<a name="frontend"></a>

### 5. Using ansible to deploy frontend role

```
sudo ansible-playbook -i inventories/inventory.yml playbook-frontend.yml
```

<img src= images/frontend_run.png>

<a name="nginx"></a>

### 6. Using ansible to deploy nginx role

```
sudo ansible-playbook -i inventories/inventory.yml playbook-nginx.yml
```

<img src= images/nginx_run.png>

<a name="all"></a>

### 7. Using ansible to deploy all roles

```
sudo ansible-playbook -i inventories/inventory.yml playbook-aio.yml
```

<img src= images/aio.png>
