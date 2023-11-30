# Hướng dẫn sử dụng ansible playbook để triển khai các thành phần hệ thống
Vào thư mục root của project, và nhập lệnh sau:
```commandline
ansible-playbook -i inventories/inventory.yaml setup.yaml --ask-vault-pass
```
Mật khẩu sử dụng để access ansible-vault là `phutx`

Sau khi tất cả dịch vụ đều sẵn sàng, tiến hành vào trang [`http://localhost:80`](http://localhost:80). Nếu thành công hệ thống sẽ trả về trang chủ danh sách sinh viên tham gia VDT 2023 lĩnh vực cloud.