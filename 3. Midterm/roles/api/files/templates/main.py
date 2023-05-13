



data = """db.internees.insertMany([
{'id': '1', 'name': 'Bùi Minh Sơn', 'birth': '2002', 'sex': 'Nam', 'university': 'Đại học Công nghệ - Đại học Quốc gia Hà Nội', 'major': 'Công nghệ thông tin'},
{'id': '2', 'name': 'Đào Đại Hiệp', 'birth': '2001', 'sex': 'Nam', 'university': 'Đại học Bách khoa Hà Nội', 'major': 'Điện tử viễn thông'},
{'id': '3', 'name': 'Đỗ Anh Tú', 'birth': '2002', 'sex': 'Nam', 'university': 'Đại học Công nghệ - Đại học Quốc gia Hà Nội', 'major': 'Mạng máy tính và truyền thông dữ liệu'},
{'id': '4', 'name': 'Đỗ Bảo Hoàng', 'birth': '1997', 'sex': 'Nam', 'university': 'Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga', 'major': 'An toàn thông tin'},
{'id': '5', 'name': 'Hoàng Quốc Doanh', 'birth': '2001', 'sex': 'Nam', 'university': 'Đại Học Bách Khoa Hà Nội', 'major': 'None'},
{'id': '6', 'name': 'Le Minh Duc', 'birth': '2002', 'sex': 'Nam', 'university': 'Đại Học Bách Khoa Hà Nội', 'major': 'Công nghệ thông tin ứng dụng phần mềm'},
{'id': '7', 'name': 'Lê Phúc Lai', 'birth': '2002', 'sex': 'Nam', 'university': 'Đại Học Bách Khoa Hà Nội', 'major': 'Kỹ thuật điện tử viễn thông'},
{'id': '8', 'name': 'Lê Quang Anh', 'birth': '1997', 'sex': 'Nam', 'university': 'Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga', 'major': 'An toàn thông tin'},
{'id': '9', 'name': 'Lê Trọng Minh', 'birth': '2000', 'sex': 'Nam', 'university': 'Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga', 'major': 'Kỹ thuật điều khiển và tự động hóa'},
{'id': '10', 'name': 'Lê Tùng Lâm', 'birth': '1999', 'sex': 'Nam', 'university': 'Đại Học Bách Khoa Hà Nội', 'major': 'Khoa học máy tính'},
{'id': '11', 'name': 'Lê Văn Chiến', 'birth': '2002', 'sex': 'Nam', 'university': 'Đại học Công nghệ - Đại học Quốc gia Hà Nội', 'major': 'Kỹ thuật hàng không vũ trụ'},
{'id': '12', 'name': 'Linh Thi Nguyen', 'birth': '2002', 'sex': 'Nữ', 'university': 'Đại Học Bách Khoa Hà Nội', 'major': 'ICT'},
{'id': '13', 'name': 'Nguyễn Đại An', 'birth': '2023', 'sex': 'Nam', 'university': 'Đại Học Bách Khoa Hà Nội', 'major': 'Khoa học máy tính'},
{'id': '14', 'name': 'Nguyễn Đình Hoàng', 'birth': '2002', 'sex': 'Nam', 'university': 'Đại học Công nghệ - Đại học Quốc gia Hà Nội', 'major': 'Công nghệ thông tin ứng dụng phần mềm'},
{'id': '15', 'name': 'Nguyen Duc Vinh Data', 'birth': '2002', 'sex': 'Nam', 'university': 'Học viện Công nghệ Bưu chính Viễn thông', 'major': 'None'},
{'id': '16', 'name': 'Nguyễn Dương Long', 'birth': '2002', 'sex': 'Nam', 'university': 'ĐH Thuỷ lợi', 'major': 'Công nghệ thông tin ứng dụng phần mềm'},
{'id': '17', 'name': 'Nguyen Huu Thang', 'birth': '2000', 'sex': 'Nam', 'university': 'Đại Học Bách Khoa Hà Nội', 'major': 'Khoa học máy tính'},
{'id': '18', 'name': 'Nguyễn Mạnh Cường', 'birth': '1997', 'sex': 'Nam', 'university': 'Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga', 'major': 'Điện tử'},
{'id': '19', 'name': 'Nguyễn Mạnh Đức', 'birth': '2002', 'sex': 'Nam', 'university': 'Học viện Kỹ thuật mật mã', 'major': 'An toàn thông tin'},
{'id': '20', 'name': 'Nguyễn Ngọc Chung', 'birth': '2002', 'sex': 'Nam', 'university': 'Học viên Công nghệ Bưu chính Viễn Thông HCM', 'major': 'None'},
{'id': '21', 'name': 'Nguyễn Tuấn Anh', 'birth': '1997', 'sex': 'Nam', 'university': 'Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga', 'major': 'An toàn thông tin'},
{'id': '22', 'name': 'Nguyễn Văn Quang', 'birth': '1997', 'sex': 'Nam', 'university': 'Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga', 'major': 'An toàn thông tin'},
{'id': '23', 'name': 'Ninh Chí Hướng', 'birth': '2002', 'sex': 'Nam', 'university': 'Học viện Công nghệ Bưu chính viễn thông', 'major': 'An toàn thông tin'},
{'id': '24', 'name': 'Ninh Văn Nghĩa', 'birth': '2001', 'sex': 'Nam', 'university': 'Đại Học Bách Khoa Hà Nội', 'major': 'Khoa học máy tính'},
{'id': '25', 'name': 'Phạm Anh Đức', 'birth': '2001', 'sex': 'Nam', 'university': 'Đại học Bách Khoa Hà Nội', 'major': 'Toán ứng dụng và tin học'},
{'id': '26', 'name': 'Phạm Duy Cương', 'birth': '1997', 'sex': 'Nam', 'university': 'Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga', 'major': 'Công nghệ điện tử'},
{'id': '27', 'name': 'Phạm Hồng Thanh', 'birth': '1998', 'sex': 'Nam', 'university': 'Swinburne University', 'major': 'Phát triển phần mềm'},
{'id': '28', 'name': 'Phạm Thị Khánh Linh', 'birth': '2002', 'sex': 'Nữ', 'university': 'Đại học Công nghệ - Đại học Quốc gia Hà Nội', 'major': 'Mạng máy tính và truyền thông dữ liệu'},
{'id': '29', 'name': 'Phạm Văn Tới', 'birth': '2002', 'sex': 'Nam', 'university': 'Học viện Công nghệ Bưu chính viễn thông', 'major': 'Công nghệ thông tin ứng dụng phần mềm'},
{'id': '30', 'name': 'Trần Đức Mạnh', 'birth': '1998', 'sex': 'Nam', 'university': 'Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga', 'major': 'Bảo mật thông tin'},
{'id': '31', 'name': 'Trần Mạnh Dũng', 'birth': '2001', 'sex': 'Nam', 'university': 'Học viện Công nghệ Bưu chính Viễn thông', 'major': 'Điện tử viễn thông'},
{'id': '32', 'name': 'Trần Minh Dương', 'birth': '2002', 'sex': 'Nam', 'university': 'Đại học Công nghệ - Đại học Quốc gia Hà Nội', 'major': 'Mạng máy tính và truyền thông dữ liệu'},
{'id': '33', 'name': 'Trần Xuân Phú', 'birth': '2001', 'sex': 'Nam', 'university': 'Trường Đại học Công nghệ thông tin - ĐHQG Tp.Hồ chí Minh', 'major': 'Khoa học máy tính'},
{'id': '34', 'name': 'Vũ Hoàng Long', 'birth': '2001', 'sex': 'Nam', 'university': 'Đại học Bách Khoa Hà Nội', 'major': 'Khoa học máy tính'},
{'id': '35', 'name': 'Vũ Minh Hiếu', 'birth': '2000', 'sex': 'Nam', 'university': 'Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga', 'major': 'Kỹ thuật phần mềm'}
])"""

data0 = data.replace("id","STT")
data1 = data0.replace("name", "name")
data2=data1.replace("birth", "year")
data3 = data2.replace("sex", "gender")
data4 = data3.replace("university", "school")
data5 = data4.replace("major", "major")

print(data5)


