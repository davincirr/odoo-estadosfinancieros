# -*- coding: utf-8 -*-
from odoo import api, fields, models

class EjPet(models.Model):
    _name = 'ej.pet'
    name = fields.Char(string='Nombre o Razon Social', required=True)
    cedula = fields.Char(string='Cedula o Nit')
    cc = fields.Char(string='cc')
    razonsocial = fields.Char(string='Razon Social')
    age = fields.Char(string='Teléfono')
    color = fields.Char(string='Correo')
    activo = fields.Integer(string='Activo')
    pasivo = fields.Integer(string='Pasivo')
    patrimonio = fields.Integer(string='Patrimonio',compute='_calcular_patrimonio', store=True)
    
    @api.depends('activo', 'pasivo')
    def _calcular_patrimonio(self):
        for record in self:
            record.patrimonio = record.activo - record.pasivo
    
