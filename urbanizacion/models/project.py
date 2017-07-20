# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Project(models.Model):
    _inherit = 'project.project'

    note = fields.Char(
        string = 'Descripcion'
    )
    module = fields.Char(
        string='Módulo'
    )