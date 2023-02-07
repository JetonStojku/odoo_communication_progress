from odoo import fields, models, api


class AacommprogFatura(models.Model):
    _name = 'aacommprog.fatura'
    _description = 'Description'

    nr_fature = fields.Integer(string="Numri i fatures", required=True)
    data = fields.Datetime(string='Data', required=True)
    state = fields.Selection(string='State', required=True, default='draft',
                             selection=[('draft', 'Draft'),
                                        ('done', 'Konfirmuar'),
                                        ('cancel', 'Anulluar'),
                                        ])
    type = fields.Boolean(string='Tipi', required=True, default=False)
    klient_id = fields.Many2one(comodel_name='aacommprog.klient', string='Klient', required=True)
    # total = fields.Float(string='Total')


class AacommprogRreshtFature(models.Model):
    _name = 'aacommprog.rresht.fature'
    _description = 'AacommprogRreshtFature'

    produkt_id = fields.Many2one(comodel_name='aacommprog.produkt', string='Produkt', required=True)
    fatura_id = fields.Many2one(comodel_name='aacommprog.fatura', string='Fatura',
                                required=True, ondelete='cascade')
    cmimi = fields.Float(string='Cmimi', required=True)
    sasi = fields.Float(string='Sasi', required=True)
    # total = fields.Float(string='Total')
