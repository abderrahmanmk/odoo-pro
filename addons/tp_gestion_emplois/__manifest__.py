{
    'name': 'tp_gestion_emplois',
    'version': '1.0',
    'category': 'Education',
    'summary': 'Gestion Emploi du Temps',
    'description': """
        Module pour la gestion des emplois du temps scolaire.
    """,
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/emploi_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
