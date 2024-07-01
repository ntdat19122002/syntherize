import json

import shopify

from ...utility.utility import utility
from odoo import http
from odoo.http import request


class AccessScope(http.Controller):
     @http.route('/access_scope', auth='public')
     def access_scope(self, **kw):
          utility.init_shopify_session()
          access_scopes_shopify_data =  shopify.AccessScope.find()
          access_scopes_shopify_data = [scope.handle for scope in access_scopes_shopify_data]
          return json.dumps(access_scopes_shopify_data)

class StoreFrontAccessToken(http.Controller):
     @http.route('/create_store_front_access_token', auth='public')
     def create_store_front_access_token(self, **kw):
          try:
               utility.init_shopify_session()
               shopify.StorefrontAccessToken.create()
               return {'success': True}
          except Exception as e:
               return json.dumps(e.response.body.decode('utf-8'))

     @http.route('/store_front_access_token', auth='public')
     def get_store_front_access_token(self, **kw):
          try:
               utility.init_shopify_session()
               store_front_access_token_data =  shopify.StorefrontAccessToken.find()
               store_front_access_token_data = [scope.handle for scope in store_front_access_token_data]
               return json.dumps(store_front_access_token_data)
          except Exception as e:
               return json.dumps(e.response.body.decode('utf-8'))