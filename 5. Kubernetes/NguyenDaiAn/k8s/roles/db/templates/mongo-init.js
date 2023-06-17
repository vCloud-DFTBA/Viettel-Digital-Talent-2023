rs.initiate();
db = new Mongo().getDB("data");
db.createCollection("users",{ capped: false })
db.users.insert(
[
  {
    "No": 1,
    "Name": "Bùi Minh Sơn",
    "Birthyear": "2002",
    "Gender": "Nam",
    "University": "Đại học Công nghệ - Đại học Quốc gia Hà Nội",
    "Major": "Công nghệ thông tin",
    "deleted": false,
    "Username": "sonbm"
  },
  {
    "No": 2,
    "Name": "Đào Đại Hiệp",
    "Birthyear": "2001",
    "Gender": "Nam",
    "University": "Đại học Bách khoa Hà Nội",
    "Major": "Điện tử viễn thông",
    "deleted": false,
    "Username": "hiepdd"
  },
  {
    "No": 3,
    "Name": "Đỗ Anh Tú",
    "Birthyear": "2002",
    "Gender": "Nam",
    "University": "Đại học Công nghệ - Đại học Quốc gia Hà Nội",
    "Major": "Mạng máy tính và truyền thông dữ liệu",
    "deleted": false,
    "Username": "tuda"
  },
  {
    "No": 4,
    "Name": "Đỗ Bảo Hoàng",
    "Birthyear": "1997",
    "Gender": "Nam",
    "University": "Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga",
    "Major": "An toàn thông tin",
    "deleted": false,
    "Username": "hoangdb"
  },
  {
    "No": 5,
    "Name": "Hoàng Quốc Doanh",
    "Birthyear": "2001",
    "Gender": "Nam",
    "University": "Đại Học Bách Khoa Hà Nội",
    "Major": null,
    "deleted": false,
    "Username": "doanhhq"
  },
  {
    "No": 6,
    "Name": "Le Minh Duc",
    "Birthyear": "2002",
    "Gender": "Nam",
    "University": "Đại Học Bách Khoa Hà Nội",
    "Major": "Công nghệ thông tin ứng dụng phần mềm",
    "deleted": false,
    "Username": "duclm"
  },
  {
    "No": 7,
    "Name": "Lê Phúc Lai",
    "Birthyear": "2002",
    "Gender": "Nam",
    "University": "Đại Học Bách Khoa Hà Nội",
    "Major": "Kỹ thuật điện tử viễn thông",
    "deleted": false,
    "Username": "lailp"
  },
  {
    "No": 8,
    "Name": "Lê Quang Anh",
    "Birthyear": "1997",
    "Gender": "Nam",
    "University": "Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga",
    "Major": "An toàn thông tin",
    "deleted": false,
    "Username": "anhlq"
  },
  {
    "No": 9,
    "Name": "Lê Trọng Minh",
    "Birthyear": "2000",
    "Gender": "Nam",
    "University": "Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga",
    "Major": "Kỹ thuật điều khiển và tự động hóa",
    "deleted": false,
    "Username": "minhlt"
  },
  {
    "No": 10,
    "Name": "Lê Tùng Lâm",
    "Birthyear": "1999",
    "Gender": "Nam",
    "University": "Đại Học Bách Khoa Hà Nội",
    "Major": "Khoa học máy tính",
    "deleted": false,
    "Username": "lamlt"
  },
  {
    "No": 11,
    "Name": "Lê Văn Chiến",
    "Birthyear": "2002",
    "Gender": "Nam",
    "University": "Đại học Công nghệ - Đại học Quốc gia Hà Nội",
    "Major": "Kỹ thuật hàng không vũ trụ",
    "deleted": false,
    "Username": "chienlv"
  },
  {
    "No": 12,
    "Name": "Nguyễn Thị Linh",
    "Birthyear": "2002",
    "Gender": "Nữ",
    "University": "Đại Học Bách Khoa Hà Nội",
    "Major": "ICT",
    "deleted": false,
    "Username": "linhnt"
  },
  {
    "No": 13,
    "Name": "Nguyễn Đại An",
    "Birthyear": "2023",
    "Gender": "Nam",
    "University": "Đại Học Bách Khoa Hà Nội",
    "Major": "Khoa học máy tính",
    "deleted": false,
    "Username": "annd"
  },
  {
    "No": 14,
    "Name": "Nguyễn Đình Hoàng",
    "Birthyear": "2002",
    "Gender": "Nam",
    "University": "Đại học Công nghệ - Đại học Quốc gia Hà Nội",
    "Major": "Công nghệ thông tin ứng dụng phần mềm",
    "deleted": false,
    "Username": "hoangnd"
  },
  {
    "No": 15,
    "Name": "Nguyen Duc Vinh",
    "Birthyear": "2002",
    "Gender": "Nam",
    "University": "Học viện Công nghệ Bưu chính Viễn thông",
    "Major": null,
    "deleted": false,
    "Username": "vinhnd"
  },
  {
    "No": 16,
    "Name": "Nguyễn Dương Long",
    "Birthyear": "2002",
    "Gender": "Nam",
    "University": "ĐH Thuỷ lợi",
    "Major": "Công nghệ thông tin ứng dụng phần mềm",
    "deleted": false,
    "Username": "longnd"
  },
  {
    "No": 17,
    "Name": "Nguyen Huu Thang",
    "Birthyear": "2000",
    "Gender": "Nam",
    "University": "Đại Học Bách Khoa Hà Nội",
    "Major": "Khoa học máy tính",
    "deleted": false,
    "Username": "thangnh"
  },
  {
    "No": 18,
    "Name": "Nguyễn Mạnh Cường",
    "Birthyear": "1997",
    "Gender": "Nam",
    "University": "Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga",
    "Major": "Điện tử",
    "deleted": false,
    "Username": "cuongnm"
  },
  {
    "No": 19,
    "Name": "Nguyễn Mạnh Đức",
    "Birthyear": "2002",
    "Gender": "Nam",
    "University": "Học viện Kỹ thuật mật mã",
    "Major": "An toàn thông tin",
    "deleted": false,
    "Username": "ducnm"
  },
  {
    "No": 20,
    "Name": "Nguyễn Ngọc Chung",
    "Birthyear": "2002",
    "Gender": "Nam",
    "University": "Học viên Công nghệ Bưu chính Viễn Thông HCM",
    "Major": null,
    "deleted": false,
    "Username": "chungnn"
  },
  {
    "No": 21,
    "Name": "Nguyễn Tuấn Anh",
    "Birthyear": "1997",
    "Gender": "Nam",
    "University": "Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga",
    "Major": "An toàn thông tin",
    "deleted": false,
    "Username": "anhnt"
  },
  {
    "No": 22,
    "Name": "Nguyễn Văn Quang",
    "Birthyear": "1997",
    "Gender": "Nam",
    "University": "Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga",
    "Major": "An toàn thông tin",
    "deleted": false,
    "Username": "quangnv"
  },
  {
    "No": 23,
    "Name": "Ninh Chí Hướng",
    "Birthyear": "2002",
    "Gender": "Nam",
    "University": "Học viện Công nghệ Bưu chính viễn thông",
    "Major": "An toàn thông tin",
    "deleted": false,
    "Username": "huongnc"
  },
  {
    "No": 24,
    "Name": "Ninh Văn Nghĩa",
    "Birthyear": "2001",
    "Gender": "Nam",
    "University": "Đại Học Bách Khoa Hà Nội",
    "Major": "Khoa học máy tính",
    "deleted": false,
    "Username": "nghianv"
  },
  {
    "No": 25,
    "Name": "Phạm Anh Đức",
    "Birthyear": "2001",
    "Gender": "Nam",
    "University": "Đại học Bách Khoa Hà Nội",
    "Major": "Toán ứng dụng và tin học",
    "deleted": false,
    "Username": "ducpa"
  },
  {
    "No": 26,
    "Name": "Phạm Duy Cương",
    "Birthyear": "1997",
    "Gender": "Nam",
    "University": "Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga",
    "Major": "Công nghệ điện tử",
    "deleted": false,
    "Username": "cuongpd"
  },
  {
    "No": 27,
    "Name": "Phạm Hồng Thanh",
    "Birthyear": "1998",
    "Gender": "Nam",
    "University": "Swinburne University",
    "Major": "Phát triển phần mềm",
    "deleted": false,
    "Username": "thanhph"
  },
  {
    "No": 28,
    "Name": "Phạm Thị Khánh Linh",
    "Birthyear": "2002",
    "Gender": "Nữ",
    "University": "Đại học Công nghệ - Đại học Quốc gia Hà Nội",
    "Major": "Mạng máy tính và truyền thông dữ liệu",
    "deleted": false,
    "Username": "linhpt"
  },
  {
    "No": 29,
    "Name": "Phạm Văn Tới",
    "Birthyear": "2002",
    "Gender": "Nam",
    "University": "Học viện Công nghệ Bưu chính viễn thông",
    "Major": "Công nghệ thông tin ứng dụng phần mềm",
    "deleted": false,
    "Username": "toipv"
  },
  {
    "No": 30,
    "Name": "Trần Đức Mạnh",
    "Birthyear": "1998",
    "Gender": "Nam",
    "University": "Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga",
    "Major": "Bảo mật thông tin",
    "deleted": false,
    "Username": "manhtd"
  },
  {
    "No": 31,
    "Name": "Trần Mạnh Dũng",
    "Birthyear": "2001",
    "Gender": "Nam",
    "University": "Học viện Công nghệ Bưu chính Viễn thông",
    "Major": "Điện tử viễn thông",
    "deleted": false,
    "Username": "dungtm"
  },
  {
    "No": 32,
    "Name": "Trần Minh Dương",
    "Birthyear": "2002",
    "Gender": "Nam",
    "University": "Đại học Công nghệ - Đại học Quốc gia Hà Nội",
    "Major": "Mạng máy tính và truyền thông dữ liệu",
    "deleted": false,
    "Username": "duongtm"
  },
  {
    "No": 33,
    "Name": "Trần Xuân Phú",
    "Birthyear": "2001",
    "Gender": "Nam",
    "University": "University Đại học Công nghệ thông tin - ĐHQG Tp.Hồ chí Minh",
    "Major": "Khoa học máy tính",
    "deleted": false,
    "Username": "phutx"
  },
  {
    "No": 34,
    "Name": "Vũ Hoàng Long",
    "Birthyear": "2001",
    "Gender": "Nam",
    "University": "Đại học Bách Khoa Hà Nội",
    "Major": "Khoa học máy tính",
    "deleted": false,
    "Username": "longvh"
  },
  {
    "No": 35,
    "Name": "Vũ Minh Hiếu",
    "Birthyear": "2000",
    "Gender": "Nam",
    "University": "Đại học CNTT, cơ khí & quang học St.Petersburg LB Nga",
    "Major": "Kỹ thuật phần mềm",
    "deleted": false,
    "Username": "hieuvm"
  }
]
)
