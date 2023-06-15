from app.models.intern import Intern
interns_data = [
    {
        "name": "Bùi Minh Sơn",
        "year_of_birth": "2002",
        "university": "Đại học Công nghệ - Đại học Quốc gia Hà Nội"
    },
    {
        "name": "Đào Đại Hiệp",
        "year_of_birth": "2001",
        "university": "Đại học Bách khoa Hà Nội"
    },
    {
        "name": "Đỗ Anh Tú",
        "year_of_birth": "2002",
        "university": "Đại học Công nghệ - Đại học Quốc gia Hà Nội"
    },
    {
        "name": "Đỗ Bảo Hoàng",
        "year_of_birth": "1997",
        "university": "Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga"
    },
    {
        "name": "Hoàng Quốc Doanh",
        "year_of_birth": "2001",
        "university": "Đại Học Bách Khoa Hà Nội"
    },
    {
        "name": "Le Minh Duc",
        "year_of_birth": "2002",
        "university": "Đại Học Bách Khoa Hà Nội"
    },
    {
        "name": "Lê Phúc Lai",
        "year_of_birth": "2002",
        "university": "Đại Học Bách Khoa Hà Nội"
    },
    {
        "name": "Lê Quang Anh",
        "year_of_birth": "1997",
        "university": "Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga"
    },
    {
        "name": "Lê Trọng Minh",
        "year_of_birth": "2000",
        "university": "Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga"
    },
    {
        "name": "Lê Tùng Lâm",
        "year_of_birth": "1999",
        "university": "Đại Học Bách Khoa Hà Nội"
    },
    {
        "name": "Lê Văn Chiến",
        "year_of_birth": "2002",
        "university": "Đại học Công nghệ - Đại học Quốc gia Hà Nội"
    },
    {
        "name": "Linh Thi Nguyen",
        "year_of_birth": "2002",
        "university": "Đại Học Bách Khoa Hà Nội"
    },
    {
        "name": "Nguyễn Đại An",
        "year_of_birth": "2023",
        "university": "Đại Học Bách Khoa Hà Nội"
    },
    {
        "name": "Nguyễn Đình Hoàng",
        "year_of_birth": "2002",
        "university": "Đại học Công nghệ - Đại học Quốc gia Hà Nội"
    },
    {
        "name": "Nguyen Duc Vinh Data",
        "year_of_birth": "2002",
        "university": "Học viện Công nghệ Bưu chính Viễn thông"
    },
    {
        "name": "Nguyễn Dương Long",
        "year_of_birth": "2002",
        "university": "ĐH Thuỷ lợi"
    },
    {
        "name": "Nguyen Huu Thang",
        "year_of_birth": "2000",
        "university": "Đại Học Bách Khoa Hà Nội"
    },
    {
        "name": "Nguyễn Mạnh Cường",
        "year_of_birth": "1997",
        "university": "Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga"
    },
    {
        "name": "Nguyễn Mạnh Đức",
        "year_of_birth": "2002",
        "university": "Học viện Kỹ thuật mật mã"
    },
    {
        "name": "Nguyễn Ngọc Chung",
        "year_of_birth": "2002",
        "university": "Học viên Công nghệ Bưu chính Viễn Thông HCM"
    },
    {
        "name": "Nguyễn Tuấn Anh",
        "year_of_birth": "1997",
        "university": "Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga"
    },
    {
        "name": "Nguyễn Văn Quang",
        "year_of_birth": "1997",
        "university": "Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga"
    },
    {
        "name": "Ninh Chí Hướng",
        "year_of_birth": "2002",
        "university": "Học viện Công nghệ Bưu chính viễn thông"
    },
    {
        "name": "Ninh Văn Nghĩa",
        "year_of_birth": "2001",
        "university": "Đại Học Bách Khoa Hà Nội"
    },
    {
        "name": "Phạm Anh Đức",
        "year_of_birth": "2001",
        "university": "Đại học Bách Khoa Hà Nội"
    },
    {
        "name": "Phạm Duy Cương",
        "year_of_birth": "1997",
        "university": "Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga"
    },
    {
        "name": "Phạm Hồng Thanh",
        "year_of_birth": "1998",
        "university": "Swinburne University"
    },
    {
        "name": "Phạm Thị Khánh Linh",
        "year_of_birth": "2002",
        "university": "Đại học Công nghệ - Đại học Quốc gia Hà Nội"
    },
    {
        "name": "Phạm Văn Tới",
        "year_of_birth": "2002",
        "university": "Học viện Công nghệ Bưu chính viễn thông"
    },
    {
        "name": "Trần Đức Mạnh",
        "year_of_birth": "1998",
        "university": "Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga"
    },
    {
        "name": "Trần Mạnh Dũng",
        "year_of_birth": "2001",
        "university": "Học viện Công nghệ Bưu chính Viễn thông"
    },
    {
        "name": "Trần Minh Dương",
        "year_of_birth": "2002",
        "university": "Đại học Công nghệ - Đại học Quốc gia Hà Nội"
    },
    {
        "name": "Trần Xuân Phú",
        "year_of_birth": "2001",
        "university": "Trường Đại học Công nghệ thông tin - ĐHQG Tp.Hồ chí Minh"
    },
    {
        "name": "Vũ Hoàng Long",
        "year_of_birth": "2001",
        "university": "Đại học Bách Khoa Hà Nội"
    },
    {
        "name": "Vũ Minh Hiếu",
        "year_of_birth": "2000",
        "university": "Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga"
    }
]

def init_db():
    try:
        for intern in interns_data:
            intern_to_add = Intern(name=intern['name'], year_of_birth=intern['year_of_birth'], university=intern['university'])
            intern_to_add.save()
        print('Added interns to database')
    except:
        print('Error when adding interns to database')
