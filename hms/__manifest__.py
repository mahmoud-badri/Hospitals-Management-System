{
    'name': "HMS",
    'author': "Mahmoud Badry",
    'category': "",
    'version': "17.0.0.1.0",
    'depends': ["base", "crm", "mail"
                ],
    'data':[
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/base_menu.xml',
        'views/patient_view.xml',
        'views/history.xml',
        'views/department.xml',
        'views/doctor.xml',
        'views/customers_crm.xml',
        'reports/ patient_report.xml',
    ],
    'assets': {
        'web.assets_backend': ["hms/static/src/css/style.css"]
    },
    'application': True,
}