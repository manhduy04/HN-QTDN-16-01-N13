# 📖 1. Giới thiệu

Hệ thống ERP Quản lý khách hàng và quản lý công việc được phát triển trên nền tảng Odoo ERP, phục vụ bài tập lớn học phần Hội nhập và Quản trị Doanh nghiệp tại Khoa Công nghệ Thông tin – Đại học Đại Nam.

Hệ thống giúp doanh nghiệp quản lý tập trung các nghiệp vụ quan trọng như:

- Quản lý nhân sự (HRM)
- Quản lý khách hàng (CRM)
- Quản lý công việc (Task Management)

Việc tích hợp các module trên cùng một nền tảng giúp doanh nghiệp tối ưu quy trình làm việc, nâng cao hiệu quả quản lý và giảm thời gian xử lý nghiệp vụ.

---

# 🎯 2. Mục tiêu dự án

- Xây dựng hệ thống ERP trên nền tảng Odoo.
- Quản lý tập trung thông tin nhân sự, khách hàng và công việc.
- Tự động hóa quy trình quản lý doanh nghiệp.
- Theo dõi tiến độ công việc và phân công nhân sự.
- Hỗ trợ doanh nghiệp quản lý dữ liệu chính xác và hiệu quả.

---

# 🏗️ 3. Kiến trúc hệ thống

## 3.1 HRM (Human Resource Management)

Module quản lý nhân sự giúp lưu trữ và quản lý toàn bộ thông tin nhân viên.

### Chức năng

- Quản lý hồ sơ nhân viên
- Quản lý phòng ban
- Quản lý chức vụ
- Quản lý hợp đồng lao động
- Theo dõi thông tin nhân sự
- Phân quyền người dùng

---

## 3.2 Customer Management

Module quản lý khách hàng hỗ trợ doanh nghiệp theo dõi toàn bộ thông tin khách hàng.

### Chức năng

- Quản lý khách hàng
- Quản lý khách hàng tiềm năng
- Quản lý thông tin liên hệ
- Quản lý lịch sử giao dịch
- Theo dõi trạng thái khách hàng
- Hỗ trợ chăm sóc khách hàng

---

## 3.3 Task Management

Module quản lý công việc giúp theo dõi tiến độ làm việc của nhân viên.

### Chức năng

- Tạo công việc
- Phân công công việc
- Theo dõi tiến độ
- Quản lý deadline
- Cập nhật trạng thái công việc
- Báo cáo tiến độ

---

# 🔧 4. Công nghệ sử dụng

| Thành phần | Công nghệ |
|---|---|
| ERP Framework | Odoo |
| Backend | Python |
| Cơ sở dữ liệu | PostgreSQL |
| Container | Docker |
| Hệ điều hành | Ubuntu / WSL2 |
| Quản lý mã nguồn | Git & GitHub |

---

# ⚙️ 5. Cài đặt

## 5.1 Clone project

```bash
git clone https://github.com/vandat2004/HN-QTDN-16-01-N13.git
cd HN-QTDN-16-01-N13
```

---

## 5.2 Tạo Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```

---

## 5.3 Cài đặt dependencies

```bash
pip install -r requirements.txt
```

---

## 5.4 Khởi tạo PostgreSQL

```bash
sudo docker-compose up -d
```

Thông tin Database

| Thuộc tính | Giá trị |
|---|---|
| Host | localhost |
| Port | 5431 |
| User | odoo |
| Password | odoo |

---

## 5.5 Tạo file cấu hình

```bash
cp odoo.conf.template odoo.conf
```

Ví dụ:

```ini
[options]
addons_path = addons
db_host = localhost
db_port = 5431
db_user = odoo
db_password = odoo
xmlrpc_port = 8069
```

---

## 5.6 Khởi động Odoo

```bash
python3 odoo-bin.py -c odoo.conf
```

Truy cập:

```text
http://localhost:8069
```

---

# 📦 6. Cài đặt Module

Sau khi khởi động hệ thống:

- Đăng nhập Odoo
- Vào Apps
- Chọn Update Apps List
- Tìm các module của nhóm
- Cài đặt:
  - HRM
  - Customer Management
  - Task Management

---

# 📁 7. Cấu trúc thư mục

```text
HN-QTDN-16-01-N13/
├── addons/
│   ├── hrm/
│   ├── customer_management/
│   └── task_management/
├── odoo/
├── docker-compose.yml
├── requirements.txt
├── odoo-bin.py
├── odoo.conf.template
└── README.md
```

---

# 🚀 8. Chức năng nổi bật

## 👨‍💼 Quản lý nhân sự

- Quản lý nhân viên
- Quản lý phòng ban
- Quản lý chức vụ
- Theo dõi hồ sơ

---

## 👥 Quản lý khách hàng

- Quản lý thông tin khách hàng
- Theo dõi lịch sử giao dịch
- Quản lý khách hàng tiềm năng
- Chăm sóc khách hàng

---

## 📋 Quản lý công việc

- Phân công công việc
- Theo dõi tiến độ
- Quản lý deadline
- Báo cáo công việc

---

# 🧪 9. Kiểm thử

Khởi động hệ thống:

```bash
python3 odoo-bin.py -c odoo.conf
```

Sau đó truy cập:

```text
http://localhost:8069
```

Kiểm tra:

- Đăng nhập hệ thống
- Cài đặt module
- Thêm dữ liệu
- Chỉnh sửa dữ liệu
- Xóa dữ liệu
- Kiểm tra phân quyền

---

# 👥 10. Thành viên nhóm

**Nhóm 13**

**Lớp KHMT 16-01**

**Khoa Công nghệ Thông tin**

**Đại học Đại Nam**

Repository:

```text
https://github.com/vandat2004/HN-QTDN-16-01-N13
```

---

# 📚 11. Tài liệu tham khảo

- Odoo Documentation
- PostgreSQL Documentation
- Docker Documentation
- Python Documentation

---

# 📝 12. License

Dự án được phát triển phục vụ mục đích học tập tại Đại học Đại Nam.

© 2026 - KHMT16-01 - Nhóm 13
