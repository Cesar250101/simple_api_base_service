# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class simple_api_base_service(models.Model):
#     _name = 'simple_api_base_service.simple_api_base_service'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100