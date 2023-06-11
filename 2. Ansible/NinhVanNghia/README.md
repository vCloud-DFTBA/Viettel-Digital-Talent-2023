# Tổng quan hệ thống

![alt text](https://github.com/nghianinhnb/Viettel-Digital-Talent-2023/tree/Ansible/2.%20Ansible/NinhVanNghia/image/Over%20view.jpg)

# Khởi tạo cụm máy chủ ảo

<h2>Chạy lệnh: docer compose up</h2>
</br>

![alt text](https://github.com/nghianinhnb/Viettel-Digital-Talent-2023/tree/Ansible/2.%20Ansible/NinhVanNghia/image/1%20Environment.png)

# Chạy

<h2>Truy cập localhost:7681 vào terminal của coordinator được cài đặt ansible</h2>
<h2>Chạy các lệnh:</h2>
<h3>cd /vdt/ansible</h3>
<h3>ansible-playbook -i inventory.yaml playbook.yaml --extra-vars "@vars.yaml"</h3>
</br>

<p>playbook.yaml</p>

![playbook](https://github.com/nghianinhnb/Viettel-Digital-Talent-2023/tree/Ansible/2.%20Ansible/NinhVanNghia/image/PlayBook.png)

<p>inventory.yaml</p>

![Inventory](https://github.com/nghianinhnb/Viettel-Digital-Talent-2023/tree/Ansible/2.%20Ansible/NinhVanNghia/image/Inventory.png)

<p>vars.yaml</p>

![Inventory](https://github.com/nghianinhnb/Viettel-Digital-Talent-2023/tree/Ansible/2.%20Ansible/NinhVanNghia/image/vars.png)

<p>Role commom</p>

![Role commom](https://github.com/nghianinhnb/Viettel-Digital-Talent-2023/tree/Ansible/2.%20Ansible/NinhVanNghia/image/role%20install%20docker.png)

<p>Role builder</p>

![Role builder](https://github.com/nghianinhnb/Viettel-Digital-Talent-2023/tree/Ansible/2.%20Ansible/NinhVanNghia/image/role%20build%20image.png)

# Kết quả
![alt text](https://github.com/nghianinhnb/Viettel-Digital-Talent-2023/tree/Ansible/2.%20Ansible/NinhVanNghia/image/2%20Install%20docker.png)
![alt text](https://github.com/nghianinhnb/Viettel-Digital-Talent-2023/tree/Ansible/2.%20Ansible/NinhVanNghia/image/3%20Build.png)
![alt text](https://github.com/nghianinhnb/Viettel-Digital-Talent-2023/tree/Ansible/2.%20Ansible/NinhVanNghia/image/4%20Run%20container.png)
![alt text](https://github.com/nghianinhnb/Viettel-Digital-Talent-2023/tree/Ansible/2.%20Ansible/NinhVanNghia/image/5%20Result.png)
