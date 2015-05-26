from django.forms import ModelForm
from models import Client, Companyia, Marca, Producte, Sucursal

class ClientForm(ModelForm):
    class Meta:
        model = Client
        exclude = ('registration_date','user')

class CompanyiaForm(ModelForm):
    class Meta:
        model = Companyia
        exclude = ('user',)

class MarcaForm(ModelForm):
    class Meta:
        model = Marca
        exclude =('user',)

class ProducteForm(ModelForm):
    class Meta:
        model = Producte
        exclude =('user',)

class SucursalForm(ModelForm):
    class Meta:
        model = Sucursal
        exclude =('user',)
