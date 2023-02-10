from odoo import fields, models, api


class CommprogProdukt(models.Model):
    _name = 'commprog.produkt'
    _description = 'Description'

    name = fields.Char(string="Produkti", required=True)
    cmim_shitje = fields.Float(string='Cmim shitje', required=True)
    cmim_blerje = fields.Float(string='Cmim blerje', required=True)
    sasi = fields.Float(string='Sasi', required=True)
    kosto = fields.Float(string='Kosto', required=True)
    kategori_ids = fields.Many2many(comodel_name='commprog.kategori', string='Kategoria')


class CommprogKategori(models.Model):
    _name = 'commprog.kategori'
    _description = 'CommprogKategori'
    _rec_name = "emri"

    emri = fields.Char(string="Emrërtimi i kategorisë")
