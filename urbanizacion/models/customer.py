# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Customer(models.Model):
    _inherit = 'res.partner'

    apod_legal = fields.Char(
        string='Apoderado Legal'
    )
    ci = fields.Char(
        string='Doc de Identidad'
    )
    ci_exp = fields.Selection(
        string='Expedido en',
        selection=[
            ('BE', 'BENI'),
            ('CH', 'CHUQUISACA'),
            ('CBBA', 'COCHABAMBA'),
            ('LP', 'LA PAZ'),
            ('OR', 'ORURO'),
            ('PN', 'PANDO'),
            ('PT', 'POTOSI'),
            ('SC', 'SANTA CRUZ'),
            ('TJ', 'TARIJA'),
        ]

    )
    est_civil = fields.Selection(
        string = 'Estado Civil',
        selection = [
            ('soltero','Soltero/a'),
            ('casado','Casado/a'),
            ('divorciado', 'Divorciado/a'),
            ('viudo', 'Viudo/a'),
            ('unionlib', 'Unión Libre'),
        ],
        default = 'soltero',
    )