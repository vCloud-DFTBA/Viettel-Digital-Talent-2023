## Deploy your application in the docker-compose homework using ansible:
1. Setup docker for your target environments in role “common”
2. Split your application into 3 roles: “web”, “api” and “db”


## Create NFS server for sharing data between containers
1. Overview
We will use 10GB disk to create NFS server for sharing data between containers. **`/dev/sda`**
    <div align="center">
        <img src="./assets/nfs_disk.png" width="1000" />
    </div>
2. Install **`nfs-kernel-server`** package
    ```bash
    sudo apt update
    sudo apt install nfs-kernel-server
    ```
3. Create directory for sharing data
    ```bash
    sudo mkdir -p /mnt/nfs_volume/docker_nfs_share
    ```
4. Change ownership of the directory to nobody user
    ```bash
    sudo chown nobody:nogroup /mnt/nfs_volume/docker_nfs_share
    ```
5. Export the directory
    ```bash
    sudo vi /etc/exports
    ```
    Add the following line to the file
    ```bash
    /mnt/nfs_volume/docker_nfs_share    *(rw,sync,no_subtree_check,no_root_squash,no_all_squash,insecure)
    ```
    - **`rw`**: Allow both read and write requests on the NFS volume.
    - **`sync`**: Reply to requests only after the changes have been committed to stable storage.
    - **`no_subtree_check`**: Disable subtree checking. When a shared directory is the subdirectory of a larger file system, nfs performs scans of every directory above it, in order to verify its permissions and details. Disabling the subtree check may increase the reliability of NFS, but reduce security.
    - **`no_root_squash`**: Enable root squashing. This prevents root users connected remotely from having root privileges and assigns them the user ID for the user nfsnobody.
    - **`no_all_squash`**: Enable all squashing. This option is the converse of no_root_squash and makes root users on the client machine appear as root users on the NFS server. This option is generally used for diskless clients.
    - **`insecure`**: This option allows the NFS server to respond to requests from unprivileged ports (ports greater than 1024). This option is useful for mounting NFS volumes from older clients such as NFS version 3.
6. Restart the NFS server
    ```bash
    sudo systemctl restart nfs-kernel-server
    ```
docker volume create --driver local \
--opt type=nfs \
--opt o=addr=10.114.0.2,rw \
--opt device=:/mnt/nfs_volume/docker_nfs_share \
nfs_volume

docker run -d \
--mount type=volume,src=nfs_volume,dst=/usr/share/nginx/html,volume-driver=local,volume-opt=type=nfs,volume-opt=o=addr=10.114.0.2,volume-opt=device=:/mnt/nfs_volume/docker_nfs_share \
nginx
