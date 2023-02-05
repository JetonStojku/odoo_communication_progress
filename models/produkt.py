from odoo import fields, models, api


class AacommprogProdukt(models.Model):
    _name = 'aacommprog.produkt'
    _description = 'Description'

    name = fields.Char(string="Produkti", required=True)
    cmim_shitje = fields.Float(string='Cmim shitje', required=True)
    cmim_blerje = fields.Float(string='Cmim blerje', required=True)
    sasi = fields.Float(string='Sasi', required=True)
    kosto = fields.Float(string='Kosto', required=True)
