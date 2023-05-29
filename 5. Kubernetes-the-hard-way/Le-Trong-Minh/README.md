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
## VirtualBox

Download and Install [VirtualBox](https://www.virtualbox.org/wiki/Downloads).

## Vagrant

Vagrant provides an easier way to deploy multiple virtual machines on VirtualBox more consistently.

Download and Install [Vagrant](https://www.vagrantup.com/) on our platform.

## The project defaults

The project have been configured with the following networking defaults.

```bash
vagrant destroy -f
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




