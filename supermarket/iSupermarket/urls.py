from django.conf.urls import patterns, include, url
from models import *
#from filmApplication.forms import ActorForm, DirectorForm, MovieForm, ReviewForm
from views import *
from django.contrib import admin
from viewsEloi import *
#from forms import ClientForm

from django.conf.urls import patterns, url, include
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from rest_framework.urlpatterns import format_suffix_patterns


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
    url(r'^Client/(?P<pk>\d+)/edit/$',ClientUpdate.as_view(), name='client_update'),
    url(r'^Client/(?P<pk>\d+)/delete/$',ClientDelete.as_view(), name='client_delete'),
    url(r'^Companyia/(?P<pk>\d+)/$',CompanyiaDetail.as_view(),name='companyia_detail'),
    url(r'^Companyia/(?P<pk>\d+)/edit/$',CompanyiaUpdate.as_view(), name='companyia_update'),
    url(r'^Companyia/(?P<pk>\d+)/delete/$',CompanyiaDelete.as_view(), name='companyia_delete'),
    url(r'^Sucursal/(?P<pk>\d+)/$',SucursalDetail.as_view(),name='sucursal_detail'),
    url(r'^Sucursal/(?P<pk>\d+)/edit/$','iSupermarket.views.SucursalUpdate2', name='sucursal_update'),
    url(r'^Sucursal/(?P<pk>\d+)/delete/$',SucursalDelete.as_view(), name='sucursal_delete'),
    url(r'^Marca/(?P<pk>\d+)/$',MarcaDetail.as_view(), name='marca_detail'),
    url(r'^Marca/(?P<pk>\d+)/edit/$',MarcaUpdate.as_view(), name='marca_update'),
    url(r'^Marca/(?P<pk>\d+)/delete/$',MarcaDelete.as_view(), name='marca_delete'),
    url(r'^Producte/(?P<pk>\d+)/$',ProducteDetail.as_view(), name = 'producte_detail'),
    url(r'^Producte/(?P<pk>\d+)/edit/$','iSupermarket.views.ProducteUpdate2', name='producte_update'),
    url(r'^Producte/(?P<pk>\d+)/delete/$',ProducteDelete.as_view(), name='producte_delete'),
    url(r'^Client/create/$',ClientCreate.as_view(),name='client_create'),
    url(r'^Producte/create/$','iSupermarket.views.ProducteCreate2',name='producte_create'),
    url(r'^Marca/create/$',MarcaCreate.as_view(),name='marca_create'),
    url(r'^Sucursal/create/$','iSupermarket.views.SucursalCreate2',name='sucursal_create'),
    url(r'^Companyia/create/$',CompanyiaCreate.as_view(),name='companyia_create'),
    url(r'^Client\.(?P<extension>(json|xml))$', Clients.as_view(), name='client_list_conneg'),
    url(r'^Marca\.(?P<extension>(json|xml))$', Marcas.as_view(), name='marca_list_conneg'),
    url(r'^Producte\.(?P<extension>(json|xml))$', Productes.as_view(), name='producte_list_conneg'),
    url(r'^Sucursal\.(?P<extension>(json|xml))$', Sucursals.as_view(), name='sucursal_list_conneg'),
    url(r'^Companyia\.(?P<extension>(json|xml))$', Companyias.as_view(), name='companyia_list_conneg'),
    url(r'^Client/(?P<pk>\d+)\.(?P<extension>(json|xml))$', ClientDetail.as_view(), name='client_detail_conneg'),
    url(r'^Marca/(?P<pk>\d+)\.(?P<extension>(json|xml))$', MarcaDetail.as_view(), name='marca_detail_conneg'),
    url(r'^Producte/(?P<pk>\d+)\.(?P<extension>(json|xml))$', ProducteDetail.as_view(), name='producte_detail_conneg'),
    url(r'^Sucursal/(?P<pk>\d+)\.(?P<extension>(json|xml))$', SucursalDetail.as_view(), name='sucursal_detail_conneg'),
    url(r'^Companyia/(?P<pk>\d+)\.(?P<extension>(json|xml))$', CompanyiaDetail.as_view(), name='companyia_detail_conneg'),
    url(r'^Register/$',UserCreate.as_view(),name='user_create'),
    url(r'^Sucursal/(?P<pk>\d+)/reviews/create/$', 'iSupermarket.views.review', name='review_create'),
)

#RESTful API
urlpatterns += patterns('',
    url(r'^api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/Clients/$', APIClientList.as_view(), name='client-list'),
    url(r'^api/Clients/(?P<pk>\d+)/$', APIClientDetail.as_view(), name='client-detail'),
    url(r'^api/Sucursals/$', APISucursalList.as_view(), name='sucursal-list'),
    url(r'^api/Sucursals/(?P<pk>\d+)/$', APISucursalDetail.as_view(), name='sucursal-detail'),
    url(r'^api/Marca/$', APIMarcaList.as_view(), name='marca-list'),
    url(r'^api/Marca/(?P<pk>\d+)/$', APIMarcaDetail.as_view(), name='marca-detail'),
    url(r'^api/Producte/$', APIProducteList.as_view(), name='producte-list'),
    url(r'^api/Producte/(?P<pk>\d+)/$', APIProducteDetail.as_view(), name='producte-detail'),
    url(r'^api/Companyia/$', APICompanyiaList.as_view(), name='companyia-list'),
    url(r'^api/Companyia/(?P<pk>\d+)/$', APICompanyiaDetail.as_view(), name='companyia-detail'),
    url(r'^api/sucursalreviews/$', APISucursalReviewList.as_view(), name='sucursalreview-list'),
    url(r'^api/sucursalreviews/(?P<pk>\d+)/$', APISucursalReviewDetail.as_view(), name='sucursalreview-detail'),
    
)

# Format suffixes
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['api','json', 'xml'])
