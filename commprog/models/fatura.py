from odoo import fields, models, api
from odoo.exceptions import UserError


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
        koef = 1 if self.type else -1
        for rec in self.rresht_fature_ids:
            rec.produkt_id.sasi += koef * rec.sasi

    def anullo(self):
        self.state = "cancel"
        koef = -1 if self.type else 1
        for rec in self.rresht_fature_ids:
            rec.produkt_id.sasi += koef * rec.sasi

    def draft(self):
        self.state = "draft"

    def unlink(self):
        for rec in self:
            if rec.state != 'draft':
                raise UserError("Mund të fshihen vetëm faturat në draft!")
        return super(CommprogFatura, self).unlink()


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
