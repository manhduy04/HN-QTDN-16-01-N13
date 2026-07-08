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

Đây là hệ thống ERP được xây dựng trên nền tảng Odoo 15, phục vụ việc quản lý khách hàng, quản lý nhân sự và quản lý công việc trong doanh nghiệp.

Hệ thống hướng tới việc số hóa quy trình làm việc, giúp doanh nghiệp quản lý tập trung trên một nền tảng duy nhất, giảm thời gian xử lý thủ công và nâng cao hiệu quả quản lý.

Bên cạnh các chức năng quản lý, hệ thống còn cung cấp các công cụ hỗ trợ như theo dõi tiến độ công việc, thống kê dữ liệu, báo cáo trực quan và phân quyền người dùng, giúp nhà quản lý dễ dàng giám sát hoạt động của doanh nghiệp và đưa ra quyết định nhanh chóng, chính xác.

---

# 🎯 Mục tiêu

- Quản lý khách hàng
- Quản lý nhân sự
- Quản lý công việc
- Đồng bộ dữ liệu trên một hệ thống ERP

---

# 🏗️ Kiến trúc hệ thống

Hệ thống gồm 4 module chính:

<img width="1024" height="574" alt="image" src="https://github.com/user-attachments/assets/c88ab1b6-0f24-4a58-ac39-bd54d243de89" />


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

# 🚀 Chức năng nổi bật

- Quản lý khách hàng
- Quản lý nhân viên
- Quản lý công việc
- Theo dõi tiến độ
- Phân quyền người dùng

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

# Giao diện ứng dụng.

Giao diện Danh sách Nhân viên (List View): Hệ thống hiển thị trực quan toàn bộ danh sách nhân sự chính thức của công ty.  

<img width="1909" height="940" alt="image" src="https://github.com/user-attachments/assets/6ddb7d4c-5164-4193-96c4-567ca7cd4e23" />

Giao diện Khởi tạo Nhân viên mới (Form View): Khi phát sinh nhân sự mới, bộ phận HR sử dụng cấu trúc biểu mẫu chuẩn hóa để nhập hồ sơ.

<img width="1909" height="948" alt="image" src="https://github.com/user-attachments/assets/350d4eeb-82ee-48bb-b0eb-3d85b4cccb84" />

Giao diện Danh sách Khách hàng (List View): Giao diện hiển thị danh mục toàn bộ các khách hàng/đối tác hiện có trong cơ sở dữ liệu. 

<img width="1915" height="943" alt="image" src="https://github.com/user-attachments/assets/e5c34280-e8cf-469f-a641-35e6f8b12ba0" />

Giao diện Biểu mẫu khởi tạo Khách hàng (Form View): Khi tiếp nhận thông tin từ các kênh thô, nhân viên click nút "Tạo" để mở biểu mẫu nhập liệu.

<img width="1918" height="943" alt="image" src="https://github.com/user-attachments/assets/14c5d47e-429d-4f49-b688-a36b666cd543" />

Giao diện Hồ sơ chi tiết Khách hàng đã gán Dữ liệu gốc chức năng sửa [Mức 1]: Hệ thống chứng minh tính toàn vẹn dữ liệu gốc khi hiển thị thông tin chi tiết của đối tác Nguyễn Minh Tuấn.

<img width="1918" height="942" alt="image" src="https://github.com/user-attachments/assets/efb6deab-d5f9-4d1c-9787-3d2407edee81" />

Giao diện Danh sách Công việc (List View): Giao diện cung cấp cái nhìn tổng quan về toàn bộ các đầu việc trong hệ thống.

<img width="1915" height="943" alt="image" src="https://github.com/user-attachments/assets/3badcad3-ab46-498c-81d3-f9eea467d4ea" />

Giao diện Khởi tạo Công việc thủ công (Form View): Bên cạnh luồng tạo tự động, hệ thống cho phép người quản lý chủ động tạo việc mới bằng biểu mẫu chuẩn hóa. Form tích hợp các nút chuyển trạng thái nhanh (Bắt đầu, Hoàn thành, Hủy) ở góc trên và các trường chọn dữ liệu liên kết đối tác, nhân sự cùng thanh đo tiến độ khởi tạo mặc định là 0%.

<img width="1918" height="943" alt="image" src="https://github.com/user-attachments/assets/f188b6f7-3a46-4d50-ade1-21c29321690b" />


# 🔮 Hướng phát triển

- 📧 **Tích hợp Email**
  - Tự động gửi thông báo, nhắc việc và xác nhận thông tin đến khách hàng, nhân viên.

- 📱 **Tích hợp Telegram**
  - Gửi thông báo công việc, trạng thái dự án và nhắc deadline theo thời gian thực.

- 🤖 **AI Chatbot thông minh hơn**
  - Nâng cao khả năng tư vấn, hỗ trợ khách hàng và trả lời theo dữ liệu doanh nghiệp.

- 📲 **Đồng bộ Mobile**
  - Phát triển ứng dụng hoặc PWA để quản lý công việc mọi lúc, mọi nơi.

- 📊 **Báo cáo Dashboard nâng cao**
  - Bổ sung biểu đồ, KPI và thống kê trực quan hỗ trợ nhà quản lý ra quyết định.

- 🧠 **Phân tích dữ liệu bằng AI**
  - Phân tích hành vi khách hàng, dự đoán xu hướng và đề xuất giải pháp kinh doanh.

---

# 👨‍💻 Nhóm thực hiện

Sinh viên Khoa Công nghệ Thông tin

Đại học Đại Nam

---

<img width="1125" height="1625" alt="images_page-0001" src="https://github.com/user-attachments/assets/5ef762c3-8e5a-422c-8d1e-7e7a56f6d897" />


<div align="center">

Made with ❤️ using Odoo 15

</div>
