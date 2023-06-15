CREATE TABLE IF NOT EXISTS attendee
(
    id          bigint       not null
        primary key,
    major       varchar(255) null,
    name        varchar(255) null,
    school      varchar(255) null,
    sex         varchar(255) null,
    username    varchar(255) null,
    year_of_bth bigint       null
)


-- Insert dữ liệu
INSERT INTO attendee (name, username, year_of_bth, sex, school, major) VALUES
  ('Bùi Minh Sơn', 'sonbm', 2002, 'Nam', 'Đại học Công nghệ - Đại học Quốc gia Hà Nội', 'Công nghệ thông tin'),
  ('Đào Đại Hiệp', 'hiepdd', 2001, 'Nam', 'Đại học Bách khoa Hà Nội', 'Điện tử viễn thông'),
  ('Đỗ Anh Tú', 'tuda', 2002, 'Nam', 'Đại học Công nghệ - Đại học Quốc gia Hà Nội', 'Mạng máy tính và truyền thông dữ liệu'),
  ('Đỗ Bảo Hoàng', 'hoangdb', 1997, 'Nam', 'Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga', 'An toàn thông tin'),
  ('Hoàng Quốc Doanh', 'doanhhq', 2001, 'Nam', 'Đại Học Bách Khoa Hà Nội', NULL),
  ('Le Minh Duc', 'duclm', 2002, 'Nam', 'Đại Học Bách Khoa Hà Nội', 'Công nghệ thông tin ứng dụng phần mềm'),
  ('Lê Phúc Lai', 'lailp', 2002, 'Nam', 'Đại Học Bách Khoa Hà Nội', 'Kỹ thuật điện tử viễn thông'),
  ('Lê Quang Anh', 'anhlq', 1997, 'Nam', 'Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga', 'An toàn thông tin'),
  ('Lê Trọng Minh', 'minhlt', 2000, 'Nam', 'Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga', 'Kỹ thuật điều khiển và tự động hóa'),
  ('Lê Tùng Lâm', 'lamlt', 1999, 'Nam', 'Đại Học Bách Khoa Hà Nội', 'Khoa học máy tính'),
  ('Lê Văn Chiến', 'chienlv', 2002, 'Nam', 'Đại học Công nghệ - Đại học Quốc gia Hà Nội', 'Kỹ thuật hàng không vũ trụ'),
  ('Linh Thi Nguyen', 'linhnt', 2002, 'Nữ', 'Đại Học Bách Khoa Hà Nội', 'ICT'),
  ('Nguyễn Đại An', 'annd', 2023, 'Nam', 'Đại Học Bách Khoa Hà Nội', 'Khoa học máy tính'),
  ('Nguyễn Đình Hoàng', 'hoangnd', 2002, 'Nam', 'Đại học Công nghệ - Đại học Quốc gia Hà Nội', 'Công nghệ thông tin ứng dụng phần mềm'),
  ('Nguyen Duc Vinh Data', 'vinhnd', 2002, 'Nam', 'Học viện Công nghệ Bưu chính Viễn thông', NULL),
  ('Nguyễn Dương Long', 'longnd', 2002, 'Nam', 'ĐH Thuỷ lợi', 'Công nghệ thông tin ứng dụng phần mềm'),
  ('Nguyen Huu Thang', 'thangnh', 2000, 'Nam', 'Đại Học Bách Khoa Hà Nội', 'Khoa học máy tính'),
  ('Nguyễn Mạnh Cường', 'cuongnm', 1997, 'Nam', 'Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga', 'Điện tử'),
  ('Nguyễn Mạnh Đức', 'ducnm', 2002, 'Nam', 'Học viện Kỹ thuật mật mã', 'An toàn thông tin'),
  ('Nguyễn Ngọc Chung', 'chungnn', 2002, 'Nam', 'Học viên Công nghệ Bưu chính Viễn Thông HCM', NULL),
  ('Nguyễn Tuấn Anh', 'anhnt', 1997, 'Nam', 'Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga', 'An toàn thông tin'),
  ('Nguyễn Văn Quang', 'quangnv', 1997, 'Nam', 'Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga', 'An toàn thông tin'),
  ('Ninh Chí Hướng', 'huongnc', 2002, 'Nam', 'Học viện Công nghệ Bưu chính viễn thông', 'An toàn thông tin'),
  ('Ninh Văn Nghĩa', 'nghianv', 2001, 'Nam', 'Đại Học Bách Khoa Hà Nội', 'Khoa học máy tính'),
  ('Phạm Anh Đức', 'ducpa', 2001, 'Nam', 'Đại học Bách Khoa Hà Nội', 'Toán ứng dụng và tin học'),
  ('Phạm Duy Cương', 'cuongpd', 1997, 'Nam', 'Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga', 'Công nghệ điện tử'),
  ('Phạm Hồng Thanh', 'thanhph', 1998, 'Nam', 'Swinburne University', 'Phát triển phần mềm'),
  ('Phạm Thị Khánh Linh', 'linhptk', 2002, 'Nữ', 'Đại học Công nghệ - Đại học Quốc gia Hà Nội', 'Mạng máy tính và truyền thông dữ liệu'),
  ('Phạm Văn Tới', 'toipv', 2002, 'Nam', 'Học viện Công nghệ Bưu chính viễn thông', 'Công nghệ thông tin ứng dụng phần mềm'),
  ('Trần Đức Mạnh', 'manhtd', 1998, 'Nam', 'Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga', 'Bảo mật thông tin'),
  ('Trần Mạnh Dũng', 'dungtm', 2001, 'Nam', 'Học viện Công nghệ Bưu chính Viễn thông', 'Điện tử viễn thông'),
  ('Trần Minh Dương', 'duongtm', 2002, 'Nam', 'Đại học Công nghệ - Đại học Quốc gia Hà Nội', 'Mạng máy tính và truyền thông dữ liệu'),
  ('Trần Xuân Phú', 'phutx', 2001, 'Nam', 'Trường Đại học Công nghệ thông tin - ĐHQG Tp.Hồ Chí Minh', 'Khoa học máy tính'),
  ('Vũ Hoàng Long', 'longvh', 2001, 'Nam', 'Đại học Bách Khoa Hà Nội', 'Khoa học máy tính'),
  ('Vũ Minh Hiếu', 'hieuvm', 2000, 'Nam', 'Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga', 'Kỹ thuật phần mềm');