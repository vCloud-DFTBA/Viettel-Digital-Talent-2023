SET NAMES utf8;

CREATE TABLE IF NOT EXISTS attendee (
    id INT NOT NULL AUTO_INCREMENT,
    major VARCHAR(255),
    name VARCHAR(255),
    school VARCHAR(255),
    sex VARCHAR(10),
    year_of_bth INT,
    PRIMARY KEY (id)
) DEFAULT CHARSET=utf8;

INSERT INTO attendee (id, major, name, school, sex, year_of_bth) VALUES (1, 'Công nghệ thông tin', 'Bùi Minh Sơn', 'Đại học Công nghệ - Đại học Quốc gia Hà Nội', 'Nam', 2002);
INSERT INTO attendee (id, major, name, school, sex, year_of_bth) VALUES (2, 'Điện tử viễn thông', 'Đào Đại Hiệp', 'Đại học Bách khoa Hà Nội', 'Nam', 2001);
INSERT INTO attendee (id, major, name, school, sex, year_of_bth) VALUES (3, 'Mạng máy tính và truyền thông dữ liệu', 'Đỗ Anh Tú', 'Đại học Công nghệ - Đại học Quốc gia Hà Nội', 'Nam', 2002);
INSERT INTO attendee (id, major, name, school, sex, year_of_bth) VALUES (4, 'An toàn thông tin', 'Đỗ Bảo Hoàng', 'Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga', 'Nam', 1997);
INSERT INTO attendee (id, major, name, school, sex, year_of_bth) VALUES (5, 'NULL', 'Hoàng Quốc Doanh', 'Đại Học Bách Khoa Hà Nội', 'Nam', 2001);
INSERT INTO attendee (id, major, name, school, sex, year_of_bth) VALUES (6, 'Công nghệ thông tin ứng dụng phần mềm', 'Le Minh Duc', 'Đại Học Bách Khoa Hà Nội', 'Nam', 2002);
INSERT INTO attendee (id, major, name, school, sex, year_of_bth) VALUES (7, 'Kỹ thuật điện tử viễn thông', 'Lê Phúc Lai', 'Đại Học Bách Khoa Hà Nội', 'Nam', 2002);
INSERT INTO attendee (id, major, name, school, sex, year_of_bth) VALUES (8, 'An toàn thông tin', 'Lê Quang Anh', 'Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga', 'Nam', 1997);
INSERT INTO attendee (id, major, name, school, sex, year_of_bth) VALUES (9, 'Kỹ thuật điều khiển và tự động hóa', 'Lê Trọng Minh', 'Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga', 'Nam', 2000);
INSERT INTO attendee (id, major, name, school, sex, year_of_bth) VALUES (10, 'Khoa học máy tính', 'Lê Tùng Lâm', 'Đại Học Bách Khoa Hà Nội', 'Nam', 1999);
INSERT INTO attendee (id, major, name, school, sex, year_of_bth) VALUES (11, 'Kỹ thuật hàng không vũ trụ', 'Lê Văn Chiến', 'Đại học Công nghệ - Đại học Quốc gia Hà Nội', 'Nam', 2002);
INSERT INTO attendee (id, major, name, school, sex, year_of_bth) VALUES (12, 'ICT', 'Linh Thi Nguyen', 'Đại Học Bách Khoa Hà Nội', 'Nữ', 2002);
INSERT INTO attendee (id, major, name, school, sex, year_of_bth) VALUES (13, 'Khoa học máy tính', 'Nguyễn Đại An', 'Đại Học Bách Khoa Hà Nội', 'Nam', 2023);
INSERT INTO attendee (id, major, name, school, sex, year_of_bth) VALUES (14, 'Công nghệ thông tin ứng dụng phần mềm', 'Nguyễn Đình Hoàng', 'Đại học Công nghệ - Đại học Quốc gia Hà Nội', 'Nam', 2002);
INSERT INTO attendee (id, major, name, school, sex, year_of_bth) VALUES (15, 'NULL', 'Nguyen Duc Vinh Data', 'Học viện Công nghệ Bưu chính Viễn thông', 'Nam', 2002);
INSERT INTO attendee (id, major, name, school, sex, year_of_bth) VALUES (16, 'Công nghệ thông tin ứng dụng phần mềm', 'Nguyễn Dương Long', 'ĐH Thuỷ lợi', 'Nam', 2002);
INSERT INTO attendee (id, major, name, school, sex, year_of_bth) VALUES (17, 'Khoa học máy tính', 'Nguyen Huu Thang', 'Đại Học Bách Khoa Hà Nội', 'Nam', 2000);
INSERT INTO attendee (id, major, name, school, sex, year_of_bth) VALUES (18, 'Điện tử', 'Nguyễn Mạnh Cường', 'Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga', 'Nam', 1997);
INSERT INTO attendee (id, major, name, school, sex, year_of_bth) VALUES (19, 'An toàn thông tin', 'Nguyễn Mạnh Đức', 'Học viện Kỹ thuật mật mã', 'Nam', 2002);
INSERT INTO attendee (id, major, name, school, sex, year_of_bth) VALUES (20, 'NULL', 'Nguyễn Ngọc Chung', 'Học viên Công nghệ Bưu chính Viễn Thông HCM', 'Nam', 2002);
INSERT INTO attendee (id, major, name, school, sex, year_of_bth) VALUES (21, 'An toàn thông tin', 'Nguyễn Tuấn Anh', 'Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga', 'Nam', 1997);
INSERT INTO attendee (id, major, name, school, sex, year_of_bth) VALUES (22, 'An toàn thông tin', 'Nguyễn Văn Quang', 'Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga', 'Nam', 1997);
INSERT INTO attendee (id, major, name, school, sex, year_of_bth) VALUES (23, 'An toàn thông tin', 'Ninh Chí Hướng', 'Học viện Công nghệ Bưu chính viễn thông', 'Nam', 2002);
INSERT INTO attendee (id, major, name, school, sex, year_of_bth) VALUES (24, 'Khoa học máy tính', 'Ninh Văn Nghĩa', 'Đại Học Bách Khoa Hà Nội', 'Nam', 2001);
INSERT INTO attendee (id, major, name, school, sex, year_of_bth) VALUES (25, 'Toán ứng dụng và tin học', 'Phạm Anh Đức', 'Đại học Bách Khoa Hà Nội', 'Nam', 2001);
INSERT INTO attendee (id, major, name, school, sex, year_of_bth) VALUES (26, 'Công nghệ điện tử', 'Phạm Duy Cương', 'Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga', 'Nam', 1997);
INSERT INTO attendee (id, major, name, school, sex, year_of_bth) VALUES (27, 'Phát triển phần mềm', 'Phạm Hồng Thanh', 'Swinburne University', 'Nam', 1998);
INSERT INTO attendee (id, major, name, school, sex, year_of_bth) VALUES (28, 'Mạng máy tính và truyền thông dữ liệu', 'Phạm Thị Khánh Linh', 'Đại học Công nghệ - Đại học Quốc gia Hà Nội', 'Nữ', 2002);
INSERT INTO attendee (id, major, name, school, sex, year_of_bth) VALUES (29, 'Công nghệ thông tin ứng dụng phần mềm', 'Phạm Văn Tới', 'Học viện Công nghệ Bưu chính viễn thông', 'Nam', 2002);
INSERT INTO attendee (id, major, name, school, sex, year_of_bth) VALUES (30, 'Bảo mật thông tin', 'Trần Đức Mạnh', 'Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga', 'Nam', 1998);
INSERT INTO attendee (id, major, name, school, sex, year_of_bth) VALUES (31, 'Điện tử viễn thông', 'Trần Mạnh Dũng', 'Học viện Công nghệ Bưu chính Viễn thông', 'Nam', 2001);
INSERT INTO attendee (id, major, name, school, sex, year_of_bth) VALUES (32, 'Mạng máy tính và truyền thông dữ liệu', 'Trần Minh Dương', 'Đại học Công nghệ - Đại học Quốc gia Hà Nội', 'Nam', 2002);
INSERT INTO attendee (id, major, name, school, sex, year_of_bth) VALUES (33, 'Khoa học máy tính', 'Trần Xuân Phú', 'Trường Đại học Công nghệ thông tin - ĐHQG Tp.Hồ chí Minh', 'Nam', 2001);
INSERT INTO attendee (id, major, name, school, sex, year_of_bth) VALUES (34, 'Khoa học máy tính', 'Vũ Hoàng Long', 'Đại học Bách Khoa Hà Nội', 'Nam', 2001);
INSERT INTO attendee (id, major, name, school, sex, year_of_bth) VALUES (35, 'Kỹ thuật phần mềm', 'Vũ Minh Hiếu', 'Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga', 'Nam', 2000);

