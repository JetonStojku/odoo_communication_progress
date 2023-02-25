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
    total = fields.Float(string='Total', compute='_compute_total', store=True)
    rresht_fature_ids = fields.One2many(comodel_name='commprog.rresht.fature',
                                        inverse_name='fatura_id', string='Rresht fature')

    @api.depends('rresht_fature_ids')
    def _compute_total(self):
        for rec in self:
            rec.total = sum(rec.rresht_fature_ids.mapped('total'))

    def aprovo(self):
        self.state = "done"

    def anullo(self):
        self.state = "cancel"

    def draft(self):
        self.state = "draft"


class CommprogRreshtFature(models.Model):
    _name = 'commprog.rresht.fature'
    _description = 'CommprogRreshtFature'

    produkt_id = fields.Many2one(comodel_name='commprog.produkt', string='Produkt', required=True)
    fatura_id = fields.Many2one(comodel_name='commprog.fatura', string='Fatura',
                                required=True, ondelete='cascade')
    cmimi = fields.Float(string='Cmimi', required=True)
    sasi = fields.Float(string='Sasi', required=True, default=1)
    total = fields.Float(string='Total', compute='_compute_total')

    @api.depends('cmimi', 'sasi')
    def _compute_total(self):
        for rec in self:
            rec.total = rec.cmimi * rec.sasi

    @api.onchange('produkt_id')
    def onchange_produkt_id(self):
        self.cmimi = self.produkt_id.cmim_shitje
