from django.contrib import admin
from .models import *
admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(ProductTag)
admin.site.register(ProductMedia)
