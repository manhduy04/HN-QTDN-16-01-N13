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

    tien_do = fields.Integer(
        string='Tiến độ (%)',
        compute='_compute_tien_do',
        store=True
    )

    @api.onchange('khach_hang_id')
    def _onchange_khach_hang(self):
        if self.khach_hang_id:
            self.nhan_vien_id = self.khach_hang_id.nhan_vien_phu_trach_id

    @api.depends('trang_thai')
    def _compute_tien_do(self):
        for record in self:
            if record.trang_thai == 'moi':
                record.tien_do = 0
            elif record.trang_thai == 'dang_lam':
                record.tien_do = 50
            elif record.trang_thai == 'hoan_thanh':
                record.tien_do = 100
            elif record.trang_thai == 'huy':
                record.tien_do = 0

    @api.onchange('nhan_vien_id')
    def _onchange_nhan_vien(self):
        if self.nhan_vien_id:
            return {
                'domain': {
                    'khach_hang_id': [
                        ('nhan_vien_phu_trach_id', '=', self.nhan_vien_id.id)
                    ]
                }
            }
        
    def action_bat_dau(self):
        self.trang_thai = 'dang_lam'


    def action_hoan_thanh(self):
        self.trang_thai = 'hoan_thanh'


    def action_huy(self):
        self.trang_thai = 'huy'


    def write(self, vals):
        result = super().write(vals)

        if vals.get('trang_thai') == 'hoan_thanh':
            for job in self:
                if job.khach_hang_id:
                    job.khach_hang_id.write({
                        'trang_thai_cham_soc': 'xong'
                    })

        return result