from django.conf.urls import patterns, include, url
from models import *
#from filmApplication.forms import ActorForm, DirectorForm, MovieForm, ReviewForm
from views import *
from django.contrib import admin
from viewsEloi import *
#from forms import ClientForm


admin.autodiscover()

urlpatterns = patterns('',
	#Url de inici
    url(r'^$', Inici.as_view(),),
    url(r'^Client/$',Clients.as_view(),name="client_list"),
    url(r'^Marca/$',Marcas.as_view(),name="marca_list"),
    url(r'^Producte/$',Productes.as_view(),name="producte_list"),
    url(r'^Companyia/$',Companyias.as_view(),name="companyia_list"),
    url(r'^Sucursal/$',Sucursals.as_view(),name="sucursal_list"),
    url(r'^Client/(?P<pk>\d+)/$',ClientDetail.as_view(),name='client_detail'),
    url(r'^Companyia/(?P<pk>\d+)/$',CompanyiaDetail.as_view(),name='companyia_detail'),
    url(r'^Sucursal/(?P<pk>\d+)/$',SucursalDetail.as_view(),name='sucursal_detail'),
    url(r'^Marca/(?P<pk>\d+)/$',MarcaDetail.as_view(), name='marca_detail'),
    url(r'^Producte/(?P<pk>\d+)/$',ProducteDetail.as_view(), name = 'producte_detail'),
    url(r'^Client/create/$',ClientCreate.as_view(),name='client_create'),
    url(r'^Producte/create/$',ProducteCreate.as_view(),name='producte_create'),
    url(r'^Marca/create/$',MarcaCreate.as_view(),name='marca_create'),
    url(r'^Sucursal/create/$',SucursalCreate.as_view(),name='sucursal_create'),
    url(r'^Companyia/create/$',CompanyiaCreate.as_view(),name='companyia_create'),
)
