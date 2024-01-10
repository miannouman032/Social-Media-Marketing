from odoo import models, fields

class SocialMediaPost(models.Model):
    _name = 'social.media.post'
    _description = 'Social Media Post'

    campaign_id = fields.Many2one('social.media.campaign', string='Campaign')
    content = fields.Text(string='Content')
    publish_date = fields.Datetime(string='Publish Date')