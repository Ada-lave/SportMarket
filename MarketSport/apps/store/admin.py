from django.contrib import admin

from .models import *

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

    list_display = ['title','category','price','date_add','avalible']
    list_filter = ('category','price','date_add')
    
    

   


admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
