from odoo import fields, models, api
from odoo.exceptions import UserError


class CommprogProdukt(models.Model):
    _name = 'commprog.produkt'
    _description = 'Description'

    name = fields.Char(string="Produkti", required=True)
    cmim_shitje = fields.Float(string='Cmim shitje', required=True)
    cmim_blerje = fields.Float(string='Cmim blerje', required=True)
    sasi = fields.Float(string='Sasi', required=True)
    kosto = fields.Float(string='Kosto', required=True)
    kategori_ids = fields.Many2many(comodel_name='commprog.kategori', string='Kategoria')

    def create(self, values):
        if values["sasi"] < 0:
            raise UserError("Sasi nuk mund të jetë negative")
        res = super(CommprogProdukt, self).create(values)
        # if res.sasi < 0:
        #     raise UserError("Sasi nuk mund të jetë negative")
        return res

    def write(self, values):
        # sasi = values.get('sasi', self.sasi)
        # if sasi < 0:
        #     raise UserError(f"Sasi nuk mund të jetë negative për produktin")
        res = super(CommprogProdukt, self).write(values)
        for rec in self:
            if rec.sasi < 0:
                raise UserError(f"Sasi nuk mund të jetë negative për produktin {rec.name}")
        return res


class CommprogKategori(models.Model):
    _name = 'commprog.kategori'
    _description = 'CommprogKategori'
    _rec_name = "emri"

    emri = fields.Char(string="Emrërtimi i kategorisë")
