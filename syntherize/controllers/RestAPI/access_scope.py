import shopify

from odoo import http

class AccessScope(http.Controller):
     @http.route('/access_scope', auth='public')
     def access_scope(self, **kw):
          print(1)
          access_scope =  shopify.AccessScope.find()
          return {}