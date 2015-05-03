# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
import datetime
from django.utils import timezone
#from datetime import date


class Companyia(models.Model):
	name = models.TextField(null=True)
	idNumber = models.TextField(null=True)


	def __unicode__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('iSupermarket:companyia_detail', kwargs={'pk':self.pk})


class Sucursal(models.Model):
	name = models.TextField(null=True)
	location = models.TextField(default="")
	zipCode = models.TextField(blank=True, null=True)
	StateOrProvince = models.TextField(blank=True, null=True)
	country = models.TextField(blank=True, null=True)
	companyia = models.ForeignKey(Companyia, null=True, related_name='sucursal')

	def __unicode__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('iSupermarket:sucursal_detail', kwargs={'pk':self.pk})



class Client(models.Model):
	name = models.CharField(max_length=20)
	lastName = models.CharField(null=True,max_length=20)
	phone = models.CharField(null=True,max_length=9)
	registration_date = models.DateTimeField(default=timezone.now())

	def was_registred_recently(self):
		return self.registration_date >= timezone.now() - datetime.timedelta(days=1)

	def __unicode__(self):
		return self.name + ' ' + self.lastName

	def get_absolute_url(self):
		return reverse('iSupermarket:client_detail', kwargs={'pk':self.pk})

class Marca(models.Model):
	name = models.TextField(null=True)

	def __unicode__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('iSupermarket:marca_detail', kwargs={'pk':self.pk})

class Producte(models.Model):
	name = models.TextField(null=True)
	marca = models.ForeignKey(Marca, null=True, related_name='producte')

	def __unicode__(self):
		return self.name + ' \''+ self.marca.name +'\''

	def get_absolute_url(self):
		return reverse('iSupermarket:producte_detail', kwargs={'pk':self.pk})

class ClientSucursal(models.Model):
	sucursal = models.ManyToManyField(Sucursal)
	client = models.ManyToManyField(Client)

class MarcaSucursal(models.Model):
	sucursal = models.ManyToManyField(Sucursal)
	marca = models.ManyToManyField(Marca)

class MarcaClient(models.Model):
	marca = models.ManyToManyField(Marca)
	client = models.ManyToManyField(Client)

