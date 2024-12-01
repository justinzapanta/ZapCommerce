from django.contrib import admin
from . import models

# Register your models here.
admin.site.register([
    
    models.Products,
    models.Cart,
    models.Transaction,
    models.User_info
])