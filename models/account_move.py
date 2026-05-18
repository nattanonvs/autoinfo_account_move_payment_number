from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = "account.move"

    payment_number = fields.Char(
        string="Payment Number",
        compute="_compute_payment_number",
        store=True,
        readonly=True
    )

    @api.depends('line_ids.matched_debit_ids', 'line_ids.matched_credit_ids')
    def _compute_payment_number(self):
        for move in self:
            payments = move._get_reconciled_payments()
            move.payment_number = ", ".join(payments.mapped("name")) if payments else ""
