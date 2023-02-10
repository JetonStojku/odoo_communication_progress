from odoo import fields, models, api


class CommprogKlient(models.Model):
    _name = 'commprog.klient'
    _description = 'Description'

    name = fields.Char(string="Emer", required=True)
    lastname = fields.Char(string='Mbiemer', required=True)
    age = fields.Integer(string='Mosha')
    cell = fields.Char(string='Celular', required=True)
