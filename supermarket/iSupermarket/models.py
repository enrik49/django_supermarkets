# Create your models here.
from django.db import models
from django.contrib.auth.models import User
#from django.core.urlresolvers import reverse
from datetime import date

class Companyia(models.Model):
	name = models.TextField(null=True)
	idNumber = models.TextField(null=True)


	def __unicode__(self):
		return self.name


class Sucursal(models.Model):
	name = models.TextField(null=True)
	location = models.TextField(default="")
	zipCode = models.TextField(blank=True, null=True)
	StateOrProvince = models.TextField(blank=True, null=True)
	country = models.TextField(blank=True, null=True)
	Companyia = models.ForeignKey(Companyia, null=True, related_name='sucursal')

	def __unicode__(self):
		return self.name


class Client(models.Model):
	name = models.CharField(max_length=20)
	lastName = models.CharField(null=True,max_length=20)
	phone = models.CharField(null=True,max_length=9)
	registration_date = models.DateTimeField('date registred', null=True)

	def was_registred_recently(self):
		return self.registration_date >= timezone.now() - datetime.timedelta(days=1)

	def __unicode__(self):
		return self.name + ' ' + self.lastName

class Marca(models.Model):
	name = models.TextField(null=True)
	def __unicode__(self):
		return self.name

class Producte(models.Model):
	name = models.TextField(null=True)
	Marca = models.ForeignKey(Marca, null=True, related_name='producte')
	def __unicode__(self):
		return self.name + ' \''+ self.Marca.name +'\''
