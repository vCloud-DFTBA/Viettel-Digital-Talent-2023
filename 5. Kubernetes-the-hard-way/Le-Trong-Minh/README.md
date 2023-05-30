> This tutorial is a modified version of the original developed by [Kelsey Hightower](https://github.com/kelseyhightower/kubernetes-the-hard-way).

# Table of contents:



# Kubernetes The Hard Way On VirtualBox

This project walks us through setting up Kubernetes-the-hard-way on a local machine using VirtualBox.


Please note that with this particular challenge, it is all about the minute detail. If you miss one tiny step anywhere along the way, it's going to break!

Always run the `cert_verify` script at the places it suggests, and always ensure you are on the correct node when you do stuff. If `cert_verify` shows anything in red, then you have made an error in a previous step. For the master node checks, run the check on `master-1` and on `master-2`


## Cluster Details

Kubernetes The Hard Way guides you through bootstrapping a highly available Kubernetes cluster with end-to-end encryption between components and RBAC authentication.

* [Kubernetes](https://github.com/kubernetes/kubernetes) 1.24.3
* [Container Runtime](https://github.com/containerd/containerd) 1.5.9
* [CNI Container Networking](https://github.com/containernetworking/cni) 0.8.6
* [Weave Networking](https://www.weave.works/docs/net/latest/kubernetes/kube-addon/)
* [etcd](https://github.com/coreos/etcd) v3.5.3
* [CoreDNS](https://github.com/coredns/coredns) v1.9.4

### Node configuration

We will be building the following:

* Two control plane nodes (`master-1` and `master-2`) running the control plane components as operating system services.
* Two worker nodes (`worker-1` and `worker-2`)
* One loadbalancer VM running HAProxy to balance requests between the two API servers.

## Labs

* [Prerequisites](docs/01-prerequisites.md)
* [Provisioning Compute Resources](docs/02-compute-resources.md)
* [Installing the Client Tools](docs/03-client-tools.md)
* [Provisioning the CA and Generating TLS Certificates](docs/04-certificate-authority.md)
* [Generating Kubernetes Configuration Files for Authentication](docs/05-kubernetes-configuration-files.md)
* [Generating the Data Encryption Config and Key](docs/06-data-encryption-keys.md)
* [Bootstrapping the etcd Cluster](docs/07-bootstrapping-etcd.md)
* [Bootstrapping the Kubernetes Control Plane](docs/08-bootstrapping-kubernetes-controllers.md)
* [Installing CRI on Worker Nodes](docs/09-install-cri-workers.md)
* [Bootstrapping the Kubernetes Worker Nodes](docs/10-bootstrapping-kubernetes-workers.md)
* [TLS Bootstrapping the Kubernetes Worker Nodes](docs/11-tls-bootstrapping-kubernetes-workers.md)
* [Configuring kubectl for Remote Access](docs/12-configuring-kubectl.md)
* [Deploy Weave - Pod Networking Solution](docs/13-configure-pod-networking.md)
* [Kube API Server to Kubelet Configuration](docs/14-kube-apiserver-to-kubelet.md)
* [Deploying the DNS Cluster Add-on](docs/15-dns-addon.md)
* [Smoke Test](docs/16-smoke-test.md)
* [E2E Test](docs/17-e2e-tests.md)
* [Extra - Certificate Verification](docs/verify-certificates.md)


# 1. Prerequisites

## VM hardware Requirements
6 GB of RAM (Preferably 16 GB)
50 GB Disk space
## VirtualBox

Download and Install [VirtualBox](https://www.virtualbox.org/wiki/Downloads).

## Vagrant

Vagrant provides an easier way to deploy multiple virtual machines on VirtualBox more consistently.

Download and Install [Vagrant](https://www.vagrantup.com/) on our platform.

## The project defaults

The project have been configured with the following networking defaults.

```bash
# stop and terminate use off all resources
vagrant destroy -f 

# create and configure guest machine according to vagrant file
vagrant up
```

### VM network

The networks used by the VirtualBox VM is `192.168.56.0/24`.

### Pod Network

The network used to assign IP addresses to pods is `10.244.0.0/16` - this is default in K8s.

### Service Network

The network used to assign IP addresses to Cluster IP is `10.96.0.0/16`.


# 2. Provisioning Resources

CD into vagrant directory

```bash
cd Viettel-Digital-Talent-2023/5. Kubernetes-the-hard-way/Le-Trong-Minh/vagrant

vagrant up
```
![](images/1.2%20vagrant-up.png)



- Deploys 5 VMs - 2 Master, 2 Worker and 1 Loadbalancer with the name 'kubernetes-ha-* '

- Set's IP addresses in the range 192.168.56

    | VM            |  VM Name               | Purpose       | IP            | Forwarded Port   | RAM  |
    | ------------  | ---------------------- |:-------------:| -------------:| ----------------:|-----:|
    | master-1      | kubernetes-ha-master-1 | Master        | 192.168.56.11 |     2711         | 2048 |
    | master-2      | kubernetes-ha-master-2 | Master        | 192.168.56.12 |     2712         | 1024 |
    | worker-1      | kubernetes-ha-worker-1 | Worker        | 192.168.56.21 |     2721         | 512  |
    | worker-2      | kubernetes-ha-worker-2 | Worker        | 192.168.56.22 |     2722         | 1024 |
    | loadbalancer  | kubernetes-ha-lb       | LoadBalancer  | 192.168.56.30 |     2730         | 1024 |

- Add's a DNS entry to each of the nodes to access internet
    > DNS: 8.8.8.8

# 3. Installing the Client Tools

## Access all VMs

Here we create an SSH key pair for the `vagrant` user who we are logged in as. We will copy the public key of this pair to the other master and both workers to permit us to use password-less SSH (and SCP) go get from `master-1` to these other nodes in the context of the `vagrant` user which exists on all nodes.

Generate Key Pair on `master-1` node

```bash
ssh-keygen
```

Leave all settings to default.

View the generated public key ID at:

```bash
cat ~/.ssh/id_rsa.pub
```
Add this key to the local authorized_keys (`master-1`) as in some commands we scp to ourself

```bash
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
```

Copy the output and form it into the following command:

```bash
cat >> ~/.ssh/authorized_keys <<EOF
<public-key>
EOF
```


![](images/3.%20access%20via%20ssh%20from%20master-1.png)


Now ssh to each of the other nodes and paste the above at each command prompt.


## Install kubectl

```bash
wget https://storage.googleapis.com/kubernetes-release/release/v1.24.3/bin/linux/amd64/kubectl
chmod +x kubectl
sudo mv kubectl /usr/local/bin/
```

### Verification

Verify `kubectl` version 1.24.3 or higher is installed:

```
kubectl version -o yaml
```

![](images/3.%20install%20kubectl.png)


# 4. Provisioning a CA and Generating TLS Certificates


In this lab you will provision a [PKI Infrastructure](https://en.wikipedia.org/wiki/Public_key_infrastructure) using the popular openssl tool, then use it to bootstrap a Certificate Authority, and generate TLS certificates for the following components: etcd, kube-apiserver, kube-controller-manager, kube-scheduler, kubelet, and kube-proxy.


On `master-1`

## Certificate Authority

Set up environment variables.

```bash
MASTER_1=$(dig +short master-1)
MASTER_2=$(dig +short master-2)
LOADBALANCER=$(dig +short loadbalancer)
```

Compute cluster internal API server service address, which is always .1 in the service CIDR range. This is also required as a SAN in the API server certificate:

```bash
SERVICE_CIDR=10.96.0.0/24
API_SERVICE=$(echo $SERVICE_CIDR | awk 'BEGIN {FS="."} ; { printf("%s.%s.%s.1", $1, $2, $3) }')
```

Check that the environment variables are set:

```bash
echo $MASTER_1
echo $MASTER_2
echo $LOADBALANCER
echo $SERVICE_CIDR
echo $API_SERVICE
```

![](images/4.1%20certificate_authority.png)

Create a CA certificate, then generate a Certificate Signing Request and use it to create a private key:


```bash
{
  # Create private key for CA
  openssl genrsa -out ca.key 2048

  # Comment line starting with RANDFILE in /etc/ssl/openssl.cnf definition to avoid permission issues
  sudo sed -i '0,/RANDFILE/{s/RANDFILE/\#&/}' /etc/ssl/openssl.cnf

  # Create CSR using the private key
  openssl req -new -key ca.key -subj "/CN=KUBERNETES-CA/O=Kubernetes" -out ca.csr

  # Self sign the csr using its own private key
  openssl x509 -req -in ca.csr -signkey ca.key -CAcreateserial  -out ca.crt -days 1000
}
```

![](images/4.2.png)

## Client and Server Certificates
### The Admin Client Certificate

Generate the `admin` client certificate and private key:

```bash
{
  # Generate private key for admin user
  openssl genrsa -out admin.key 2048

  # Generate CSR for admin user. Note the OU.
  openssl req -new -key admin.key -subj "/CN=admin/O=system:masters" -out admin.csr

  # Sign certificate for admin user using CA servers private key
  openssl x509 -req -in admin.csr -CA ca.crt -CAkey ca.key -CAcreateserial  -out admin.crt -days 1000
}
```

![](images/4.3.png)


### The Kubelet Client Certificates
### The Controller Manager Client Certificate

Generate the `kube-controller-manager` client certificate and private key:

```bash
{
  openssl genrsa -out kube-controller-manager.key 2048

  openssl req -new -key kube-controller-manager.key \
    -subj "/CN=system:kube-controller-manager/O=system:kube-controller-manager" -out kube-controller-manager.csr

  openssl x509 -req -in kube-controller-manager.csr \
    -CA ca.crt -CAkey ca.key -CAcreateserial -out kube-controller-manager.crt -days 1000
}
```

![](images/4.4.png)
### The Kube Proxy Client Certificate

Generate the `kube-proxy` client certificate and private key:


```bash
{
  openssl genrsa -out kube-proxy.key 2048

  openssl req -new -key kube-proxy.key \
    -subj "/CN=system:kube-proxy/O=system:node-proxier" -out kube-proxy.csr

  openssl x509 -req -in kube-proxy.csr \
    -CA ca.crt -CAkey ca.key -CAcreateserial  -out kube-proxy.crt -days 1000
}
```

![](images/4.5%20.png)


### The Scheduler Client Certificate

Generate the `kube-scheduler` client certificate and private key:



```bash
{
  openssl genrsa -out kube-scheduler.key 2048

  openssl req -new -key kube-scheduler.key \
    -subj "/CN=system:kube-scheduler/O=system:kube-scheduler" -out kube-scheduler.csr

  openssl x509 -req -in kube-scheduler.csr -CA ca.crt -CAkey ca.key -CAcreateserial  -out kube-scheduler.crt -days 1000
}
```



### The Kubernetes API Server Certificate
```bash
cat > openssl.cnf <<EOF
[req]
req_extensions = v3_req
distinguished_name = req_distinguished_name
[req_distinguished_name]
[v3_req]
basicConstraints = critical, CA:FALSE
keyUsage = critical, nonRepudiation, digitalSignature, keyEncipherment
extendedKeyUsage = serverAuth
subjectAltName = @alt_names
[alt_names]
DNS.1 = kubernetes
DNS.2 = kubernetes.default
DNS.3 = kubernetes.default.svc
DNS.4 = kubernetes.default.svc.cluster
DNS.5 = kubernetes.default.svc.cluster.local
IP.1 = ${API_SERVICE}
IP.2 = ${MASTER_1}
IP.3 = ${MASTER_2}
IP.4 = ${LOADBALANCER}
IP.5 = 127.0.0.1
EOF
```

Generate certs for kube-apiserver

```bash
{
  openssl genrsa -out kube-apiserver.key 2048

  openssl req -new -key kube-apiserver.key \
    -subj "/CN=kube-apiserver/O=Kubernetes" -out kube-apiserver.csr -config openssl.cnf

  openssl x509 -req -in kube-apiserver.csr \
  -CA ca.crt -CAkey ca.key -CAcreateserial  -out kube-apiserver.crt -extensions v3_req -extfile openssl.cnf -days 1000
}
```

![](images/4.7%20The%20Kubernetes%20API%20Server%20Certificate.png)

# The Kubelet Client Certificate

This certificate is for the api server to authenticate with the kubelets when it requests information from them

```bash
cat > openssl-kubelet.cnf <<EOF
[req]
req_extensions = v3_req
distinguished_name = req_distinguished_name
[req_distinguished_name]
[v3_req]
basicConstraints = critical, CA:FALSE
keyUsage = critical, nonRepudiation, digitalSignature, keyEncipherment
extendedKeyUsage = clientAuth
EOF
```

Generate certs for kubelet authentication

```bash
{
  openssl genrsa -out apiserver-kubelet-client.key 2048

  openssl req -new -key apiserver-kubelet-client.key \
    -subj "/CN=kube-apiserver-kubelet-client/O=system:masters" -out apiserver-kubelet-client.csr -config openssl-kubelet.cnf

  openssl x509 -req -in apiserver-kubelet-client.csr \
  -CA ca.crt -CAkey ca.key -CAcreateserial  -out apiserver-kubelet-client.crt -extensions v3_req -extfile openssl-kubelet.cnf -days 1000
}
```

![](images/4.8%20client-cert.png)

### The ETCD Server Certificate

Similarly ETCD server certificate must have addresses of all the servers part of the ETCD cluster

The `openssl` command cannot take alternate names as command line parameter. So we must create a `conf` file for it:

```bash
cat > openssl-etcd.cnf <<EOF
[req]
req_extensions = v3_req
distinguished_name = req_distinguished_name
[req_distinguished_name]
[ v3_req ]
basicConstraints = CA:FALSE
keyUsage = nonRepudiation, digitalSignature, keyEncipherment
subjectAltName = @alt_names
[alt_names]
IP.1 = ${MASTER_1}
IP.2 = ${MASTER_2}
IP.3 = 127.0.0.1
EOF
```

Generates certs for ETCD

```bash
{
  openssl genrsa -out etcd-server.key 2048

  openssl req -new -key etcd-server.key \
    -subj "/CN=etcd-server/O=Kubernetes" -out etcd-server.csr -config openssl-etcd.cnf

  openssl x509 -req -in etcd-server.csr \
    -CA ca.crt -CAkey ca.key -CAcreateserial  -out etcd-server.crt -extensions v3_req -extfile openssl-etcd.cnf -days 1000
}
```

![](images/4.9%20etcd-server-cert.png)

## The Service Account Key Pair

The Kubernetes Controller Manager leverages a key pair to generate and sign service account tokens as describe in the [managing service accounts](https://kubernetes.io/docs/admin/service-accounts-admin/) documentation.

Generate the `service-account` certificate and private key:

```bash
{
  openssl genrsa -out service-account.key 2048

  openssl req -new -key service-account.key \
    -subj "/CN=service-accounts/O=Kubernetes" -out service-account.csr

  openssl x509 -req -in service-account.csr \
    -CA ca.crt -CAkey ca.key -CAcreateserial  -out service-account.crt -days 1000
}
```

![](images/4.10%20account%20keypair.png)


## Verify the PKI

![](images/4.11%20check-1.png)


## Distribute the Certificates

Copy the appropriate certificates and private keys to each instance:

```bash
{
for instance in master-1 master-2; do
  scp ca.crt ca.key kube-apiserver.key kube-apiserver.crt \
    apiserver-kubelet-client.crt apiserver-kubelet-client.key \
    service-account.key service-account.crt \
    etcd-server.key etcd-server.crt \
    kube-controller-manager.key kube-controller-manager.crt \
    kube-scheduler.key kube-scheduler.crt \
    ${instance}:~/
done

for instance in worker-1 worker-2 ; do
  scp ca.crt kube-proxy.crt kube-proxy.key ${instance}:~/
done
}
```

![](images/4.12%20distribute%20the%20certs.png)
![](images/4.13%20check-2.png)


# 5. Generating Kubernetes Configuration Files for Authentication














