<h2 align="center">
    <a href="https://dainam.edu.vn/vi/khoa-cong-nghe-thong-tin">
        🎓 Faculty of Information Technology - Dai Nam University
    </a>
</h2>

<h2 align="center">
    ERP - HỆ THỐNG QUẢN LÝ KHÁCH HÀNG, NHÂN SỰ VÀ CÔNG VIỆC
</h2>

<div align="center">

![Odoo](https://img.shields.io/badge/Odoo-15-purple?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-14-blue?style=for-the-badge)
![JavaScript](https://img.shields.io/badge/JavaScript-yellow?style=for-the-badge)

</div>

---

# 📖 Giới thiệu

Đây là hệ thống ERP được xây dựng trên nền tảng **Odoo 15**, phục vụ việc quản lý khách hàng, quản lý nhân sự và quản lý công việc trong doanh nghiệp.

Hệ thống hướng tới việc số hóa quy trình làm việc, giúp doanh nghiệp quản lý tập trung trên một nền tảng duy nhất.

Ngoài các chức năng quản lý, hệ thống còn tích hợp **AI Chatbot** hỗ trợ người dùng tra cứu thông tin và tư vấn tự động.

---

# 🎯 Mục tiêu

- Quản lý khách hàng
- Quản lý nhân sự
- Quản lý công việc
- Tích hợp AI Chatbot
- Đồng bộ dữ liệu trên một hệ thống ERP

---

# 🏗️ Kiến trúc hệ thống

Hệ thống gồm 4 module chính:

## 1. Quản lý khách hàng

Chức năng

- Quản lý thông tin khách hàng
- Quản lý khách hàng tiềm năng
- Quản lý lịch sử giao dịch
- Theo dõi trạng thái chăm sóc khách hàng

---

## 2. Quản lý nhân sự

Chức năng

- Quản lý hồ sơ nhân viên
- Quản lý phòng ban
- Quản lý chức vụ
- Theo dõi trạng thái làm việc

---

## 3. Quản lý công việc

Chức năng

- Tạo công việc
- Giao việc
- Theo dõi tiến độ
- Theo dõi Deadline
- Thống kê công việc

---

## 4. AI Chatbot

Chức năng

- Hỗ trợ người dùng
- Trả lời câu hỏi
- Tìm kiếm thông tin
- Hỗ trợ thao tác trên hệ thống

---

# 🚀 Chức năng nổi bật

- Dashboard thống kê trực quan
- Quản lý khách hàng
- Quản lý nhân viên
- Quản lý công việc
- Theo dõi tiến độ
- Phân quyền người dùng
- AI Chatbot hỗ trợ

---

# 💻 Công nghệ sử dụng

## Backend

- Odoo 15
- Python 3.10

## Frontend

- XML
- JavaScript
- CSS

## Database

- PostgreSQL

## AI

- Gemini API

## Hệ điều hành

- Ubuntu
- Docker

---

# 📂 Cấu trúc dự án

```
addons/
│
├── quan_ly_khach_hang
│
├── nhan_su
│
├── quan_ly_cong_viec
│
├── quan_ly_chatbot
│
└── quan_ly_tich_hop
```

---

# ⚙️ Cài đặt

Clone project

```bash
git clone <your_repository>
```

Tạo môi trường

```bash
python3.10 -m venv venv
source venv/bin/activate
```

Cài thư viện

```bash
pip install -r requirements.txt
```

Khởi động PostgreSQL

```bash
docker compose up -d
```

Chạy Odoo

```bash
python3 odoo-bin.py -c odoo.conf
```

---

# 📊 Các module

| Module | Chức năng |
|---------|-----------|
| Quản lý khách hàng | CRM |
| Nhân sự | HRM |
| Quản lý công việc | Task Management |
| Chatbot | AI Assistant |
| Tích hợp | Liên kết dữ liệu |

---

# 🔮 Hướng phát triển

- Tích hợp Email
- Tích hợp Telegram
- AI Chatbot thông minh hơn
- Đồng bộ Mobile
- Báo cáo Dashboard nâng cao
- Phân tích dữ liệu bằng AI

---

# 👨‍💻 Nhóm thực hiện

Sinh viên Khoa Công nghệ Thông tin

Đại học Đại Nam

---

<div align="center">

Made with ❤️ using Odoo 15

</div>
