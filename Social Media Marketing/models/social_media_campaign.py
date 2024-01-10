from odoo import models, fields

class SocialMediaCampaign(models.Model):
    _name = 'social.media.campaign'
    _description = 'Social Media Campaign'

    name = fields.Char(string='Campaign Name', required=True)
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    description = fields.Text(string='Description')