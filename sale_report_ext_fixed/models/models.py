# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrderInh(models.Model):
    _inherit = 'sale.order'

    request_number = fields.Char('Request Number')
    rig_code = fields.Char('Rig code')
    cost_center = fields.Char('Cost Center')
    requester = fields.Char('Requester')
    # comments = fields.Char('Comments')
    well_charge = fields.Char('Well Charge')
    well_number = fields.Char('Well Number')
    ref_drss = fields.Char('REF DRSS')
    vendor = fields.Char('Vendor')
    vendor_name = fields.Char('Vendor Name')

    priority = fields.Selection([
        ('low', 'Low'),
        ('normal', 'Normal'),
        ('high', 'High')],
        string='Priority', default="normal", tracking=True)
