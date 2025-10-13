# -*- coding: utf-8 -*-
from odoo import api, fields, models

class MaintenanceRequest(models.Model):
    _inherit = 'maintenance.request'

    show_vendor = fields.Boolean(
        string='Mostrar proveedor',
        compute='_compute_show_vendor',
        compute_sudo=True,   # lee los parámetros globales sin problemas de permisos
        store=False          # no se guarda en BD, se calcula cada vez
    )

    @api.depends_context('uid')
    def _compute_show_vendor(self):
        """Lee el parámetro global guardado en Configuración (Res Config Settings)."""
        icp = self.env['ir.config_parameter'].sudo()
        view_vendor = icp.get_param('maintenance_custom_fela.view_vendor', default='1')
        show = (view_vendor == '1')
        for record in self:
            record.show_vendor = show
