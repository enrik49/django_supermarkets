# Create your views here.
from django.core.urlresolvers import reverse
from django.core import urlresolvers
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateResponseMixin
from django.core import serializers

from models import Client, Companyia, Marca, Producte, Sucursal
#from forms import ClientForm
from views_enric import *


class ConnegResponseMixin(TemplateResponseMixin):

    def render_json_object_response(self, objects, **kwargs):
        json_data = serializers.serialize(u"json", objects, **kwargs)
        return HttpResponse(json_data, content_type=u"application/json")

    def render_xml_object_response(self, objects, **kwargs):
        xml_data = serializers.serialize(u"xml", objects, **kwargs)
        return HttpResponse(xml_data, content_type=u"application/xml")

    def render_to_response(self, context, **kwargs):
        if 'extension' in self.kwargs:
            try:
                objects = [self.object]
            except AttributeError:
                objects = self.object_list
            if self.kwargs['extension'] == 'json':
                return self.render_json_object_response(objects=objects)
            elif self.kwargs['extension'] == 'xml':
                return self.render_xml_object_response(objects=objects)
        else:
            return super(ConnegResponseMixin, self).render_to_response(context)

class Inici(ListView):
    model = Client #Aixo ha de quedar aixi ara que ja no llistem sol clients.
    template_name = 'index.html'
    queryset = Client.objects.all() #Comentari = al anterior.

class Clients(ListView,ConnegResponseMixin):
    model = Client
    template_name = 'clients.html'
    queryset = Client.objects.all()
    context_object_name='clients_list'

class Companyias(ListView,ConnegResponseMixin):
    model = Companyia
    template_name = 'companyia.html'
    queryset = Companyia.objects.all()
    context_object_name='Companyia_list'

class Sucursals(ListView,ConnegResponseMixin):
    model = Sucursal
    template_name = 'sucursal.html'
    queryset = Sucursal.objects.all()
    context_object_name='Sucursal_list'

class Marcas(ListView,ConnegResponseMixin):
    model = Marca
    template_name = 'marca.html'
    queryset = Marca.objects.all()
    context_object_name='Marca_list'

class Productes(ListView,ConnegResponseMixin):
    model = Producte
    template_name = 'producte.html'
    queryset = Producte.objects.all()
    context_object_name='Producte_list'

class ClientDetail(DetailView,ConnegResponseMixin):
    model = Client
    template_name = 'detail_client.html'

    def get_context_data(self, **kwargs):
       context = super(ClientDetail, self).get_context_data(**kwargs)
       return context

class CompanyiaDetail(DetailView,ConnegResponseMixin):
    model = Companyia
    template_name = 'detail_companyia.html'

    def get_context_data(self, **kwargs):
       context = super(CompanyiaDetail, self).get_context_data(**kwargs)
       return context


class SucursalDetail(DetailView,ConnegResponseMixin):
    model = Sucursal
    template_name = 'detail_sucursal.html'

    def get_context_data(self, **kwargs):
       context = super(SucursalDetail, self).get_context_data(**kwargs)
       return context

class MarcaDetail(DetailView,ConnegResponseMixin):
    model = Marca
    template_name = 'detail_marca.html'

    def get_context_data(self, **kwargs):
        context = super(MarcaDetail, self).get_context_data(**kwargs)
        return context


class ProducteDetail(DetailView,ConnegResponseMixin):
    model = Producte
    template_name = 'detail_producte.html'

    def get_context_data(self, **kwargs):
        context = super(ProducteDetail, self).get_context_data(**kwargs)
        return context

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