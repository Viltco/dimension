# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CriticalItem(models.Model):
    _inherit = 'product.template'

    critical_item = fields.Boolean(string="Is Critical Item")


class CriticalItemVendor(models.Model):
    _inherit = 'res.partner'

    is_approved_vendor = fields.Boolean(string="Is approved Vendor")
