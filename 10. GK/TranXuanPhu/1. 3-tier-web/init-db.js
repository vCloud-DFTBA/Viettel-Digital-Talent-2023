db = db.getSiblingDB("students_db");
db.students.drop();

db.students.insertMany([
    {
        "STT": "1",
        "Họ và tên": "Bùi Minh Sơn",
        "Username": "sonbm",
        "Năm sinh": "2002",
        "Giới tính": "Nam",
        "Trường": "Đại học Công nghệ - Đại học Quốc gia Hà Nội",
        "Chuyên ngành": "Công nghệ thông tin"
    },
    {
        "STT": "2",
        "Họ và tên": "Đào Đại Hiệp",
        "Username": "hiepdd",
        "Năm sinh": "2001",
        "Giới tính": "Nam ",
        "Trường": "Đại học Bách khoa Hà Nội",
        "Chuyên ngành": "Điện tử viễn thông"
    },
    {
        "STT": "3",
        "Họ và tên": "Đỗ Anh Tú",
        "Username": "tuda",
        "Năm sinh": "2002",
        "Giới tính": "Nam",
        "Trường": "Đại học Công nghệ - Đại học Quốc gia Hà Nội",
        "Chuyên ngành": "Mạng máy tính và truyền thông dữ liệu"
    },
    {
        "STT": "4",
        "Họ và tên": "Đỗ Bảo Hoàng",
        "Username": "hoangdb",
        "Năm sinh": "1997",
        "Giới tính": "Nam",
        "Trường": "Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga",
        "Chuyên ngành": "An toàn thông tin"
    },
    {
        "STT": "5",
        "Họ và tên": "Hoàng Quốc Doanh",
        "Username": "doanhhq",
        "Năm sinh": "2001",
        "Giới tính": "Nam ",
        "Trường": "Đại Học Bách Khoa Hà Nội",
        "Chuyên ngành": "NULL"
    },
    {
        "STT": "6",
        "Họ và tên": "Lê Minh Đức",
        "Username": "duclm",
        "Năm sinh": "2002",
        "Giới tính": "Nam ",
        "Trường": "Đại Học Bách Khoa Hà Nội",
        "Chuyên ngành": "Công nghệ thông tin ứng dụng phần mềm"
    },
    {
        "STT": "7",
        "Họ và tên": "Lê Phúc Lai",
        "Username": "lailp",
        "Năm sinh": "2002",
        "Giới tính": "Nam ",
        "Trường": "Đại Học Bách Khoa Hà Nội",
        "Chuyên ngành": "Kỹ thuật điện tử viễn thông"
    },
    {
        "STT": "8",
        "Họ và tên": "Lê Quang Anh",
        "Username": "anhlq",
        "Năm sinh": "1997",
        "Giới tính": "Nam",
        "Trường": "Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga",
        "Chuyên ngành": "An toàn thông tin"
    },
    {
        "STT": "9",
        "Họ và tên": "Lê Trọng Minh",
        "Username": "minhlt",
        "Năm sinh": "2000",
        "Giới tính": "Nam",
        "Trường": "Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga",
        "Chuyên ngành": "Kỹ thuật điều khiển và tự động hóa"
    },
    {
        "STT": "10",
        "Họ và tên": "Lê Tùng Lâm",
        "Username": "lamlt",
        "Năm sinh": "1999",
        "Giới tính": "Nam ",
        "Trường": "Đại Học Bách Khoa Hà Nội",
        "Chuyên ngành": "Khoa học máy tính"
    },
    {
        "STT": "11",
        "Họ và tên": "Lê Văn Chiến",
        "Username": "chienlv",
        "Năm sinh": "2002",
        "Giới tính": "Nam",
        "Trường": "Đại học Công nghệ - Đại học Quốc gia Hà Nội",
        "Chuyên ngành": "Kỹ thuật hàng không vũ trụ"
    },
    {
        "STT": "12",
        "Họ và tên": "Nguyễn Thị Linh",
        "Username": "linhnt",
        "Năm sinh": "2002",
        "Giới tính": "Nữ ",
        "Trường": "Đại Học Bách Khoa Hà Nội",
        "Chuyên ngành": "ICT"
    },
    {
        "STT": "13",
        "Họ và tên": "Nguyễn Đại An",
        "Username": "annd",
        "Năm sinh": "2023",
        "Giới tính": "Nam ",
        "Trường": "Đại Học Bách Khoa Hà Nội",
        "Chuyên ngành": "Khoa học máy tính"
    },
    {
        "STT": "14",
        "Họ và tên": "Nguyễn Đình Hoàng",
        "Username": "hoangnd",
        "Năm sinh": "2002",
        "Giới tính": "Nam",
        "Trường": "Đại học Công nghệ - Đại học Quốc gia Hà Nội",
        "Chuyên ngành": "Công nghệ thông tin ứng dụng phần mềm"
    },
    {
        "STT": "15",
        "Họ và tên": "Nguyễn Đức Vinh",
        "Username": "vinhnd",
        "Năm sinh": "2002",
        "Giới tính": "Nam",
        "Trường": "Học viện Công nghệ Bưu chính Viễn thông",
        "Chuyên ngành": "NULL"
    },
    {
        "STT": "16",
        "Họ và tên": "Nguyễn Dương Long",
        "Username": "longnd",
        "Năm sinh": "2002",
        "Giới tính": "Nam ",
        "Trường": "ĐH Thuỷ lợi",
        "Chuyên ngành": "Công nghệ thông tin ứng dụng phần mềm"
    },
    {
        "STT": "17",
        "Họ và tên": "Nguyễn Hữu Thắng",
        "Username": "thangnh",
        "Năm sinh": "2000",
        "Giới tính": "Nam ",
        "Trường": "Đại Học Bách Khoa Hà Nội",
        "Chuyên ngành": "Khoa học máy tính"
    },
    {
        "STT": "18",
        "Họ và tên": "Nguyễn Mạnh Cường",
        "Username": "cuongnm",
        "Năm sinh": "1997",
        "Giới tính": "Nam",
        "Trường": "Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga",
        "Chuyên ngành": "Điện tử"
    },
    {
        "STT": "19",
        "Họ và tên": "Nguyễn Mạnh Đức",
        "Username": "ducnm",
        "Năm sinh": "2002",
        "Giới tính": "Nam ",
        "Trường": "Học viện Kỹ thuật mật mã",
        "Chuyên ngành": "An toàn thông tin"
    },
    {
        "STT": "20",
        "Họ và tên": "Nguyễn Ngọc Chung",
        "Username": "chungnn",
        "Năm sinh": "2002",
        "Giới tính": "Nam",
        "Trường": "Học viên Công nghệ Bưu chính Viễn Thông HCM",
        "Chuyên ngành": "NULL"
    },
    {
        "STT": "21",
        "Họ và tên": "Nguyễn Tuấn Anh",
        "Username": "anhnt",
        "Năm sinh": "1997",
        "Giới tính": "Nam",
        "Trường": "Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga",
        "Chuyên ngành": "An toàn thông tin"
    },
    {
        "STT": "22",
        "Họ và tên": "Nguyễn Văn Quang",
        "Username": "quangnv",
        "Năm sinh": "1997",
        "Giới tính": "Nam",
        "Trường": "Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga ",
        "Chuyên ngành": "An toàn thông tin"
    },
    {
        "STT": "23",
        "Họ và tên": "Ninh Chí Hướng",
        "Username": "huongnc",
        "Năm sinh": "2002",
        "Giới tính": "Nam",
        "Trường": "Học viện Công nghệ Bưu chính viễn thông",
        "Chuyên ngành": "An toàn thông tin"
    },
    {
        "STT": "24",
        "Họ và tên": "Ninh Văn Nghĩa",
        "Username": "nghianv",
        "Năm sinh": "2001",
        "Giới tính": "Nam ",
        "Trường": "Đại Học Bách Khoa Hà Nội",
        "Chuyên ngành": "Khoa học máy tính"
    },
    {
        "STT": "25",
        "Họ và tên": "Phạm Anh Đức",
        "Username": "ducpa",
        "Năm sinh": "2001",
        "Giới tính": "Nam ",
        "Trường": "Đại học Bách Khoa Hà Nội",
        "Chuyên ngành": "Toán ứng dụng và tin học"
    },
    {
        "STT": "26",
        "Họ và tên": "Phạm Duy Cương",
        "Username": "cuongpd",
        "Năm sinh": "1997",
        "Giới tính": "Nam",
        "Trường": "Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga",
        "Chuyên ngành": "Công nghệ điện tử"
    },
    {
        "STT": "27",
        "Họ và tên": "Phạm Hồng Thanh",
        "Username": "thanhph",
        "Năm sinh": "1998",
        "Giới tính": "Nam ",
        "Trường": "Swinburne University",
        "Chuyên ngành": "Phát triển phần mềm"
    },
    {
        "STT": "28",
        "Họ và tên": "Phạm Thị Khánh Linh",
        "Username": "linhptk",
        "Năm sinh": "2002",
        "Giới tính": "Nữ",
        "Trường": "Đại học Công nghệ - Đại học Quốc gia Hà Nội",
        "Chuyên ngành": "Mạng máy tính và truyền thông dữ liệu"
    },
    {
        "STT": "29",
        "Họ và tên": "Phạm Văn Tới",
        "Username": "toipv",
        "Năm sinh": "2002",
        "Giới tính": "Nam",
        "Trường": "Học viện Công nghệ Bưu chính viễn thông",
        "Chuyên ngành": "Công nghệ thông tin ứng dụng phần mềm"
    },
    {
        "STT": "30",
        "Họ và tên": "Trần Đức Mạnh",
        "Username": "manhtd",
        "Năm sinh": "1998",
        "Giới tính": "Nam",
        "Trường": "Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga",
        "Chuyên ngành": "Bảo mật thông tin"
    },
    {
        "STT": "31",
        "Họ và tên": "Trần Mạnh Dũng",
        "Username": "dungtm",
        "Năm sinh": "2001",
        "Giới tính": "Nam",
        "Trường": "Học viện Công nghệ Bưu chính Viễn thông",
        "Chuyên ngành": "Điện tử viễn thông"
    },
    {
        "STT": "32",
        "Họ và tên": "Trần Minh Dương",
        "Username": "duongtm",
        "Năm sinh": "2002",
        "Giới tính": "Nam",
        "Trường": "Đại học Công nghệ - Đại học Quốc gia Hà Nội",
        "Chuyên ngành": "Mạng máy tính và truyền thông dữ liệu"
    },
    {
        "STT": "33",
        "Họ và tên": "Trần Xuân Phú",
        "Username": "phutx",
        "Năm sinh": "2001",
        "Giới tính": "Nam",
        "Trường": "TrườngĐại học Công nghệ thông tin - ĐHQG Tp.Hồ chí Minh",
        "Chuyên ngành": "Khoa học máy tính"
    },
    {
        "STT": "34",
        "Họ và tên": "Vũ Hoàng Long",
        "Username": "longvh",
        "Năm sinh": "2001",
        "Giới tính": "Nam ",
        "Trường": "Đại học Bách Khoa Hà Nội",
        "Chuyên ngành": "Khoa học máy tính"
    },
    {
        "STT": "35",
        "Họ và tên": "Vũ Minh Hiếu",
        "Username": "hieuvm",
        "Năm sinh": "2000",
        "Giới tính": "Nam",
        "Trường": "Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga",
        "Chuyên ngành": "Kỹ thuật phần mềm"
    }
]);