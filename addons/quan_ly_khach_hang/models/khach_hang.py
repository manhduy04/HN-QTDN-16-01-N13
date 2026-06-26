from odoo import models, fields

class KhachHang(models.Model):
    _name = 'khach_hang'
    _description = 'Khách hàng'
    _order = 'ten_khach_hang asc'

    ma_khach_hang = fields.Char("Mã khách hàng", required=True)
    ten_khach_hang = fields.Char("Tên khách hàng", required=True)
    loai_khach_hang = fields.Selection(
        [
            ('ca_nhan', 'Cá nhân'),
            ('doanh_nghiep', 'Doanh nghiệp')
        ],
        string="Loại khách hàng",
        default='ca_nhan'
    )
    email = fields.Char("Email")
    so_dien_thoai = fields.Char("Số điện thoại")
    dia_chi = fields.Char("Địa chỉ")
    ngay_dang_ky = fields.Date("Ngày đăng ký", default=fields.Date.today)
    ghi_chu = fields.Text("Ghi chú")
