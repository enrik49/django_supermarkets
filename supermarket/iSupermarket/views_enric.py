from django.views.generic.edit import CreateView
from models import Client, Companyia, Marca, Producte, Sucursal
from forms import *

class ClientCreate(CreateView):
    model = Client
    template_name = 'form_client.html'
    form_class = ClientForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ClientCreate, self).form_valid(form)

class CompanyiaCreate(CreateView):
    model = Companyia
    template_name = 'form_companyia.html'
    form_class = CompanyiaForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CompanyiaCreate, self).form_valid(form)

class MarcaCreate(CreateView):
    model = Marca
    template_name = 'form_marca.html'
    form_class = MarcaForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(MarcaCreate, self).form_valid(form)

class ProducteCreate(CreateView):
    model = Producte
    template_name = 'form_producte.html'
    form_class = ProducteForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ProducteCreate, self).form_valid(form)

class SucursalCreate(CreateView):
    model = Sucursal
    template_name = 'form_sucursal.html'
    form_class = SucursalForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(SucursalCreate, self).form_valid(form)