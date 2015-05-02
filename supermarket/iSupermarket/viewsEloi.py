from django.core.urlresolvers import reverse
from django.core import urlresolvers
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView

from models import Client, Companyia, Marca, Producte, Sucursal

class CompanyiaDetail(DetailView):
    model = Companyia
    template_name = 'detail_companyia.html'

    def get_context_data(self, **kwargs):
       context = super(CompanyiaDetail, self).get_context_data(**kwargs)
       return context


class SucursalDetail(DetailView):
    model = Sucursal
    template_name = 'detail_sucursal.html'

    def get_context_data(self, **kwargs):
       context = super(SucursalDetail, self).get_context_data(**kwargs)
       return context

class MarcaDetail(DetailView):
	model = Marca
	template_name = 'detail_marca.html'

	def get_context_data(self, **kwargs):
		context = super(MarcaDetail, self).get_context_data(**kwargs)
		return context


class ProducteDetail(DetailView):
	model = Producte
	template_name = 'detail_producte.html'

	def get_context_data(self, **kwargs):
		context = super(ProducteDetail, self).get_context_data(**kwargs)
		return context