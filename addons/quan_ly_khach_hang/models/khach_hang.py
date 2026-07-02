from odoo import models, fields, api
from datetime import timedelta

class KhachHang(models.Model):
    _name = 'khach_hang'
    _description = 'Khách hàng'
    _order = 'ten_khach_hang asc'
    _rec_name = 'ten_khach_hang'

    ma_khach_hang = fields.Char("Mã khách hàng", required=True)
    ten_khach_hang = fields.Char("Tên khách hàng", required=True)

    nhan_vien_phu_trach_id = fields.Many2one(
        'nhan_vien',
        string='Nhân viên phụ trách'
    )
    
    loai_khach_hang = fields.Selection(
        [
            ('ca_nhan', 'Cá nhân'),
            ('doanh_nghiep', 'Doanh nghiệp')
        ],
        string="Loại khách hàng",
        default='ca_nhan'
    )

    trang_thai_cham_soc = fields.Selection(
        [
            ('chua', 'Chưa chăm sóc'),
            ('dang', 'Đang chăm sóc'),
            ('xong', 'Đã chăm sóc'),
        ],
        string="Trạng thái chăm sóc",
        default='chua'
    )
    email = fields.Char("Email")
    so_dien_thoai = fields.Char("Số điện thoại")
    dia_chi = fields.Char("Địa chỉ")
    ngay_dang_ky = fields.Date("Ngày đăng ký", default=fields.Date.today)
    ghi_chu = fields.Text("Ghi chú")

    @api.model
    def create(self, vals):
        customer = super().create(vals)

        if customer.nhan_vien_phu_trach_id:

            self.env['cong_viec.cong_viec'].create({
                'name': f"Chăm sóc khách hàng {customer.ten_khach_hang}",
                'khach_hang_id': customer.id,
                'nhan_vien_id': customer.nhan_vien_phu_trach_id.id
                if customer.nhan_vien_phu_trach_id else False,
                'ngay_bat_dau': fields.Date.today(),
                'ngay_ket_thuc': fields.Date.today() + timedelta(days=7),
                'trang_thai': 'moi',
            })

            customer.write({
                'trang_thai_cham_soc': 'dang'
            })

        return customer

#    @api.onchange('khach_hang_id')
#    def _onchange_khach_hang(self):
#        if self.khach_hang_id:
#            self.nhan_vien_id = self.khach_hang_id.nhan_vien_phu_trach_id