# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import PoolMeta
from trytond.pyson import Id, Eval

__all__ = ['Template', 'Product', 'ProductSupplier']


class Template:
    __name__ = 'product.template'
    __metaclass__ = PoolMeta

    @classmethod
    def __setup__(cls):
        super(Template, cls).__setup__()

        # cost price
        invisible_cost_price =  ~Eval('groups', []).contains(
                Id('product_price_group', 'group_product_cost_price'))
        if 'invisible' not in cls.cost_price.states:
            cls.cost_price.states['invisible'] = invisible_cost_price
        else:
            cls.cost_price.states['invisible'] &= invisible_cost_price

        # list price
        invisible_list_price =  ~Eval('groups', []).contains(
                Id('product_price_group', 'group_product_list_price'))
        if 'invisible' not in cls.list_price.states:
            cls.list_price.states['invisible'] = invisible_list_price
        else:
            cls.list_price.states['invisible'] &= invisible_list_price


class Product:
    __name__ = 'product.product'
    __metaclass__ = PoolMeta

    @classmethod
    def __setup__(cls):
        super(Product, cls).__setup__()

        # cost price
        invisible_cost_price =  ~Eval('groups', []).contains(
                Id('product_price_group', 'group_product_cost_price'))
        if 'invisible' not in cls.cost_price.states:
            cls.cost_price.states['invisible'] = invisible_cost_price
        else:
            cls.cost_price.states['invisible'] &= invisible_cost_price

        # list price
        invisible_list_price =  ~Eval('groups', []).contains(
                Id('product_price_group', 'group_product_list_price'))
        if 'invisible' not in cls.list_price.states:
            cls.list_price.states['invisible'] = invisible_list_price
        else:
            cls.list_price.states['invisible'] &= invisible_list_price


class ProductSupplier:
    __name__ = 'purchase.product_supplier'
    __metaclass__ = PoolMeta

    @classmethod
    def __setup__(cls):
        super(ProductSupplier, cls).__setup__()

        # supplier prices
        invisible_prices =  ~Eval('groups', []).contains(
                Id('product_price_group', 'group_product_cost_price'))
        if 'invisible' not in cls.prices.states:
            cls.prices.states['invisible'] = invisible_prices
        else:
            cls.prices.states['invisible'] &= invisible_prices
