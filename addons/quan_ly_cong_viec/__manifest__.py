# -*- coding: utf-8 -*-
{
    'name': "Quản lý công việc (Tích hợp Hệ thống)",

    'summary': """
        Module quản lý công việc, tích hợp dữ liệu gốc từ HRM và Customer Management.
    """,

    'description': """
        Bài tập lớn môn Thực tập Doanh nghiệp - Nhóm 13.
        Hệ thống kết hợp Quản lý khách hàng + Quản lý công việc + Quản lý nhân sự (HRM).
    """,

    'author': "Nhóm 13 - FIT DNU (Kế thừa FIT-DNU)",
    'website': "https://github.com/manhduy04/HN-QTDN-16-01-N13",

    'category': 'Operations',
    'version': '15.0.1.0.0',

    # KHAI BÁO LIÊN KẾT MODULE Ở ĐÂY ĐỂ ĐẠT MỨC 1
    'depends': ['base', 'mail', 'nhan_su', 'khach_hang'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/task_view.xml',
        'views/task_statistic_view.xml',
        'views/my_tasks_view.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}