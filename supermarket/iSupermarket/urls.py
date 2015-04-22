from django.conf.urls import patterns, include, url
from models import *
#from filmApplication.forms import ActorForm, DirectorForm, MovieForm, ReviewForm
from views import *
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
	#Url de inici
    url(r'^$', Inici.as_view()),
)