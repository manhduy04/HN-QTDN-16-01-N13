from odoo import models, fields, api

class CongViec(models.Model):
    _name = 'cong_viec.cong_viec'
    _description = 'Quản lý công việc'

    name = fields.Char(string='Tên công việc', required=True)
    mo_ta = fields.Text(string='Mô tả')

    nhan_vien_id = fields.Many2one(
        'nhan_vien',
        string='Nhân viên phụ trách'
    )

    khach_hang_id = fields.Many2one(
        'khach_hang',
        string='Khách hàng'
    )

    ngay_bat_dau = fields.Date(string='Ngày bắt đầu')
    ngay_ket_thuc = fields.Date(string='Ngày kết thúc')

    trang_thai = fields.Selection([
        ('moi', 'Mới'),
        ('dang_lam', 'Đang làm'),
        ('hoan_thanh', 'Hoàn thành'),
        ('huy', 'Hủy'),
    ], default='moi')

    @api.onchange('khach_hang_id')
    def _onchange_khach_hang(self):
        if self.khach_hang_id:
            self.nhan_vien_id = self.khach_hang_id.nhan_vien_phu_trach_id