import shopify

from ...utility.utility import utility
from odoo import http
import json


class Webhook(http.Controller):
    @http.route('/webhook/list', auth='public')
    def get_webhook_list(self, **kw):
        utility.init_shopify_session()
        data = shopify.Webhook.find()
        data = [scope.attributes for scope in data]
        return json.dumps(data)

    @http.route('/webhook',type='json', methods=['POST'], auth='public')
    def post_webhook_list(self, **kw):
        utility.init_shopify_session()
        data = shopify.Webhook.create({
            'address':kw['webhook_address'],
            'topic':kw['webhook_topic'],
            'format':kw['webhook_format'],
        })
        return json.dumps(data)

    @http.route('/webhook',methods=['GET'], auth='public')
    def get_webhook(self, **kw):
        utility.init_shopify_session()
        data = shopify.Webhook.find(id=kw.get('webhook_id'))
        return json.dumps(data)

    @http.route('/webhook/count', auth='public')
    def get_webhook_count(self, **kw):
        utility.init_shopify_session()
        data = shopify.Webhook.count()
        return json.dumps(data)