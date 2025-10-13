{
    "name": "Maintenance Custom Fela",
    "summary": "Extensiones de configuración para Maintenance (view_vendor 0/1)",
    "version": "18.0.1.0.0",
    "author": "Tu Empresa",
    "website": "",
    "category": "Maintenance",
    "license": "LGPL-3",
    "depends": [
        "maintenance",
        "dev_maintenance_purchase_agreement",
    ],
    "data": [
        "views/res_config_settings_views.xml",
        "views/maintenance_request_views.xml",
        "views/maintenance_request_vendor_views.xml",
    ],
    "application": True,
    "installable": True,
    "auto_install": False,
}
