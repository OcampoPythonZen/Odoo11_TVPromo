# -*- coding: utf-8 -*-
from odoo import http

# class Tvp(http.Controller):
#     @http.route('/tvp/tvp/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tvp/tvp/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tvp.listing', {
#             'root': '/tvp/tvp',
#             'objects': http.request.env['tvp.tvp'].search([]),
#         })

#     @http.route('/tvp/tvp/objects/<model("tvp.tvp"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tvp.object', {
#             'object': obj
#         })