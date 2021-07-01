# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, _ , api


class ShippingCategories(models.Model):
    _name = 'shipping.categories'

    name=fields.Char(string="Name")
    shipper=fields.Many2one('res.partner',string="Shipper")
    items=fields.One2many('shipping.relation','x')


class ShippingCategoriesrelations(models.Model):
    _name = 'shipping.relation'

    x=fields.Many2one('shipping.categories')
    name=fields.Char(string="Item Name")
    code=fields.Integer(string="Code")
    intercode=fields.Integer(string="International Code")
    description=fields.Char(string="Description")
