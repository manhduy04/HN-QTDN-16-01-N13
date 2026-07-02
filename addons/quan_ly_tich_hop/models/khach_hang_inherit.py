from odoo import models, fields


class KhachHang(models.Model):
    _inherit = 'khach_hang'

    cong_viec_ids = fields.One2many(
        'cong_viec.cong_viec',
        'khach_hang_id',
        string='Danh sách công việc'
    )