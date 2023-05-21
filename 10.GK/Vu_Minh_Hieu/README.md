# Project giữa kỳ

## I. Phát triển một 3-tier web application đơn giản

### Yêu cầu:

-   #### Viết một CRUD web application đơn giản thực hiện các chức năng:
    -   Liệt kê danh sách sinh viên tham gia khóa đào tạo chương trình VDT 2023 lĩnh vực cloud dưới dạng bảng, cho phép xem chi tiết/thêm/xóa/cập nhật thông tin sinh viên
    -   Solution:
        <img src= images/react.png>
        <img src= images/fastapi_docs.png>
-   #### Thiết kế hệ thống với ba dịch vụ:

    -   web: Giao diện web viết bằng HTML + CSS + Javascript được triển khai trên nền web server nginx
        -   source : [react](./frontend/)
    -   api: RESTful API viết bằng ngôn ngữ lập trình tùy chọn (prefer Python), có đầy đủ các chức năng: list, get, create, update, delete các bản ghi thông tin sinh viên

        -   source : [fastapi](./backend/)

    -   db: Database SQL hoặc NoSQL lưu trữ thông tin sinh viên (dữ liệu khởi tạo của DB này được cho bởi bảng trong Phụ lục I.)
        -   done
    -   Viết unit tests cho các chức năng APIs
        -   source : [unit-test](./backend/test_main.py)
    -   <strike>\*Viết unit tests cho các chức năng giao diện, viết integration tests</strike>

## II. Triển khai web application sử dụng các DevOps tools & practices

### 1. Containerization

Yêu cầu:

-   Viết Dockerfile để đóng gói các dịch vụ trên thành các container image
-   Yêu cầu image đảm bảo tối ưu thời gian build và kích thước chiếm dụng, khuyến khích sử dụng các thủ thuật build image đã được giới thiệu (layer-caching, optimized RUN instructions, multi-stage build, etc.)

Output:

-   File Dockerfile cho từng dịch vụ kế hệ thống với ba dịch vụ:
    -   backend : [fastapi](./backend/Dockerfile)
    -   frontend : [react](./frontend/Dockerfile)
    -   docker-compose : [docker-compose.yml](./docker-compose.yml)
-   Output câu lệnh build và thông tin docker history của từng image:
    -   output build : [output](./logs/output_docker_compose.log)
    -   mongodb images history : [mongodb](./logs/mongo_history.log)
    -   fastapi image history : [fastapi_history](./logs/fastapi_history.log)
    -   react image history : [react_history](./logs/react_history.log)

### 2. Continuous Integration

Yêu cầu:

-   Tự động chạy unit test khi tạo PR vào branch main
-   Tự động chạy unit test khi push commit lên một branch
    Output:
-   File setup công cụ CI
    -   source : [ci file](../../.github/workflows/ci_cd.yaml)
-   Output log của luồng CI
    <img src= images/actions.png>
    <img src= images/ci_cd_1.png>
    <img src= images/run_unit_test.png>
-   Các hình ảnh demo khác
    <img src= images/github_actions.png>

### 3. Continuous Delivery

Yêu cầu:

-   Viết luồng release dịch vụ bằng công cụ CI/CD của GitHub/GitLab, thực hiện build docker image và push docker image lên Docker Hub khi có event một tag mới được developer tạo ra trên GitHub
-   Viết ansible playbook thực hiện các nhiệm vụ:

    -   Setup môi trường: Cài đặt docker trên các node triển khai dịch vụ
    -   Deploy các dịch vụ theo version sử dụng docker
    -   <strike>\*Triển khai các dịch vụ trên nhiều hosts khác nhau</strike>

-   Đảm bảo tính HA cho các dịch vụ web và api:
    -   Mỗi dịch vụ web và api được triển khai trên ít nhất 02 container khác nhau
    -   Requests đến các endpoint web và api được cân bằng tải thông qua các công cụ load balancer, ví dụ: nginx, haproxy và traefik
    -   \*Các công cụ load balancer cũng được triển khai theo mô hình cluster
    -   <strike>\*Triển khai db dưới dạng cluster</strike>

Output:

-   Ảnh minh họa kiến trúc triển khai và bản mô tả
    <img src= images/cluster_architecture.jpg>
-   Thư mục chứa ansible playbook dùng để triển khai dịch vụ, trong thư mục này cần có :
    -   File inventory chứa danh sách các hosts triển khai
        -   source : [invenroty.yml](./ansible/inventories/inventory.yml)
    -   Các file playbook
        -   source : [invenroty.yml](./ansible)
    -   Thư mục roles chứa các role :
        -   common: Setup môi trường trước deploy (done)
        -   web: Triển khai dịch vụ web (done)
        -   api: Triển khai dịch vụ api (done)
        -   db: Triển khai dịch vụ db (done)
        -   lb: Triển khai dịch vụ load balancing (done)
-   File setup CD
    -   source : [ci-cd file](../../.github/workflows/ci_cd.yaml)
-   Output của luồng build và push Docker Image lên Docker Hub
    <img src= images/push_to_docker_hub.png>
-   Hướng dẫn sử dụng ansible playbook để triển khai các thành phần hệ thống

```
cd Viettel-Digital-Talent-2023/10.GK/Vu_Minh_Hieu/ansible
sudo ansible-playbook -i invenroty/inventory.yml playbook-aio.yml
```

-   Output log triển khai hệ thống
    -   source : [logs](./logs/)

### 4. Monitoring

Yêu cầu:

-   Viết ansible playbook roles monitor thực hiện các nhiệm vụ:
    -   Cài đặt các dịch vụ node exporter và cadvisor dưới dạng container
    -   Đẩy thông số giám sát lên hệ thống giám sát Prometheus tập trung
    -   Chú ý: Tên các container có tiền tố là <username>\_ để phân biệt thông số giám sát dịch vụ của các sinh viên trên hệ thống giám sát tập trung. Thông tin <username> của từng sinh viên cho bởi bảng trong Phụ lục I.

Output:

-   Role monitor chứa các playbook và cấu hình giám sát cho hệ thống
    -   source : [moniroring](./ansible/roles/monitoring/)
-   Ảnh chụp dashboard giám sát nodes & containers, có thể sử dụng hệ thống prometheus tập trung ở 171.236.38.100:9090
    <img src= images/prometheus.png>

### 5. Logging

Yêu cầu:

-   Viết ansible playbook thực hiện các nhiệm vụ:
    -   Cài đặt dịch vụ logstash hoặc fluentd để collect log từ các dịch vụ web, api và db
    -   Đẩy log dịch vụ lên hệ thống Elasticsearch tập trung 171.236.38.100:9200
    -   Log phải đảm bảo có ít nhất các thông tin: IP truy cập, thời gian, action tác động, kết quả (thành công/không thành công/status code)
    -   Log được index với tiền tố <username>\_ để phân biệt log dịch vụ của các sinh viên khác nhau. Thông tin <username> của từng sinh viên cho bởi bảng trong Phụ lục I.

Output:

-   Ansible playbook triển khai các dịch vụ collect log (tách module logging)
    -   source : [moniroring](./ansible/roles/logging/)
-   Ảnh chụp sample log từ Kibana 171.236.38.100:5601
    <img src= images/elastic.png>
