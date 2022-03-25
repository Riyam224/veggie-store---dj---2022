from django.contrib import admin

# Register your models here.
from .models import Product, Category , Team , Newsletter

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Team)
admin.site.register(Newsletter)