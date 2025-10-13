# -*- coding: utf-8 -*-
from odoo import api, fields, models


class MaintenanceRequest(models.Model):
    _inherit = 'maintenance.request'

    # Campo computado para saber si mostrar vendor
    show_vendor = fields.Boolean(
        compute='_compute_show_vendor',
        store=False
    )

    @api.depends_context('uid')
    def _compute_show_vendor(self):
        """Determina si se debe mostrar el vendor según configuración"""
        icp = self.env['ir.config_parameter'].sudo()
        view_vendor = icp.get_param('maintenance_custom_fela.view_vendor', default='1')
        show = (view_vendor == '1')
        for record in self:
            record.show_vendor = show