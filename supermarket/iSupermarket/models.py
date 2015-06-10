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
	user = models.ForeignKey(User, default=1)


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
	user = models.ForeignKey(User, default=1)

	def __unicode__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('iSupermarket:sucursal_detail', kwargs={'pk':self.pk})



class Client(models.Model):
	name = models.CharField(max_length=20)
	lastName = models.CharField(null=True,max_length=20)
	phone = models.CharField(null=True,max_length=9)
	registration_date = models.DateTimeField(default=timezone.now())
	user = models.ForeignKey(User, default=1)
	country = models.CharField(null=True,max_length=25)
	city = models.CharField(null=True,max_length=25)

	def was_registred_recently(self):
		return self.registration_date >= timezone.now() - datetime.timedelta(days=1)

	was_registred_recently.admin_order_field = 'pub_date'
	was_registred_recently.boolean = True
	was_registred_recently.short_description = 'Published recently?'
	def __unicode__(self):
		return unicode(self.name) + u' ' + unicode(self.lastName)

	def get_absolute_url(self):
		return reverse('iSupermarket:client_detail', kwargs={'pk':self.pk})

class Marca(models.Model):
	name = models.TextField(null=True)
	user = models.ForeignKey(User, default=1)

	def __unicode__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('iSupermarket:marca_detail', kwargs={'pk':self.pk})

class Producte(models.Model):
	name = models.TextField(null=True)
	marca = models.ForeignKey(Marca, null=True, related_name='producte')
	user = models.ForeignKey(User, default=1)

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

class Review(models.Model):
    RATING_CHOICES = ((1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5'))
    rating = models.PositiveSmallIntegerField('ratings (stars)', blank=False, default=3, choices=RATING_CHOICES)
    comment = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, default=1)
    date_re = timezone.now()

    class Meta:
        abstract = True

class SucursalReview(Review):
    sucursal = models.ForeignKey(Sucursal)

