from django.contrib import admin
from sales.models import Customer,Order,Price

# Register your models here.
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Price)
