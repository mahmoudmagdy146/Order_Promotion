# -*- coding: utf-8 -*-
from odoo import http

# class OrderPromotion(http.Controller):
#     @http.route('/order_promotion/order_promotion/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/order_promotion/order_promotion/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('order_promotion.listing', {
#             'root': '/order_promotion/order_promotion',
#             'objects': http.request.env['order_promotion.order_promotion'].search([]),
#         })

#     @http.route('/order_promotion/order_promotion/objects/<model("order_promotion.order_promotion"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('order_promotion.object', {
#             'object': obj
#         })