# -*- coding: utf-8 -*-
import re
from datetime import date, timedelta
from odoo import fields, models, api
from odoo.exceptions import ValidationError


class KhachHang(models.Model):
    _name = 'khach_hang'
    _description = 'Khách Hàng'

    first_name = fields.Char(string='Tên', required=True)
    last_name = fields.Char(string='Họ và tên đệm', required=True)
    full_name = fields.Char(string='Họ và tên', compute='_compute_full_name', store=True)
    email = fields.Char(string='Email', required=True)
    phone = fields.Char(string='Số điện thoại', required=True)
    address = fields.Char(string='Địa chỉ', required=True)
    birthday = fields.Date(string='Ngày sinh', required=True)

    ho_tro_ids = fields.One2many('ho_tro_khach_hang', 'nguoi_tao', string='Hỗ trợ khách hàng')
    khach_hang_tiem_nang_ids = fields.One2many('khach_hang_tiem_nang', 'khach_hang_id', string='Khách hàng tiềm năng')

    @api.depends('first_name', 'last_name')
    def _compute_full_name(self):
        for record in self:
            if record.first_name and record.last_name:
                record.full_name = f"{record.last_name.strip()} {record.first_name.strip()}"

    @api.constrains('birthday')
    def _check_birthday(self):
        for record in self:
            if record.birthday and record.birthday > date.today():
                raise ValidationError("Ngày sinh không hợp lệ! Không thể lớn hơn ngày hiện tại.")

    @api.constrains('email')
    def _check_email(self):
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        for record in self:
            if record.email and not re.match(email_regex, record.email.strip()):
                raise ValidationError("Địa chỉ email không hợp lệ!")

    @api.constrains('phone')
    def _check_phone(self):
        phone_regex = r'^\d{10}$'
        for record in self:
            if record.phone and not re.match(phone_regex, record.phone.strip()):
                raise ValidationError("Số điện thoại không hợp lệ! Phải có đúng 10 chữ số.")

    @api.constrains('first_name', 'last_name')
    def _check_name(self):
        name_regex = r"^[a-zA-ZÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚĂĐĨŨƠàáâãèéêìíòóôõùúăđĩũơƯĂÂÊÔƠỨỪỮỬỰẤẦẨẪẬẮẰẲẴẶẸẺẼỀỀỂưăâêôơứừữửựấầẩẫậắằẳẵặẹẻẽềềểỄỆỈỊỌỎỐỒỔỖỘỚỜỞỠỢỤỦỨỨỬỰỲÝỶỸỸửựỳýỷỹ\s]+$"
        for record in self:
            if not record.first_name or not record.last_name:
                continue
            first_name_clean = record.first_name.strip()
            last_name_clean = record.last_name.strip()

            if len(first_name_clean) < 2 or len(last_name_clean) < 2:
                raise ValidationError("Tên và họ không hợp lệ! Phải có ít nhất 2 ký tự.")

            if not re.match(name_regex, first_name_clean) or not re.match(name_regex, last_name_clean):
                raise ValidationError("Tên không được chứa ký tự đặc biệt hoặc số!")

# =========================================================================
    # ĐOẠN CODE TỰ ĐỘNG HÓA QUY TRÌNH (MỨC 2) - BẢN SỬA CHUẨN TRANSACTION
    # =========================================================================
@api.model
    def create(self, vals):
        # 1. Gọi hàm tạo khách hàng mặc định của Odoo để lưu thông tin xuống database trước
        customer = super(KhachHang, self).create(vals)
        
        # 2. Kiểm tra xem module 'quan_ly_cong_viec' (model 'task') có tồn tại trong hệ thống không
        if 'task' in self.env:
            try:
                with self.env.cr.savepoint():
                    # Tự động tính ngày deadline là 3 ngày sau kể từ ngày tạo khách hàng
                    deadline_auto = date.today() + timedelta(days=3)
                    
                    # CẬP NHẬT: Thêm leader_id để thỏa mãn thuộc tính required=True bên model task
                    self.env['task'].create({
                        'name': f"Liên hệ chăm sóc khách hàng mới: {customer.full_name}",
                        'customer_id': customer.id,
                        'leader_id': 1,  # Đảm bảo ID này tồn tại trong bảng 'employee' của bạn
                        'deadline': deadline_auto,
                        'progress': 0,
                        'description': f"Hệ thống tự động tạo tác vụ: Vui lòng gọi điện tư vấn và làm quen với khách hàng {customer.full_name}."
                    })
            except Exception:
                # Nếu có bất kỳ lỗi nào, hệ thống sẽ bỏ qua để giữ an toàn cho dữ liệu khách hàng
                pass
                
        return customer