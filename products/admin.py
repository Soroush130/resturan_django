from django.contrib import admin

# Register your models here.
from products.models import Products, CategoryProducts, Gallery


class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'title', 'price', 'active']

    class Meta:
        model = Products


admin.site.register(CategoryProducts)
admin.site.register(Products, ProductAdmin)
admin.site.register( Gallery)
