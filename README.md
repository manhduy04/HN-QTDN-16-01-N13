<h2 align="center">
    <a href="https://dainam.edu.vn/vi/khoa-cong-nghe-thong-tin">
    🎓 Faculty of Information Technology (DaiNam University)
    </a>
</h2>
<h2 align="center">
    CÔNG NGHỆ HAY - PLATFORM ERP
</h2>
<div align="center">
    <p align="center">
        <img src="docs/logo/aiotlab_logo.png" alt="AIoTLab Logo" width="170"/>
        <img src="docs/logo/fitdnu_logo.png" alt="FIT Logo" width="180"/>
        <img src="docs/logo/dnu_logo.png" alt="DaiNam University Logo" width="200"/>
    </p>

[![AIoTLab](https://img.shields.io/badge/AIoTLab-green?style=for-the-badge)](https://www.facebook.com/DNUAIoTLab)
[![Faculty of Information Technology](https://img.shields.io/badge/Faculty%20of%20Information%20Technology-blue?style=for-the-badge)](https://dainam.edu.vn/vi/khoa-cong-nghe-thong-tin)
[![DaiNam University](https://img.shields.io/badge/DaiNam%20University-orange?style=for-the-badge)](https://dainam.edu.vn)

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
<div align="center">

### Hệ điều hành
[![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)](https://ubuntu.com/)

### Backend Framework
[![Odoo](https://img.shields.io/badge/Odoo_16-714B67?style=for-the-badge&logo=odoo&logoColor=white)](https://www.odoo.com/)
[![Python](https://img.shields.io/badge/Python_3.10-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)

### Frontend
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://html.spec.whatwg.org/)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)](https://www.w3.org/Style/CSS/)

### AI & Machine Learning
[![Google Gemini](https://img.shields.io/badge/Google_Gemini-8E75B2?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev/)

### Database
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)

### DevOps
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)

</div>

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
git clone https://github.com/manhduy04/HN-QTDN-16-01-N13
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
