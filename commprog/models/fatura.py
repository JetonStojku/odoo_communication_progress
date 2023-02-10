from odoo import fields, models, api


class CommprogFatura(models.Model):
    _name = 'commprog.fatura'
    _description = 'Description'

    nr_fature = fields.Integer(string="Numri i fatures", required=True)
    data = fields.Datetime(string='Data', required=True)
    state = fields.Selection(string='State', required=True, default='draft',
                             selection=[('draft', 'Draft'),
                                        ('done', 'Konfirmuar'),
                                        ('cancel', 'Anulluar'),
                                        ])
    type = fields.Boolean(string='Tipi', required=True, default=False)
    klient_id = fields.Many2one(comodel_name='commprog.klient', string='Klient', required=True)
    # total = fields.Float(string='Total')


class CommprogRreshtFature(models.Model):
    _name = 'commprog.rresht.fature'
    _description = 'CommprogRreshtFature'

    produkt_id = fields.Many2one(comodel_name='commprog.produkt', string='Produkt', required=True)
    fatura_id = fields.Many2one(comodel_name='commprog.fatura', string='Fatura',
                                required=True, ondelete='cascade')
    cmimi = fields.Float(string='Cmimi', required=True)
    sasi = fields.Float(string='Sasi', required=True)
    # total = fields.Float(string='Total')
