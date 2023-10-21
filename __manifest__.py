# -*- coding: utf-8 -*-
{
    'name': "data_bulk_upload_app",

    'summary': """
        Enhance your business with data bulk upload capabilities""",

    'description': """
        Data Bulk Upload App - Advanced Data Management for Your Business

        Features:
        - Intuitive bulk data upload
        - Integration with major Odoo modules
        - Customizable views for your specific business needs
        - User-friendly interface
        
        Benefit from advanced data management tools and streamline your business operations with Data Bulk Upload App.
    """,

    'author': "Tarek Eissa",
    'maintainer': "Tarek Eissa",
    'contributors': [""],
    'website': "https://www.prospexai.com",
    
    'category': 'Data Management',
    'version': '1.0',

    'license': "Other proprietary",
    'depends': ['base', 'website', 'spreadsheet_dashboard', 'base_setup', 'portal', 'web', 'web_editor'],

    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',

    ],
    'images': [
        'static/description/main_screenshot.png',
        'static/src/img/pngwing.com.png'
    ],

    'price': 49.99,
    'currency': 'USD',

    'application': True,
    'installable': True,
}
