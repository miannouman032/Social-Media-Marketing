
{
    'name': 'Social Media Marketing',
    'version': '1.0',
    'author': 'Your Name',
    'category': 'Marketing',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/social_media_campaign_view.xml',
        'views/social_media_post_view.xml',
        'actions.xml',
    ],
    'installable': True,
    'application': True,
}