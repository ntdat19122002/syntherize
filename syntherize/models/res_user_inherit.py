from odoo import models, fields
from odoo.http import request


class ResUserInherit(models.Model):
    _inherit = 'res.users'  # Note the plural 'res.users'

    def get_store_by_current_user(self):
         return  request.env['shopify.store'].sudo().search([('user_id', '=', self.id)])