# -*- coding: utf-8 -*-
from odoo import models, fields

class CongViec(models.Model):
    _name = 'cong_viec.cong_viec'
    _description = 'Quản lý công việc'

    name = fields.Char(string='Tên công việc', required=True)
    mo_ta = fields.Text(string='Mô tả')

    nhan_vien_id = fields.Many2one(
        'nhan_vien',
        string='Nhân viên phụ trách'
    )

    ngay_bat_dau = fields.Date(string='Ngày bắt đầu')
    ngay_ket_thuc = fields.Date(string='Ngày kết thúc')

    trang_thai = fields.Selection([
        ('moi', 'Mới'),
        ('dang_lam', 'Đang làm'),
        ('hoan_thanh', 'Hoàn thành'),
        ('huy', 'Hủy'),
    ], string='Trạng thái', default='moi')
