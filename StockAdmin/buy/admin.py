from django.contrib import admin

from .models import Buy, BuyItem


@admin.register(Buy)
class BuyAdmin(admin.ModelAdmin):
    list_display = 'slug', 'date',
    list_filter = 'date',


@admin.register(BuyItem)
class BuyItemAdmin(admin.ModelAdmin):
    list_display = 'buy', 'item', 'amount'
    list_filter = 'buy',

