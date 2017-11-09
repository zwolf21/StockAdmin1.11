from django.contrib import admin

from .models import Buy, BuyItem, BuyStock


@admin.register(Buy)
class BuyAdmin(admin.ModelAdmin):
    list_display = 'buy_num', 'buy_date',
    list_filter = 'buy_date',


@admin.register(BuyItem)
class BuyItemAdmin(admin.ModelAdmin):
    list_display = 'buy', 'item', 'buy_amount', 'stocked_amount', 'completed', 'incompleted_amount', 'force_end',
    list_filter = 'buy',



@admin.register(BuyStock)
class BuyStockAdmin(admin.ModelAdmin):
	list_display = 'buyitem', 'stock_amount', 'stock_date',
	list_filter = 'buyitem__buy',
