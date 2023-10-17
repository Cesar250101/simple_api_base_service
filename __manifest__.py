# -*- coding: utf-8 -*-
{
    'name': "simple_api_base_service",

    'summary': """
        Modulo base para la implementación de los 
        servicios de la API Simple_API""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Method ERP",
    'website': "https://www.method.cl",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/company.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}