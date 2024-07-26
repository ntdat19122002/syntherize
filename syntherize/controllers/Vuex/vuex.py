import json

import shopify

from ...utility.utility import utility
from odoo import http
from odoo.http import request


class Vuex(http.Controller):
     @http.route('/vuex/default', auth='public')
     def vuex_default(self, **kw):
          ngrok_address = request.env['ir.config_parameter'].sudo().get_param('syntherize.ngrok_address')
          return json.dumps({
               'ngrok_address': ngrok_address,
          })