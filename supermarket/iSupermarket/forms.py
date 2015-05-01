from django.forms import ModelForm
from models import client

class ClientForm(ModelForm):
    class Meta:
        model = Restaurant
