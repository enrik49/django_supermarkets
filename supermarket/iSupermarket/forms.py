from django.forms import ModelForm
from models import Client, Companyia, Marca, Producte, Sucursal

class ClientForm(ModelForm):
    class Meta:
        model = Client
        exclude = ('registration_date',)

class CompanyiaForm(ModelForm):
    class Meta:
        model = Companyia
        exclude =()

class MarcaForm(ModelForm):
    class Meta:
        model = Marca
        exclude =()

class ProducteForm(ModelForm):
    class Meta:
        model = Producte
        exclude =()

class SucursalForm(ModelForm):
    class Meta:
        model = Sucursal
        exclude =()