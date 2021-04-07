# -*- coding: utf-8 -*-

from odoo import models, fields, api,_


class AttachmentFields(models.Model):
    _inherit = 'mrp.production'

    check=fields.Boolean("Check")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Ready'),
        ('qc_test', 'Inline Inspection'),
        ('confirm', 'Confirmed'),
        ('planned', 'Planned'),
        ('progress', 'In Progress'),
        ('qc_labeling', 'Labeling '),
        ('to_close', 'To Close'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')], string='State',
        compute='_compute_state', copy=False, index=True, readonly=True,
        store=True, tracking=True,
        help=" * Draft: The MO is not confirmed yet.\n"
             " * Confirmed: The MO is confirmed, the stock rules and the reordering of the components are trigerred.\n"
             " * Planned: The WO are planned.\n"
             " * In Progress: The production has started (on the MO or on the WO).\n"
             " * To Close: The production is done, the MO has to be closed.\n"
             " * Done: The MO is closed, the stock moves are posted. \n"
             " * Cancelled: The MO has been cancelled, can't be confirmed anymore.")

    def action_confirm(self):
        for i in self:
            i.state = 'confirmed'
        rec = super(AttachmentFields, self).action_confirm()

    def action_qc_testing(self):
        for i in self:
            i.state = 'qc_test'

    def action_assign(self):
        rec = super(AttachmentFields, self).action_assign()
        for i in self.move_raw_ids:
            if i.reserved_availability == 0:
                self.check = False
                break
            else:
                self.check = True

    def button_plan(self):
        """ Create work orders. And probably do stuff, like things. """
        orders_to_plan = self.filtered(lambda order: order.routing_id and order.state in ['confirm'])
        for order in orders_to_plan:
            order.move_raw_ids.filtered(lambda m: m.state == 'draft')._action_confirm()
            quantity = order.product_uom_id._compute_quantity(order.product_qty, order.bom_id.product_uom_id) / order.bom_id.product_qty
            boms, lines = order.bom_id.explode(order.product_id, quantity, picking_type=order.bom_id.picking_type_id)
            order._generate_workorders(boms)
            order._plan_workorders()
        return True

    def final_testing(self):
        for i in self:
            i.state = 'qc_labeling'

    def confirmation(self):
        for i in self:
            i.state = 'confirm'


