# -*- coding: utf-8 -*-

{
    'name': 'Quản lý tích hợp',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Liên kết Quản lý khách hàng và Quản lý công việc',

    'depends': [
        'quan_ly_khach_hang',
        'quan_ly_cong_viec',
    ],

    'data': [
        'views/khach_hang_view_inherit.xml',
    ],

    'installable': True,
    'application': False,
}