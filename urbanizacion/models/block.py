# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Block(models.Model):
    _name = 'block.project'

    name = fields.Char(
        string = 'Nombre'
    )
    abrev = fields.Char(
        string = "Abreviaturas"
    )
    urbanization = fields.Many2one(
        'project.project',
        string='Urbanización'
    )
