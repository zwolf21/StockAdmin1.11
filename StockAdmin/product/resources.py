from import_export import resources, fields
from import_export.widgets import ManyToManyWidget, ForeignKeyWidget

from .models import Product, Market


class ProductResourceAdmin(resources.ModelResource):
	markets = fields.Field(attribute='markets', column_name='markets', widget=ManyToManyWidget(Market, field='name'))

	class Meta:
		model = Product
		import_id_fields = 'code',
		exclude = 'id', 'updated', 'created', 
		export_order = 'name', 'code', 'price', 'markets'


class MarketResourceAdmin(resources.ModelResource):

	class Meta:
		model = Market
		import_id_fields = 'name',
		export_order = 'name', 'tel', 'fax',
		exclude = 'id', 'created', 'updated',