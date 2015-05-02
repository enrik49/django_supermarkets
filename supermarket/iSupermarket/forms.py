from django.forms import ModelForm
from models import Client, Companyia, Marca, Producte, Sucursal

class ClientForm(ModelForm):
    class Meta:
        model = Client
        exclude = ('registration_date',)

class CompanyiaForm(ModelForm):
    class Meta:
        model = Companyia

class MarcaForm(ModelForm):
    class Meta:
        model = Marca

class ProducteForm(ModelForm):
    class Meta:
        model = Producte

class SucursalForm(ModelForm):
    class Meta:
        model = Sucursal