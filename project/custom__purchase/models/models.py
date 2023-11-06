from odoo import models, fields, api
from datetime import date, datetime


class PurchaseRequest(models.Model):
    _name = 'purchase_order'
    _description = "NEW"
    name = fields.Char()
    value = fields.Integer()
    description = fields.Text()
    New = fields.Many2one('account.account', string="Account")
    user_id = fields.Many2one('res.users', default=lambda self: self.env.user.id, string="Requested by")
    requested = fields.Date(default=date.today(), string="Requested on")
    PurchaseRequestLines_ids = fields.One2many('purchase_liens', 'liens_id')

    state = fields.Selection(selection=[
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
    ], string='Status', required=True, readonly=True, copy=False,
        tracking=True, default='draft')

    def action_draft(self):
        for rec in self:
            rec.state = 'draft'

    def action_done(self):
        for rec in self:
            rec.state = 'confirmed'

    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100


class PurchaseRequestLine(models.Model):
    _name = 'purchase_liens'
    liens_id = fields.Many2one('purchase_order')
    product_id = fields.Many2one('product.product', string='product')
    vendor_id = fields.Many2one('res.partner', string="vendor")
    quantity = fields.Float(string="Quantity")
    product_uom = fields.Many2one('uom.uom', string='Unit of Measure',
                                  domain="[('category_id', '=', product_uom_category_id)]")
    product_uom_category_id = fields.Many2one(related='product_id.uom_id.category_id')
    product_id = fields.Many2one('product.product', string='Product',
                                 change_default=True, index='btree_not_null')
