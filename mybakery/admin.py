from django.contrib import admin
from  .models import Product,ContactMessage,MenuItem


# Register your models here.
admin.site.register(Product)
admin.site.register(ContactMessage)
admin.site.register(MenuItem)