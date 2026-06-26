from odoo import models, fields

class NhanVien(models.Model):
    _name = 'nhan_vien'
    _description = 'Nhân viên'
    _order = 'ngay_sinh asc'

    ma_dinh_danh = fields.Char("Mã định danh", required=True)
    ngay_sinh = fields.Date("Ngày sinh")
    que_quan = fields.Char("Quê quán")
    dia_chi = fields.Char("Địa chỉ")
    email = fields.Char("Email")
    so_dien_thoai = fields.Char("Số điện thoại")
    so_bhxh = fields.Char("Số BHXH")
    luong = fields.Float("Lương")

    phong_ban_id = fields.Many2one('phong_ban', string="Phòng ban")
    chuc_vu_id = fields.Many2one('chuc_vu', string="Chức vụ")

    lich_su_cong_tac_ids = fields.One2many(
        'lich_su_cong_tac', 'nhan_vien_id', string="Lịch sử công tác"
    )

    chung_chi_ids = fields.One2many(
        'chung_chi', 'nhan_vien_id', string="Chứng chỉ"
    )
