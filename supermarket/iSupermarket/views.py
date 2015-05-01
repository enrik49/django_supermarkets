# Create your views here.
from django.core.urlresolvers import reverse
from django.core import urlresolvers
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView

from models import Client, Companyia, Marca, Producte, Sucursal
#from forms import ClientForm

class Inici(ListView):
    model = Client #Aixo ha de quedar aixi ara que ja no llistem clients.
    template_name = 'index.html'
    queryset = Client.objects.all() #Comentari = al anterior.

class Client(ListView):
    model = Client
    template_name = 'clients.html'
    queryset = Client.objects.all()
    context_object_name='clients_list'

class ClientDetail(DetailView):
    model = Client
    template_name = 'client_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ClientDetail, self).get_context_data(**kwargs)
        return context

class Companyia(ListView):
    model = Companyia
    template_name = 'companyia.html'
    queryset = Companyia.objects.all()
    context_object_name='Companyia_list'

class Sucursal(ListView):
    model = Sucursal
    template_name = 'sucursal.html'
    queryset = Sucursal.objects.all()
    context_object_name='Sucursal_list'

class Marca(ListView):
    model = Marca
    template_name = 'marca.html'
    queryset = Marca.objects.all()
    context_object_name='Marca_list'

class Producte(ListView):
    model = Producte
    template_name = 'producte.html'
    queryset = Producte.objects.all()
    context_object_name='Producte_list'



'''class RestaurantCreate(CreateView):
    model = Restaurant
    template_name = 'myrestaurants/form.html'
    form_class = RestaurantForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(RestaurantCreate, self).form_valid(form)

class DishCreate(CreateView):
    model = Dish
    template_name = 'myrestaurants/form.html'
    form_class = DishForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.restaurant = Restaurant.objects.get(id=self.kwargs['pk'])
        return super(DishCreate, self).form_valid(form)

def review(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    new_review = RestaurantReview(
        rating=request.POST['rating'],
        comment=request.POST['comment'],
        user=request.user,
        restaurant=restaurant)
    new_review.save()
    return HttpResponseRedirect(urlresolvers.reverse('myrestaurants:restaurant_detail', args=(restaurant.id,)))'''
