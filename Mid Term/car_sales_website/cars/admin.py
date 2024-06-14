from django.contrib import admin
from cars import models
# Register your models here.

class SelectBrand(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'slug']

admin.site.register(models.CarBrande, SelectBrand)
admin.site.register(models.CarModel)
admin.site.register(models.Comment)