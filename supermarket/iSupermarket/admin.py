from .models import *
from django.contrib import admin

class AdminClient(admin.ModelAdmin):
    list_display = ['name','lastName','registration_date','was_registred_recently']
    fieldsets = [
    ('User information',{'fields':['name','lastName','phone','user']}),
    (None,{'fields':['registration_date',],'classes': ['collapse']}),
    ]


admin.site.register(Client, AdminClient)

class AdminCompanyia(admin.ModelAdmin):
    list_display = ['name','idNumber']
    fieldsets = [
    (None,{'fields':['name']}),
    (None,{'fields':['idNumber','user']}),
    ]
admin.site.register(Companyia,AdminCompanyia)

class AdminSucursal(admin.ModelAdmin):
    list_display=['name','StateOrProvince','country','companyia']
    fieldsets = [
    ('Sucursal information',{'fields':['name','location','zipCode','StateOrProvince','country']}),
    (None,{'fields':['companyia','user']}),
    ]
admin.site.register(Sucursal,AdminSucursal)    
        


class AdminProducte(admin.ModelAdmin):
    list_display=['name','marca']
    fieldsets = [
    (None,{'fields':['name']}),
    (None,{'fields':['marca']}),

    ]
admin.site.register(Marca)
admin.site.register(Producte,AdminProducte)
admin.site.register(SucursalReview)

"""admin.site.register(models.Companyia)
admin.site.register(models.Sucursal)
admin.site.register(models.Client)
admin.site.register(models.Marca)
admin.site.register(models.Producte)
"""
