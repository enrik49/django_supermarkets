# Create your views here.
from django.core.urlresolvers import reverse, reverse_lazy
from django.core import urlresolvers
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView, DeleteView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.base import TemplateResponseMixin
from django.core import serializers
from rest_framework import routers, serializers, viewsets

from models import Client, Companyia, Marca, Producte, Sucursal
from forms import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from rest_framework import generics, permissions
from serializers import *

from django.shortcuts import render, render_to_response, RequestContext


class LoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)

class CheckIsOwnerMixin(object):
    def get_object(self, *args, **kwargs):
        obj = super(CheckIsOwnerMixin, self).get_object(*args, **kwargs)
        if not obj.user == self.request.user:
            raise PermissionDenied
        return obj


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

class Clients(LoginRequiredMixin,ListView,ConnegResponseMixin):
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

def ProducteCreate2(request):
    if request.method == 'POST':
        formulario = ProducteForm2(request.user, request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/app/Producte')
    else:
        formulario = ProducteForm2(request.user)
    return render_to_response('form_producte.html',{'form':formulario},context_instance=RequestContext(request))

class SucursalCreate(CreateView):
    model = Sucursal
    template_name = 'form_sucursal.html'
    form_class = SucursalForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(SucursalCreate, self).form_valid(form)

def SucursalCreate2(request):
    if request.method == 'POST':
        formulario = SucursalForm2(request.user, request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/app/Sucursal')
    else:
        formulario = SucursalForm2(request.user)
    return render_to_response('form_sucursal.html',{'form':formulario},context_instance=RequestContext(request))

class UserCreate(CreateView):
    model = User
    template_name = 'form_user.html'
    form_class = UserCreationForm
    success_url = "/app"

    def form_valid(self,form):
        return super(UserCreate,self).form_valid(form)

class ClientUpdate(UpdateView):
	model=Client
	template_name = 'update_client.html'
	form_class = ClientForm

class ClientDelete(DeleteView):
	model = Client
	success_url = "/app/Client"
	template_name = 'delete_client.html'

class CompanyiaUpdate(UpdateView):
	model=Companyia
	template_name = 'update_companyia.html'
	form_class = CompanyiaForm

class CompanyiaDelete(DeleteView):
	model = Companyia
	success_url = "/app/Companyia"
	template_name = 'delete_companyia.html'

class SucursalUpdate(UpdateView):
    model=Sucursal
    template_name = 'update_sucursal.html'
    form_class = SucursalForm

def SucursalUpdate2(request,pk):
    sucursal = Sucursal.objects.get(id=pk)
    if request.method == 'POST':
        formulario = SucursalForm2(sucursal.user, request.POST, instance=sucursal)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/app/Sucursal')
    else:
        formulario = SucursalForm2(sucursal.user, instance=sucursal)
    return render_to_response('update_sucursal.html',{'form':formulario},context_instance=RequestContext(request))


class SucursalDelete(DeleteView):
    model = Sucursal
    success_url = "/app/Sucursal"
    template_name = 'delete_sucursal.html'


class MarcaUpdate(UpdateView):
    model=Marca
    template_name = 'update_marca.html'
    form_class = MarcaForm

class MarcaDelete(DeleteView):
    model = Marca
    success_url = "/app/Marca"
    template_name = 'delete_marca.html'

class ProducteUpdate(UpdateView):
    model=Producte
    template_name = 'update_producte.html'
    form_class = ProducteForm


def ProducteUpdate2(request,pk):
    producte = Producte.objects.get(id=pk)
    if request.method == 'POST':
        formulario = ProducteForm2(producte.user, request.POST, instance=producte)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/app/Producte')
    else:
        formulario = ProducteForm2(producte.user, instance=producte)
    return render_to_response('update_producte.html',{'form':formulario},context_instance=RequestContext(request))

class ProducteDelete(DeleteView):
    model = Producte
    success_url = "/app/Producte"
    template_name = 'delete_producte.html'






class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.user == request.user

class APIClientList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Client
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class APIClientDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Client
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
