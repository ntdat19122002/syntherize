import binascii
import os
import traceback

import shopify
import werkzeug

import odoo
from odoo import http
import json
from odoo.addons.portal.controllers.portal import CustomerPortal

from odoo.http import request, _logger


class CustomerPortal(CustomerPortal):
    @odoo.http.route()
    def home(self):
        # Todo: Check nhóm người dùng. Nếu là admin thì redirect về '/web' 👌
        # Reply: Trong odoo, admin sau khi đăng nhập đã được tự động trả về web
        if request.env.user.has_group('base.group_user'):
            return werkzeug.utils.redirect('/web')
        return werkzeug.utils.redirect('/apps/syntherize')


class AuthShopifyController(http.Controller):
    @http.route('/shopify/syntherize/auth', auth='public')
    def shopify_auth2(self, **kw):
        try:
            if 'shop' in kw:
                api_version = request.env['ir.config_parameter'].sudo().get_param('syntherize.shopify_api_version')
                shopify_key = request.env['ir.config_parameter'].sudo().get_param('syntherize.shopify_key')
                shopify_secret = request.env['ir.config_parameter'].sudo().get_param('syntherize.shopify_secret')

                shopify.Session.setup(api_key=shopify_key, secret=shopify_secret)

                shop_url = kw['shop']
                # Todo: tạo state từ việc hash secret key với tên shop👌
                # Reply: state dùng để tránh lỗi CSRF (tấn công giả mạo), odoo đã có sãn hàm tạo CSRF token từ session
                # time_limit (Nếu có) và database.secret
                state = 'abc'
                redirect_uri = request.env['ir.config_parameter'].sudo().get_param('web.base.url') + "/shopify/syntherize/finalize"
                scopes = [
                    "read_products",
                    "read_orders",
                    "write_orders",
                    'read_script_tags',
                    'write_script_tags',
                    'read_themes'
                ]

                newSession = shopify.Session(shop_url, api_version)
                auth_url = newSession.create_permission_url(scopes, redirect_uri,state)

                return werkzeug.utils.redirect(auth_url)
        except Exception as e:
            _logger.error(traceback.format_exc())
        return werkzeug.utils.redirect('https://nestscale.com/contact-us')

    @http.route('/shopify/syntherize/finalize', autgeth="public", type="http", cors="*")
    def shopify_callback(self, **kw):
        try:
            # Todo: Check state 👌
            if kw['state'] == 'abc':
                if 'shop' in request.params:
                    api_version = request.env['ir.config_parameter'].sudo().get_param('syntherize.shopify_api_version')
                    shopify_key = request.env['ir.config_parameter'].sudo().get_param('syntherize.shopify_key')
                    shopify_secret = request.env['ir.config_parameter'].sudo().get_param('syntherize.shopify_secret')
                    shop_url = kw['shop']
                    shopify.Session.setup(api_key=shopify_key, secret=shopify_secret)
                    shopify_session = shopify.Session(shop_url, api_version)
                    access_token = shopify_session.request_token(kw)
                    shopify.ShopifyResource.activate_session(shopify_session)

                    if access_token:
                        shopify_shop = shopify.Shop.current()  # Get the current shop

                        shop = request.env['shopify.store'].sudo().search([('shop_url', '=', kw['shop'])])
                        if not shop:
                            # Chưa tồn tại shop trong database, tạo shop mới
                            self.make_new_shop(shopify_shop, access_token)
                        else:
                            # Shop đã tồn tại, cập nhật lại thông tin của shop
                            # Các thông tin không thay đổi => không cần cập nhật:
                            # - Id
                            self.upgrade_shop_info(shop, shopify_shop, access_token)

                        shop.make_webhook()
                        shop.make_script_tag()

                        return werkzeug.utils.redirect('/apps/syntherize')
        except Exception as e:
            _logger.error(traceback.format_exc())
        # Các route http trả về trang hỗ trợ hoặc báo lỗi khi xảy ra exception
        return werkzeug.utils.redirect('https://nestscale.com/contact-us')

    def make_new_shop(self, shopify_shop, access_token):
        if request.env.user:
             created_shop = request.env['shopify.store'].sudo().create({
                'shopify_id': shopify_shop.id,
                'shop_url': shopify_shop.domain,
                'shop_name': shopify_shop.name,
                'currency': shopify_shop.currency,
                'country': shopify_shop.country,
                'phone': shopify_shop.phone,
                'email': shopify_shop.email,
                'token': access_token,
                'user_id': request.env.user.id
             })
             request.env.user.shop_id = created_shop.id
        else:
            request.env['shopify.store'].sudo().create({
                'shopify_id': shopify_shop.id,
                'shop_url': shopify_shop.domain,
                'shop_name': shopify_shop.name,
                'currency': shopify_shop.currency,
                'country': shopify_shop.country,
                'phone': shopify_shop.phone,
                'email': shopify_shop.email,
                'token': access_token
            })

    def upgrade_shop_info(self, shop, shopify_shop, access_token):
        if shop.user_id:
            shop.sudo().write({
                # 'shopify_id': shopify_shop.id,
                'shop_url': shopify_shop.domain,
                'shop_name': shopify_shop.name,
                'currency': shopify_shop.currency,
                'country': shopify_shop.country,
                'phone': shopify_shop.phone,
                'email': shopify_shop.email,
                'token': access_token,
            })
        else:
            if request.env.user:
                created_shop = shop.sudo().write({
                    'user_id': request.env.user.id,
                    # 'shopify_id': shopify_shop.id,
                    'shop_url': shopify_shop.domain,
                    'shop_name': shopify_shop.name,
                    'currency': shopify_shop.currency,
                    'country': shopify_shop.country,
                    'phone': shopify_shop.phone,
                    'email': shopify_shop.email,
                    'token': access_token,
                })
                request.env.user.shop_id = created_shop.id
            else:
                shop.sudo().write({
                    # 'shopify_id': shopify_shop.id,
                    'shop_url': shopify_shop.domain,
                    'shop_name': shopify_shop.name,
                    'currency': shopify_shop.currency,
                    'country': shopify_shop.country,
                    'phone': shopify_shop.phone,
                    'email': shopify_shop.email,
                    'token': access_token,
                })

    @http.route('/apps/syntherize', auth='public')
    def main(self, **kw):
        return self.render_ui()

    @http.route('/apps/syntherize/<string:components>', auth="user", type="http", cors="*")
    def app_shopify_xero_branch(self):
        return self.render_ui()

    @http.route('/apps/syntherize/<string:components>/<string:components2>', auth="user", type="http", cors="*")
    def app_shopify_xero_branch2(self):
        return self.render_ui()

    def render_ui(self):
        value = {
            'user_name': request.env.user.name
        }
        return request.render('syntherize.app-test', {'app_setting': json.dumps(value)})
