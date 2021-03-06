# This file is part product_price_group module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from . import product


def register():
    Pool.register(
        product.Template,
        product.Product,
        module='product_price_group', type_='model')
    Pool.register(
        product.ProductSupplier,
        module='product_price_group', type_='model',
        depends='purchase')
