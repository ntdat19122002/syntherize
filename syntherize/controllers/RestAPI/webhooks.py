import shopify

from ...utility.utility import utility
from odoo import http
import json


class Webhook(http.Controller):
    @http.route('/webhook/list', auth='public')
    def get_webhook_list(self, **kw):
        utility.init_shopify_session()
        access_scopes_shopify_data = shopify.Webhook.find()
        access_scopes_shopify_data = [scope.handle for scope in access_scopes_shopify_data]
        return json.dumps(access_scopes_shopify_data)