from django.contrib import admin
from .models import User, Category, Product, Beet

# Register your models here.
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Beet)
