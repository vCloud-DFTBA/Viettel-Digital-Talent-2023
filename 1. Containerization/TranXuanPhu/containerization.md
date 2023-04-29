# Bài tập 
**Đề bài**: Nêu lên sự khác nhau giữa:
- ARG và ENV
- COPY và ADD
- CMD và ENTRYPOINT

## ARG và ENV
- **`ARG`** được dùng để truyền biến vào Docker vào giai đoạn build và sẽ không được lưu vào image.
- **`ENV`** mặc khác set các biến environment, lưu vào image và có thể được sử dụng bởi các process trong container.

## COPY và ADD
Cả hai lệnh đều được dùng để copy files từ host vào trong Docker Container, tuy nhiên vẫn có một số điểm khác biệt:
- **`COPY`**: `<src>` có thể là file hoặc folder ở trên host, trong khi `<des>` là địa chỉ mà file hoặc folder được copy vào bên trong Docker Image.
- **`ADD`** về cơ bản giống **`COPY`** nhưng sẽ có thêm một số chức năng như `<src>` có thể là URL hay có thể giải nén các định dạng file thông dụng như `.zip`, `.tar`, `.gz`, etc.

## CMD và ENTRYPOINT
Tuy cả hai lệnh đều được sử dụng để set default command khi build Docker Image, nhưng vẫn có một số điểm khác biệt:
- Lệnh được định nghĩa trong **`CMD`** có thể được ghi đè bằng cách truyền lệnh/tham số vào lệnh `docker run`. Và nếu có nhiều instruction **`CMD`** trong Dockerfile, chỉ có lệnh **`CMD`** cuối cùng được thực thi.
- Mặt khác, **ENTRYPOINT**, tham số được truyền vào lệnh `docker run` sẽ được xem như tham số cho **ENTRYPOINT**.