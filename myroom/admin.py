from django.contrib import admin
from . import models


admin.site.register(models.Furniture)
admin.site.register(models.MyFurniture)
admin.site.register(models.FurniturePosition)
admin.site.register(models.GuestBook)