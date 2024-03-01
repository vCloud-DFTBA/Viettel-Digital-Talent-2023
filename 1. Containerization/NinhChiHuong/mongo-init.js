db.createUser(
    {
        user: 'apiuser',
        pwd: 'apipassword',
        roles: [
            {
                role: 'readWrite',
                db: 'student-db'
            }]
    })

db.createCollection('student');

db.student.insertMany([
{ sid : 1, full_name : "Bùi Minh Sơn", year_of_birth : 2002, university : "Đại học Công nghệ - Đại học Quốc gia Hà Nội", major : "Công nghệ thông tin" },
{ sid : 2, full_name : "Đào Đại Hiệp", year_of_birth : 2001, university : "Đại học Bách khoa Hà Nội", major : "Khoa học máy tính" },
{ sid : 3, full_name : "Đỗ Anh Tú", year_of_birth : 2002, university : "Đại học Công nghệ - Đại học Quốc gia Hà Nội", major : "Khoa học máy tính" },
{ sid : 4, full_name : "Đỗ Bảo Hoàng", year_of_birth : 1997, university : "Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga", major : "ĐTVT" },
{ sid : 5, full_name : "Hoàng Quốc Doanh", year_of_birth : 2001, university : "ĐH Bách khoa Hà Nội", major : "NULL" },
{ sid : 6, full_name : "Le Minh Duc", year_of_birth : 2002, university : "Đại học Bách khoa Hà Nội", major : "Công nghệ thông tin ứng dụng phần mềm" },
{ sid : 7, full_name : "Lê Phúc Lai", year_of_birth : 2002, university : "ĐH Bách khoa Hà Nội", major : "Khoa học máy tính" },
{ sid : 8, full_name : "Lê Quang Anh", year_of_birth : 1997, university : "Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga", major : "Truyền thông và mạng máy tính" },
{ sid : 9, full_name : "Lê Trọng Minh", year_of_birth : 2000, university : "Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga", major : "Khoa học máy tính" },
{ sid : 10, full_name : "Lê Tùng Lâm", year_of_birth : 1999, university : "ĐH Bách khoa Hà Nội", major : "Công nghệ thông tin Global ICT" },
{ sid : 11, full_name : "Lê Văn Chiến", year_of_birth : 2002, university : "Đại học Công nghệ - Đại học Quốc gia Hà Nội", major : "Kỹ thuật viễn thông" },
{ sid : 12, full_name : "Linh Thi Nguyen", year_of_birth : 2002, university : "Đại học Bách khoa Hà Nội", major : "ICT" },
{ sid : 13, full_name : "Nguyễn Đại An", year_of_birth : 2023, university : "ĐH Bách khoa Hà Nội", major : "Khoa học máy tính" },
{ sid : 14, full_name : "Nguyễn Đình Hoàng", year_of_birth : 2002, university : "Đại học Công nghệ - Đại học Quốc gia Hà Nội", major : "Kỹ thuật Cơ điện tử" },
{ sid : 15, full_name : "Nguyen Duc Vinh", year_of_birth : 2002, university : "Học viện Công nghệ Bưu chính Viễn thông", major : "NULL" },
{ sid : 16, full_name : "Nguyễn Dương Long", year_of_birth : 2002, university : "ĐH Thuỷ lợi", major : "ĐTVT" },
{ sid : 17, full_name : "Nguyen Huu Thang", year_of_birth : 2000, university : "Đại học Bách khoa Hà Nội", major : "Khoa học máy tính" },
{ sid : 18, full_name : "Nguyễn Mạnh Cường", year_of_birth : 1997, university : "Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga", major : "ATTT" },
{ sid : 19, full_name : "Nguyễn Mạnh Đức", year_of_birth : 2002, university : "Học viện Kỹ thuật mật mã", major : "An toàn thông tin" },
{ sid : 20, full_name : "Nguyễn Ngọc Chung", year_of_birth : 2002, university : "Học viên Công nghệ Bưu chính Viễn Thông HCM", major : "NULL" },
{ sid : 21, full_name : "Nguyễn Tuấn Anh", year_of_birth : 1997, university : "Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga", major : "An toàn thông tin" },
{ sid : 22, full_name : "Nguyễn Văn Quang", year_of_birth : 1997, university : "Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga", major : "An toàn thông tin" },
{ sid : 23, full_name : "Ninh Chí Hướng", year_of_birth : 2002, university : "Học viện Công nghệ Bưu chính Viễn thông", major : "An toàn thông tin" },
{ sid : 24, full_name : "Ninh Văn Nghĩa", year_of_birth : 2001, university : "ĐH Bách khoa Hà Nội", major : "Kỹ thuật Cơ điện tử" },
{ sid : 25, full_name : "Phạm Anh Đức", year_of_birth : 2001, university : "ĐH Bách khoa Hà Nội", major : "Toán ứng dụng và tin học" },
{ sid : 26, full_name : "Phạm Duy Cương", year_of_birth : 1997, university : "Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga", major : "ĐTVT" },
{ sid : 27, full_name : "Phạm Hồng Thanh", year_of_birth : 1998, university : "Swinburne University", major : "ATTT" },
{ sid : 28, full_name : "Phạm Thị Khánh Linh", year_of_birth : 2002, university : "Đại học Công nghệ - Đại học Quốc gia Hà Nội", major : "Mạng máy tính và truyền thông dữ liệu" },
{ sid : 29, full_name : "Phạm Văn Tới", year_of_birth : 2002, university : "Học viện Công nghệ Bưu chính Viễn thông", major : "Mạng máy tính và truyền thông dữ liệu" },
{ sid : 30, full_name : "Trần Đức Mạnh", year_of_birth : 1998, university : "Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga", major : "Hệ thống thông tin" },
{ sid : 31, full_name : "Trần Mạnh Dũng", year_of_birth : 2001, university : "Học viện Công nghệ Bưu chính Viễn thông", major : "Kỹ thuật thông tin và truyền thông" },
{ sid : 32, full_name : "Trần Minh Dương", year_of_birth : 2002, university : "Đại học Công nghệ - Đại học Quốc gia Hà Nội", major : "Mạng máy tính và truyền thông dữ liệu" },
{ sid : 33, full_name : "Trần Xuân Phú", year_of_birth : 2001, university : "university Đại học Công nghệ thông tin - ĐHQG Tp.Hồ chí Minh", major : "Khoa học máy tính" },
{ sid : 34, full_name : "Vũ Hoàng Long", year_of_birth : 2001, university : "ĐH Bách khoa Hà Nội", major : "Khoa học máy tính" },
{ sid : 35, full_name : "Vũ Minh Hiếu", year_of_birth : 2000, university : "Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga", major : "Kỹ thuật phần mềm" },
]);
