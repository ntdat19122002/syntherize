import json

import shopify

from ...utility.utility import utility
from odoo import http
from odoo.http import request


class Explorer(http.Controller):
     @http.route('/graphql/explorer', type='json', auth='public')
     def graphql_explore(self, **kw):
          utility.init_shopify_session()
          access_scopes_shopify_data =  shopify.GraphQL().execute(kw['explorer_input'])
          return json.dumps(access_scopes_shopify_data)