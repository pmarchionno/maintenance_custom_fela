# -*- coding: utf-8 -*-
from odoo import api, fields, models

PARAM_KEY = "maintenance_custom_fela.view_vendor"

class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    # Checkbox en UI; se persistirá como '0'/'1' en ir.config_parameter
    view_vendor = fields.Boolean(
        string="Ver Proveedor en Maintenance",
        config_parameter=False,  # lo manejamos manualmente para guardar '0'/'1'
        help="Si está activo, el parámetro del sistema se guarda como '1'; si no, como '0'."
    )

    @api.model
    def get_values(self):
        res = super().get_values()
        icp = self.env["ir.config_parameter"].sudo()
        raw = icp.get_param(PARAM_KEY, default="1")  # por defecto '1'
        res.update(
            view_vendor=(raw == "1")
        )
        return res

    def set_values(self):
        super().set_values()
        icp = self.env["ir.config_parameter"].sudo()
        icp.set_param(PARAM_KEY, "1" if self.view_vendor else "0")
