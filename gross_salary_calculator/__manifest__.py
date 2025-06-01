{
    "odoo_version": "18.0",
    "name": "Gross Salary Calculator",
    "author": "Osama Moawad",
    "version": "1.3",
    "summary": "Calculate gross salary from net",
    "category": "Human Resources",
    "depends": ["hr","hr_contract"],
    "data": [
        "views/hr_contract_views.xml"
    ],
    'images': [
        'static/description/icon.jpeg',
        # 'static/description/conver.jpeg',
    ],
    "installable": True,
    "application": False,
    "license": "LGPL-3"
}
