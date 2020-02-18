from django.contrib import admin
from django.contrib.auth.models import Group

from pos.models import Product, Order, OrderItem, StoreDetails, Creditor


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'productname', 'quantity', 'price', 'sale_price', 'active', 'created_at', 'updated_at', 'picture')
    list_display_links = ('productname', 'quantity', 'price', 'sale_price', 'active', 'created_at', 'updated_at')
    search_fields = ('productname', 'created_at')
    list_filter = ('active',)
    list_per_page = 10


class OrderAdmin(admin.ModelAdmin):
    list_display = ('total_price', 'success', 'timestamp')
    list_display_links = ('total_price', 'success', 'timestamp')
    search_fields = ('total_price', 'success', 'timestamp')
    list_per_page = 10
    date_hierarchy = 'timestamp'


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'order', 'timestamp')
    list_display_links = ('product', 'order', 'timestamp')
    list_per_page = 10
    search_fields = ('product__productname',)
    date_hierarchy = 'timestamp'


class StoreDetailsAdmin(admin.ModelAdmin):
    list_display = ('store_name', 'store_logo')
    list_display_links = ('store_name', 'store_logo')
    list_per_page = 10


class CreditorAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'item_description', 'amount', 'quantity', 'payment_status', 'amount_paid', 'balance', 'date')
    list_display_links = ('customer_name', 'item_description', 'amount', 'quantity', 'payment_status', 'amount_paid', 'balance', 'date')
    search_fields = ('customer_name', 'item_description', 'amount', 'quantity', 'payment_status', 'amount_paid', 'balance', 'date')
    list_per_page = 10
    #prepopulated_fields = {'balance': ('amount',)}


admin.site.unregister(Group)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(StoreDetails, StoreDetailsAdmin)
admin.site.register(Creditor, CreditorAdmin)