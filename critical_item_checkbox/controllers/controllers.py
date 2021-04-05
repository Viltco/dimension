# -*- coding: utf-8 -*-
# from odoo import http


# class CriticalItemCheckbox(http.Controller):
#     @http.route('/critical_item_checkbox/critical_item_checkbox/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/critical_item_checkbox/critical_item_checkbox/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('critical_item_checkbox.listing', {
#             'root': '/critical_item_checkbox/critical_item_checkbox',
#             'objects': http.request.env['critical_item_checkbox.critical_item_checkbox'].search([]),
#         })

#     @http.route('/critical_item_checkbox/critical_item_checkbox/objects/<model("critical_item_checkbox.critical_item_checkbox"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('critical_item_checkbox.object', {
#             'object': obj
#         })
