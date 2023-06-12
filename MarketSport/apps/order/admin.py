from django.contrib import admin
from .models import *


class OrderItemAdmin(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrederAdmin(admin.ModelAdmin):
    list_display = ['id','name','address','mobile','paid_amount','paid']
    inlines = [OrderItemAdmin]


admin.site.register(Order, OrederAdmin)
admin.site.register(OrderItem)
