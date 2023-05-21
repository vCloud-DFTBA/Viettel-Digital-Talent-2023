db = new Mongo().getDB("data");
db.createCollection("users",{ capped: false })
db.users.insert(
    [
        {
          "No": 1,
          "Name": "Bùi Minh Sơn",
          "Birthyear": 2002,
          "Gender": "Nam",
          "University": "Đại học Công nghệ - Đại học Quốc gia Hà Nội",
          "Major": "Công nghệ thông tin"
        },
        {
          "No": 2,
          "Name": "Đào Đại Hiệp",
          "Birthyear": 2001,
          "Gender": "Nam",
          "University": "Đại học Bách khoa Hà Nội",
          "Major": "Điện tử viễn thông"
        },
        {
          "No": 3,
          "Name": "Đỗ Anh Tú",
          "Birthyear": 2002,
          "Gender": "Nam",
          "University": "Đại học Công nghệ - Đại học Quốc gia Hà Nội",
          "Major": "Mạng máy tính và truyền thông dữ liệu"
        },
        {
          "No": 4,
          "Name": "Đỗ Bảo Hoàng",
          "Birthyear": 1997,
          "Gender": "Nam",
          "University": "Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga",
          "Major": "An toàn thông tin"
        },
        {
          "No": 5,
          "Name": "Hoàng Quốc Doanh",
          "Birthyear": 2001,
          "Gender": "Nam",
          "University": "Đại Học Bách Khoa Hà Nội",
          "Major": null
        },
        {
          "No": 6,
          "Name": "Le Minh Duc",
          "Birthyear": 2002,
          "Gender": "Nam",
          "University": "Đại Học Bách Khoa Hà Nội",
          "Major": "Công nghệ thông tin ứng dụng phần mềm"
        },
        {
          "No": 7,
          "Name": "Lê Phúc Lai",
          "Birthyear": 2002,
          "Gender": "Nam",
          "University": "Đại Học Bách Khoa Hà Nội",
          "Major": "Kỹ thuật điện tử viễn thông"
        },
        {
          "No": 8,
          "Name": "Lê Quang Anh",
          "Birthyear": 1997,
          "Gender": "Nam",
          "University": "Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga",
          "Major": "An toàn thông tin"
        },
        {
          "No": 9,
          "Name": "Lê Trọng Minh",
          "Birthyear": 2000,
          "Gender": "Nam",
          "University": "Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga",
          "Major": "Kỹ thuật điều khiển và tự động hóa"
        },
        {
          "No": 10,
          "Name": "Lê Tùng Lâm",
          "Birthyear": 1999,
          "Gender": "Nam",
          "University": "Đại Học Bách Khoa Hà Nội",
          "Major": "Khoa học máy tính"
        },
        {
          "No": 11,
          "Name": "Lê Văn Chiến",
          "Birthyear": 2002,
          "Gender": "Nam",
          "University": "Đại học Công nghệ - Đại học Quốc gia Hà Nội",
          "Major": "Kỹ thuật hàng không vũ trụ"
        },
        {
          "No": 12,
          "Name": "Linh Thi Nguyen",
          "Birthyear": 2002,
          "Gender": "Nữ",
          "University": "Đại Học Bách Khoa Hà Nội",
          "Major": "ICT"
        },
        {
          "No": 13,
          "Name": "Nguyễn Đại An",
          "Birthyear": 2023,
          "Gender": "Nam",
          "University": "Đại Học Bách Khoa Hà Nội",
          "Major": "Khoa học máy tính"
        },
        {
          "No": 14,
          "Name": "Nguyễn Đình Hoàng",
          "Birthyear": 2002,
          "Gender": "Nam",
          "University": "Đại học Công nghệ - Đại học Quốc gia Hà Nội",
          "Major": "Công nghệ thông tin ứng dụng phần mềm"
        },
        {
          "No": 15,
          "Name": "Nguyen Duc Vinh Data",
          "Birthyear": 2002,
          "Gender": "Nam",
          "University": "Học viện Công nghệ Bưu chính Viễn thông",
          "Major": null
        },
        {
          "No": 16,
          "Name": "Nguyễn Dương Long",
          "Birthyear": 2002,
          "Gender": "Nam",
          "University": "ĐH Thuỷ lợi",
          "Major": "Công nghệ thông tin ứng dụng phần mềm"
        },
        {
          "No": 17,
          "Name": "Nguyen Huu Thang",
          "Birthyear": 2000,
          "Gender": "Nam",
          "University": "Đại Học Bách Khoa Hà Nội",
          "Major": "Khoa học máy tính"
        },
        {
          "No": 18,
          "Name": "Nguyễn Mạnh Cường",
          "Birthyear": 1997,
          "Gender": "Nam",
          "University": "Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga",
          "Major": "Điện tử"
        },
        {
          "No": 19,
          "Name": "Nguyễn Mạnh Đức",
          "Birthyear": 2002,
          "Gender": "Nam",
          "University": "Học viện Kỹ thuật mật mã",
          "Major": "An toàn thông tin"
        },
        {
          "No": 20,
          "Name": "Nguyễn Ngọc Chung",
          "Birthyear": 2002,
          "Gender": "Nam",
          "University": "Học viên Công nghệ Bưu chính Viễn Thông HCM",
          "Major": null
        },
        {
          "No": 21,
          "Name": "Nguyễn Tuấn Anh",
          "Birthyear": 1997,
          "Gender": "Nam",
          "University": "Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga",
          "Major": "An toàn thông tin"
        },
        {
          "No": 22,
          "Name": "Nguyễn Văn Quang",
          "Birthyear": 1997,
          "Gender": "Nam",
          "University": "Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga",
          "Major": "An toàn thông tin"
        },
        {
          "No": 23,
          "Name": "Ninh Chí Hướng",
          "Birthyear": 2002,
          "Gender": "Nam",
          "University": "Học viện Công nghệ Bưu chính viễn thông",
          "Major": "An toàn thông tin"
        },
        {
          "No": 24,
          "Name": "Ninh Văn Nghĩa",
          "Birthyear": 2001,
          "Gender": "Nam",
          "University": "Đại Học Bách Khoa Hà Nội",
          "Major": "Khoa học máy tính"
        },
        {
          "No": 25,
          "Name": "Phạm Anh Đức",
          "Birthyear": 2001,
          "Gender": "Nam",
          "University": "Đại học Bách Khoa Hà Nội",
          "Major": "Toán ứng dụng và tin học"
        },
        {
          "No": 26,
          "Name": "Phạm Duy Cương",
          "Birthyear": 1997,
          "Gender": "Nam",
          "University": "Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga",
          "Major": "Công nghệ điện tử"
        },
        {
          "No": 27,
          "Name": "Phạm Hồng Thanh",
          "Birthyear": 1998,
          "Gender": "Nam",
          "University": "Swinburne University",
          "Major": "Phát triển phần mềm"
        },
        {
          "No": 28,
          "Name": "Phạm Thị Khánh Linh",
          "Birthyear": 2002,
          "Gender": "Nữ",
          "University": "Đại học Công nghệ - Đại học Quốc gia Hà Nội",
          "Major": "Mạng máy tính và truyền thông dữ liệu"
        },
        {
          "No": 29,
          "Name": "Phạm Văn Tới",
          "Birthyear": 2002,
          "Gender": "Nam",
          "University": "Học viện Công nghệ Bưu chính viễn thông",
          "Major": "Công nghệ thông tin ứng dụng phần mềm"
        },
        {
          "No": 30,
          "Name": "Trần Đức Mạnh",
          "Birthyear": 1998,
          "Gender": "Nam",
          "University": "Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga",
          "Major": "Bảo mật thông tin"
        },
        {
          "No": 31,
          "Name": "Trần Mạnh Dũng",
          "Birthyear": 2001,
          "Gender": "Nam",
          "University": "Học viện Công nghệ Bưu chính Viễn thông",
          "Major": "Điện tử viễn thông"
        },
        {
          "No": 32,
          "Name": "Trần Minh Dương",
          "Birthyear": 2002,
          "Gender": "Nam",
          "University": "Đại học Công nghệ - Đại học Quốc gia Hà Nội",
          "Major": "Mạng máy tính và truyền thông dữ liệu"
        },
        {
          "No": 33,
          "Name": "Trần Xuân Phú",
          "Birthyear": 2001,
          "Gender": "Nam",
          "University": "University Đại học Công nghệ thông tin - ĐHQG Tp.Hồ chí Minh",
          "Major": "Khoa học máy tính"
        },
        {
          "No": 34,
          "Name": "Vũ Hoàng Long",
          "Birthyear": 2001,
          "Gender": "Nam",
          "University": "Đại học Bách Khoa Hà Nội",
          "Major": "Khoa học máy tính"
        },
        {
          "No": 35,
          "Name": "Vũ Minh Hiếu",
          "Birthyear": 2000,
          "Gender": "Nam",
          "University": "Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga",
          "Major": "Kỹ thuật phần mềm"
        }
       ]
)