from odoo.http import request


class Utility:
    def __init__(self):
        pass

    def get_store_by_current_user(self):
        return request.env['shopify.store'].sudo().search([('user_id', '=', request.env.user.id)])

    def init_shopify_session(self):
        store = self.get_store_by_current_user()
        store.init_shopify_session()

utility = Utility()