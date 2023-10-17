# -*- coding: utf-8 -*-
from odoo import http

# class SimpleApiBaseService(http.Controller):
#     @http.route('/simple_api_base_service/simple_api_base_service/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/simple_api_base_service/simple_api_base_service/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('simple_api_base_service.listing', {
#             'root': '/simple_api_base_service/simple_api_base_service',
#             'objects': http.request.env['simple_api_base_service.simple_api_base_service'].search([]),
#         })

#     @http.route('/simple_api_base_service/simple_api_base_service/objects/<model("simple_api_base_service.simple_api_base_service"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('simple_api_base_service.object', {
#             'object': obj
#         })