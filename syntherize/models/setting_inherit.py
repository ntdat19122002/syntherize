from odoo import models,fields
class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    syntherize_ngrok_address = fields.Char('NGROK address', config_parameter='syntherize.ngrok_address')

    syntherize_shopify_api_version = fields.Char('API Version', config_parameter='syntherize.shopify_api_version')
    syntherize_shopify_key = fields.Char('Client Key', config_parameter='syntherize.shopify_key')
    syntherize_shopify_secret = fields.Char('Secret Key', config_parameter='syntherize.shopify_secret')