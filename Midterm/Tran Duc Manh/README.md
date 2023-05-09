### Install docker via Ansible 
What need to be done?
- Check if there are any users to add to the `docker` group: user `docker`.
- Reset ssh connection to apply user changes.
- Load OS-specific vars.
- Ensure old versions of Docker are not installed.
- Ensure dependencies are installed.
- Ensure additional dependencies are installed (on Ubuntu < 20.04 and any other systems).
- Ensure additional dependencies are installed (on Ubuntu >= 20.04).
- Add Docker apt key.
- Ensure curl is present (on older systems without SNI).
- Add Docker apt key (alternative for older systems without SNI).
- Add Docker repository.
- Install Docker packages (with downgrade option).
- Install docker-compose plugin.
- Install docker-compose-plugin (with downgrade option).
- Ensure /etc/docker/ directory exists.
- Configure Docker daemon options.
- Ensure Docker is started and enabled at boot.
- restart docker
- Check current docker-compose version.


```
ansible-playbook -i ./inventories/local.yml playbook-docker.yml  >> docker.run
```
You can see the log in the `docker.run` file

### Install 3-tier application via Ansible
#### Nginx
Install community docker module
```
ansible-galaxy collection install community.docker
``
Run the playbook
```
ansible-playbook -i ./inventories/local.yml playbook-nginx.yml  >> nginx.run

```
ansible-playbook -i ./inventories/local.yml playbooks/logstash.yml  >> logs/logstash.run

ansible-playbook -i ./inventories/local.yml playbooks/monitor.yml  >> logs/monitor.run

apt install python3-virtualenv
sudo apt-get install python3.10-distutils

virtualenv -p /usr/bin/python3.10 /root/py310
source /root/py310/bin/activate