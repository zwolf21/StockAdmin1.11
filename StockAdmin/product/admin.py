from django.contrib import admin

from .models import Market, Product
from .resources import ProductResourceAdmin, MarketResourceAdmin

from import_export.admin import ImportExportModelAdmin


@admin.register(Market)
class MarketAdmin(ImportExportModelAdmin):
    list_display = 'name', 'tel', 'fax',
    resource_class = MarketResourceAdmin


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    list_display = 'name', 'code', 'std_price', 'market',
    search_fields = 'name',
    resource_class = ProductResourceAdmin


    def market(self, instance):
    	return ', '.join(n.name for n in instance.markets.all())
    market.short_description = '도매상'


