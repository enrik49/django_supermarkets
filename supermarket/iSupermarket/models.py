# Create your models here.
from django.db import models
from django.contrib.auth.models import User
#from django.core.urlresolvers import reverse
#from datetime import date

class Companyia(models.Model):
	name = models.TextField()

class Sucursal(models.Model):
	name = models.TextField()

class Client(models.Model):
	name = models.TextField()

class Marca(models.Model):
	name = models.TextField()

class Producte(models.Model):
	name = models.TextField()
