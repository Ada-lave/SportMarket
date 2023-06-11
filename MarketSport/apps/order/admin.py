from django.contrib import admin
from .models import *


class OrderItemAdmin(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrederAdmin(admin.ModelAdmin):
    inlines = [OrderItemAdmin]


admin.site.register(Order, OrederAdmin)
admin.site.register(OrderItem)
