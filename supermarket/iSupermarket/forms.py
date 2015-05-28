from django.forms import ModelForm, ModelChoiceField
from models import Client, Companyia, Marca, Producte, Sucursal
from django.contrib.auth.models import User

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

class ProducteForm2(ModelForm):
    user = User
    class Meta:
        model = Producte
        exclude =('user',)

    def __init__(self, user, *args, **kwargs):
        super(ProducteForm2, self).__init__(*args,**kwargs)
        self.user = user
        self.fields['marca'] = ModelChoiceField(Marca.objects.filter(user=user),to_field_name="id")

    def save(self):
        producte = super(ProducteForm2, self).save(commit=False)
        producte.user = self.user
        producte.save()
        return producte

class SucursalForm(ModelForm):
    class Meta:
        model = Sucursal
        exclude =('user',)


class SucursalForm2(ModelForm):
    user = User
    class Meta:
        model = Sucursal
        exclude =('user',)

    def __init__(self, user, *args, **kwargs):
        super(SucursalForm2, self).__init__(*args,**kwargs)
        self.user = user
        print user
        self.fields['companyia'] = ModelChoiceField(Companyia.objects.filter(user=user),to_field_name="id")

    def save(self):
        sucursal = super(SucursalForm2, self).save(commit=False)
        sucursal.user = self.user
        sucursal.save()
        return sucursal




