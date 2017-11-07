from django.contrib import admin

from .models import BuyProfile, StockProfile


@admin.register(BuyProfile)
class BuyProfileAdmin(admin.ModelAdmin):
    list_display = 'product', 'market', 'buy_price', 'box_amount', 'buy_unit', 'buybox', 'active',
    list_filter = 'active', 'market', 'buy_unit',
    search_fields = 'product__name', 'market__name',
    list_editable = 'buy_price', 'box_amount', 'buy_unit', 'buybox', 'active',



@admin.register(StockProfile)
class StockProfileAdmin(admin.ModelAdmin):
	list_display = 'product', 'pkg_amount', 'std_unit',
	list_filter = 'std_unit',
	search_fields = 'product__name',
