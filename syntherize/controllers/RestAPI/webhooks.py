import shopify

from ...utility.utility import utility
from odoo import http
from odoo.http import request
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
        return json.dumps(data.attributes)

    @http.route('/webhook',methods=['GET'], auth='public')
    def get_webhook(self, **kw):
        utility.init_shopify_session()
        data = shopify.Webhook.find(kw.get('webhook_id'))
        return json.dumps(data.attributes)

    @http.route('/webhook/upgrade',type='json', methods=['PUT'], auth='public')
    def put_webhook(self, **kw):
        utility.init_shopify_session()
        if kw.get('webhook_id'):
            webhook = shopify.Webhook.find(kw.get('webhook_id'))
        elif kw.get('webhook_topic'):
            webhooks = shopify.Webhook.find()
            webhook = [webhook for webhook in webhooks if webhook.topic == kw.get('webhook_topic')][0]
        webhook.address = kw.get('webhook_address')
        webhook.save()
        return json.dumps(webhook.attributes)

    @http.route('/webhook/count', auth='public')
    def get_webhook_count(self, **kw):
        utility.init_shopify_session()
        data = shopify.Webhook.count()
        return json.dumps(data)

    @http.route('/webhook/delete',type='json', auth='public')
    def del_webhook(self, **kw):
        utility.init_shopify_session()
        if kw.get('webhook_id'):
            webhook = shopify.Webhook.find(kw.get('webhook_id'))
        elif kw.get('webhook_topic'):
            webhooks = shopify.Webhook.find()
            webhook = [webhook for webhook in webhooks if webhook.topic == kw.get('webhook_topic')][0]
        webhook.destroy()
        return 'Have deleted'

class RechievedWebhook(http.Controller):
    @http.route('/webhook/checkouts/create', type='json', auth='public')
    def webhook_checkout_update(self, **kw):
        print(request.jsonrequest)

    @http.route('/webhook/<string:category>/<string:type>', type='json', auth='public')
    def webhook_return_data(self, **kw):
        print(request.jsonrequest)