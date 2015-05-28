from rest_framework.fields import CharField
from rest_framework.relations import HyperlinkedRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer
from models import *




class ClientSerializer(HyperlinkedModelSerializer):
	url = HyperlinkedIdentityField(view_name='iSupermarket:client-detail')
	user = CharField(read_only=True)
	class Meta:
		model = Client
		fields = ('url', 'name','lastName','phone','registration_date','user')

class ProducteSerializer(HyperlinkedModelSerializer):
	url = HyperlinkedIdentityField(view_name='iSupermarket:producte-detail')
	marca = HyperlinkedRelatedField(queryset=Marca.objects.all(), view_name='iSupermarket:marca-detail')
	user = CharField(read_only=True)
	class Meta:
		model = Producte
		fields = ('url', 'name', 'marca','user')

class SucursalSerializer(HyperlinkedModelSerializer):
	url = HyperlinkedIdentityField(view_name='iSupermarket:sucursal-detail')
	companyia = HyperlinkedRelatedField(queryset=Companyia.objects.all(), view_name='iSupermarket:companyia-detail')
	user = CharField(read_only=True)
	class Meta:
		model = Sucursal
		fields = ('url', 'name','location','zipCode','StateOrProvince', 'country', 'companyia','user')

class MarcaSerializer(HyperlinkedModelSerializer):
	url = HyperlinkedIdentityField(view_name='iSupermarket:marca-detail')
	user = CharField(read_only=True)
	class Meta:
		model = Marca
		fields = ('url', 'name','user')

class CompanyiaSerializer(HyperlinkedModelSerializer):
	url = HyperlinkedIdentityField(view_name='iSupermarket:companyia-detail')
	user = CharField(read_only=True)
	class Meta:
		model = Companyia
		fields = ('url', 'name','user')
