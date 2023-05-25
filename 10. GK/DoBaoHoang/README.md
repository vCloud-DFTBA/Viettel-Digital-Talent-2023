# VDT 2023 Midterm Project

## Phát triển 3-tier Webapp đầy đủ

### **1. Phát triển ứng dụng web**

Mã nguồn được lưu trong thư mục [source](https://github.com/hoang97/Viettel-Digital-Talent-2023/tree/mid_term/10.%20GK/DoBaoHoang/source)

### **2. Triển khai sử dụng các DevOps tools**

**2.1 Containerization**

File Docker cho từng dịch vụ được lưu trong từng thư mục của [source](https://github.com/hoang97/Viettel-Digital-Talent-2023/tree/mid_term/10.%20GK/DoBaoHoang/source)

Docker history của image web:

<div align="center">
  <img width="500" src="images/history_web.png">
</div>

<div align="center">
  <i>Pic. 1 - Web image docker history</i>
</div>

Docker history của image api:


<div align="center">
  <img width="500" src="images/history_api.png">
</div>

<div align="center">
  <i>Pic. 2 - API image docker history</i>
</div>

Docker history của image database:


<div align="center">
  <img width="500" src="images/history_db.png">
</div>

<div align="center">
  <i>Pic. 3 - Database image docker history</i>
</div>

**2.2 Continous Integration**

File setup CI trên github - [Test API](https://github.com/hoang97/Viettel-Digital-Talent-2023/blob/mid_term/.github/workflows/test_api.yaml)

`Luồng CI`: kiểm tra xem có thay đổi nào trong thư mục "10. GK/DoBaoHoang" không? -> nếu có mới thực hiện build mock database và test API 

Hình ảnh demo:


<div align="center">
  <img width="500" src="images/unittest_api.png">
</div>

<div align="center">
  <i>Pic. 4 - Output log của luồng CI</i>
</div>

### **3. Continuos Delivery**

<div align="center">
  <img width="500" src="images/system_architecture.png">
</div>

<div align="center">
  <i>Pic. 5 - Ảnh minh họa kiến trúc hệ thống</i>
</div>

<div align="center">
  <img width="500" src="images/CD_architecture.png">
</div>

<div align="center">
  <i>Pic. 6 - Ảnh minh họa CD pipeline</i>
</div>


File setup CD trên github - [Build and Publish](https://github.com/hoang97/Viettel-Digital-Talent-2023/blob/mid_term/.github/workflows/build_push_images.yaml)

<div align="center">
  <img width="500" src="images/build_release_image.png">
</div>

<div align="center">
  <i>Pic. 7 - Output log của luồng CD Github</i>
</div>


<div align="center">
  <img width="500" src="images/ansible_log.png">
</div>

<div align="center">
  <i>Pic. 8 - Output log của ansible</i>
</div>


<div align="center">
  <img width="500" src="images/web_1.png">
</div>

<div align="center">
  <i>Pic. 9 - Demo Webapp ha</i>
</div>


<div align="center">
  <img width="500" src="images/web_2.png">
</div>

<div align="center">
  <i>Pic. 10 - Demo Webapp ha</i>
</div>

### **4. Monitoring**

Thư mục Role Monitor chứa playbook cài đặt Node-exporter: [Monitor](https://github.com/hoang97/Viettel-Digital-Talent-2023/tree/mid_term/10.%20GK/DoBaoHoang/roles/monitor)

Thư mục Role Prometheus chứa playbook cài đặt máy chủ prometheus local: [Prometheus](https://github.com/hoang97/Viettel-Digital-Talent-2023/tree/mid_term/10.%20GK/DoBaoHoang/roles/prometheus)

Thư mục chứa File config Prometheus: [Prom config](https://github.com/hoang97/Viettel-Digital-Talent-2023/tree/mid_term/10.%20GK/DoBaoHoang/roles/prometheus)


<div align="center">
  <img width="500" src="images/prometheus.png">
</div>

<div align="center">
  <i>Pic. 11 - Dashboard giám sát node tại hệ thống tập trung</i>
</div>


### **5. Logging**

Thư mục Role Logging chưa playbook triển khai dịch vụ collect log: [Logging](https://github.com/hoang97/Viettel-Digital-Talent-2023/tree/mid_term/10.%20GK/DoBaoHoang/roles/logging)

Do máy chủ Kibana tập trung đã tắt nên chỉ có ảnh chụp demo service fluentd tập trung tại remote host:



<div align="center">
  <img width="500" src="images/datacenter.png">
</div>

<div align="center">
  <i>Pic. 12 - Demo Fluentd container</i>
</div>

<div align="center">
  <img width="500" src="images/fluentd_service.png">
</div>

<div align="center">
  <i>Pic. 13 - Demo Fluentd service</i>
</div>


<div align="center">
  <img width="500" src="images/web_create.png">
</div>

<div align="center">
  <i>Pic. 14 - Demo Webapp create</i>
</div>


<div align="center">
  <img width="500" src="images/web_edit.png">
</div>

<div align="center">
  <i>Pic. 15 - Demo Webapp edit</i>
</div>


<div align="center">
  <img width="500" src="images/web_delete.png">
</div>

<div align="center">
  <i>Pic. 16 - Demo Webapp delete</i>
</div>