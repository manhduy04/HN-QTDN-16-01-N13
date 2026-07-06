from odoo import models, fields, api
from datetime import timedelta
import logging
from ..services import ai_service


_logger = logging.getLogger(__name__)

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

    tom_tat_ai = fields.Text(
        string="Tóm tắt AI",
        readonly=True
    )

    goi_y_cham_soc = fields.Text(
        string="Gợi ý chăm sóc",
        readonly=True
    )
    email_ai = fields.Text(
        string="Email chăm sóc",
        readonly=True
    )

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
    
    def unlink(self):
        for customer in self:

            _logger.info(
                "=== TRIGGER === Đang xóa khách hàng: %s",
                customer.ten_khach_hang
            )

            jobs = self.env['cong_viec.cong_viec'].search([
                ('khach_hang_id', '=', customer.id)
            ])

            _logger.info(
                "=== TRIGGER === Tìm thấy %s công việc liên quan",
                len(jobs)
            )

            jobs.unlink()

            _logger.info(
                "=== TRIGGER === Đã xóa toàn bộ công việc của khách hàng %s",
                customer.ten_khach_hang
            )

        return super().unlink()
    
    def action_tom_tat_ai(self):
        for customer in self:

            tom_tat = ai_service.tom_tat_khach_hang(customer)

            customer.write({
                'tom_tat_ai': tom_tat
            })

    def action_goi_y_cham_soc(self):
        for customer in self:

            goi_y = ai_service.goi_y_cham_soc(customer)

            customer.write({
                'goi_y_cham_soc': goi_y
            })

    def action_soan_email(self):
        for customer in self:

            email = ai_service.soan_email(customer)

            customer.write({
                'email_ai': email
            })

#    @api.onchange('khach_hang_id')
#    def _onchange_khach_hang(self):
#        if self.khach_hang_id:
#            self.nhan_vien_id = self.khach_hang_id.nhan_vien_phu_trach_id