# -*- coding: utf-8 -*-
{
    'name': "TVP",

    'summary': """
        Modulos creados de manera independiente para TVPromo México
        Primer fase de modulos y version 1.0""",

    'description': """
        Se describiran los modulos incluidos en esta primer fase... 6 MODULOS
    """,

    'author': "TVPromo Mexico",
    'website': "http://www.tvp.mx",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/tvpromo_views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
