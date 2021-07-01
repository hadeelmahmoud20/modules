# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Shipping Categories',
    'version': '13.1',
    'summary': '',
    'description': "",
    "Author":"Hadeel Mahmoud",
    'depends': ['base','account'],
    'sequence': 15,

    'data': [
        'security/access.xml',
        'security/ir.model.access.csv',
        'views/views.xml',



    ],

    'installable': True,
    'application': True,
    'auto_install': False,

}
