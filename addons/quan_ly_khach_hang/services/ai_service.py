import requests


def tom_tat_khach_hang(customer):

    prompt = f"""
Bạn là chuyên gia chăm sóc khách hàng.

Tên:
{customer.ten_khach_hang}

Loại:
{dict(customer._fields['loai_khach_hang'].selection).get(customer.loai_khach_hang)}

Email:
{customer.email or "Chưa có"}

SĐT:
{customer.so_dien_thoai or "Chưa có"}

Địa chỉ:
{customer.dia_chi or "Chưa có"}

Ghi chú:
{customer.ghi_chu or "Không có"}

Hãy tóm tắt khoảng 100 từ.
"""

    try:

        response = requests.post(

            "http://127.0.0.1:5000/summary",

            json={

                "prompt": prompt

            },

            timeout=60

        )

        return response.json()["summary"]

    except Exception as e:

        return str(e)
    

def goi_y_cham_soc(customer):

    prompt = f"""
Bạn là chuyên gia chăm sóc khách hàng.

Thông tin khách hàng:

Tên: 
{customer.ten_khach_hang}

Loại:
{dict(customer._fields['loai_khach_hang'].selection).get(customer.loai_khach_hang)}

Email:
{customer.email or "Chưa có"}

SĐT:
{customer.so_dien_thoai or "Chưa có"}

Địa chỉ:
{customer.dia_chi or "Chưa có"}

Ghi chú:
{customer.ghi_chu or "Không có"}

Hãy đề xuất kế hoạch chăm sóc khách hàng.

Trả lời đúng theo mẫu sau:

Đánh giá:
...

Cách tiếp cận:
...

Nội dung trao đổi:
...

Thời điểm liên hệ:
...

Lời khuyên:
...

Viết bằng tiếng Việt, ngắn gọn khoảng 100–150 từ.
"""

    try:

        response = requests.post(

            "http://127.0.0.1:5000/care",

            json={

                "prompt": prompt

            },

            timeout=60

        )

        return response.json()["care"]

    except Exception as e:

        return str(e)
    

def soan_email(customer):

    prompt = f"""
Bạn là chuyên gia chăm sóc khách hàng.

Hãy viết một email chăm sóc khách hàng thật chuyên nghiệp.

Thông tin khách hàng:

Tên:
{customer.ten_khach_hang}

Loại khách hàng:
{dict(customer._fields['loai_khach_hang'].selection).get(customer.loai_khach_hang)}

Email:
{customer.email or "Chưa có"}

SĐT:
{customer.so_dien_thoai or "Chưa có"}

Địa chỉ:
{customer.dia_chi or "Chưa có"}

Ghi chú:
{customer.ghi_chu or "Không có"}

Yêu cầu:

- Viết bằng tiếng Việt.
- Xưng hô lịch sự.
- Có tiêu đề email.
- Có lời mở đầu.
- Nội dung ngắn gọn.
- Kết thúc bằng lời cảm ơn.
- Không giải thích thêm ngoài nội dung email.
"""

    try:

        response = requests.post(

            "http://127.0.0.1:5000/email",

            json={

                "prompt": prompt

            },

            timeout=60

        )

        return response.json()["email"]

    except Exception as e:

        return str(e)