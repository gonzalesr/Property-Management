# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Property(models.Model):
    _inherit = 'product.product'

    urbanization = fields.Many2one(
        'project.project',
        string='Urbanización',
    )
    block= fields.Many2one(
        'block.project',
        string='Manzano'
    )
    category = fields.Selection(
        string='Categoria',
        selection=[
            ('a', 'A'),
            ('b', 'B'),
            ('c', 'C'),
        ],
        default='a',
    )

    sup_lote = fields.Float(
        string='Superficie Terreno', digit=(12,4)
    )
    sup_const = fields.Float(
        string='Superficie de Const', digit=(12,4), help="Superficie de Construcción"
    )
    tip_const = fields.Char(
        string = 'Tipologia de Const', help='Tipología de Construcción'
    )
    mat_real = fields.Char(
        string = 'Matricula Real'
    )

    precio_m = fields.Float(
        string = 'Precio x m2',
        digit = (12,4)
    )
    precio_sup_const = fields.Float(
        string = 'Precio Sup Const',
        digit = (12,4), help = 'Precio por superficie construida'
    )
    estatus = fields.Selection(
        string='Estado',
        selection=[
            ('libre', 'Libre'),
            ('reservado', 'Reservado'),
            ('bloqueado', 'Bloqueado'),
            ('vendido', 'Vendido'),
        ],
        default='libre',
    )
    observacion = fields.Text(
        string = 'Observación'
    )
