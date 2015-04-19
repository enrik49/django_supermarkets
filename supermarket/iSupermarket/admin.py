from .models import Client, Companyia, Marca, Producte, Sucursal
from django.contrib import admin

class AdminClient(admin.ModelAdmin):
    fieldsets = [
    ('User information',{'fields':['name','lastName','phone']}),
    (None,{'fields':['registration_date'],'classes': ['collapse']}),
    ]

admin.site.register(Client, AdminClient)

class AdminCompanyia(admin.ModelAdmin):
    fieldsets = [
    (None,{'fields':['name']}),
    (None,{'fields':['idNumber']}),
    ]
admin.site.register(Companyia,AdminCompanyia)

admin.site.register(Sucursal)



'''class AdminProducte(admin.ModelAdmin):
    fieldsets = [
    (None,{'fields':['name']}),
    (None,{'fields':['Marca']}),

    ]'''
admin.site.register(Marca)
admin.site.register(Producte)

"""admin.site.register(models.Companyia)
admin.site.register(models.Sucursal)
admin.site.register(models.Client)
admin.site.register(models.Marca)
admin.site.register(models.Producte)
"""
