# Copyright 2020 Akretion (https://www.akretion.com).
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).


{
    "name": "Delivery Carrier Info",
    "summary": "Add code and description on carrier",
    "version": "14.0.1.0.0",
    "category": "Delivery",
    "website": "www.akretion.com",
    "author": "Akretion,Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    "depends": [
        "delivery",
    ],
    "data": ["views/delivery_view.xml"],
    "demo": [],
    "qweb": [],
}
