from odoo import fields, models, api


class AacommprogFatura(models.Model):
    _name = 'aacommprog.fatura'
    _description = 'Description'

    nr_fature = fields.Integer(string="Numri i fatures", required=True)
    data = fields.Datetime(string='Data', required=True)
