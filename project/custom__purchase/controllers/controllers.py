# -*- coding: utf-8 -*-
# from odoo import http


# class CustomPurchase(http.Controller):
#     @http.route('/custom__purchase/custom__purchase', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom__purchase/custom__purchase/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom__purchase.listing', {
#             'root': '/custom__purchase/custom__purchase',
#             'objects': http.request.env['custom__purchase.custom__purchase'].search([]),
#         })

#     @http.route('/custom__purchase/custom__purchase/objects/<model("custom__purchase.custom__purchase"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom__purchase.object', {
#             'object': obj
#         })
