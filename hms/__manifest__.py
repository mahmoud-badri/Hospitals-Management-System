{
    'name': "HMS",
    'author': "Mahmoud Badry",
    'category': "",
    'version': "17.0.0.1.0",
    'depends': ["base", "crm",
                ],
    'data':[
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/base_menu.xml',
        'views/patient_view.xml',
        'views/department.xml',
        'views/doctor.xml',
        'views/customers_crm.xml',
        'reports/ patient_report.xml',
    ],
    'application': True,
}