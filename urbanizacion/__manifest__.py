# -*- coding: utf-8 -*-

# Part of Probuse Consulting Service Pvt Ltd. See LICENSE file for full copyright and licensing details.

{
    'name': "Property Management",
    'license': 'AGPL-3',
    'summary': """This module allow you to manage Property.""",
    'description': """
        Property management
        This module allow you to manage property.
        Property Management

This module Will help to manage property activities.

    """,
    'author': "SISCRUZ Business Consulting Solution",
    'website': "http://www.siscruz.com",
    'support': 'info@siscruz.com',
    'images': ['static/description/icon.png'],
    'version': '1.0',
    'category' : 'tools',
    'depends': ['base','product'],
    'data':[
        'views/property_customer.xml',
        'views/property_project.xml',
        'views/block_view.xml',
        'views/product_view.xml',
    ],
    'installable' : True,
    'application' : False,
    'auto_install' : False,
}
