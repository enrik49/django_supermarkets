from rest_framework.fields import CharField
from rest_framework.relations import HyperlinkedRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer
from models import *




class ClientSerializer(HyperlinkedModelSerializer):
	url = HyperlinkedIdentityField(view_name='iSupermarket:client-detail')

	class Meta:
		model = Client
		fields = ('url', 'name','lastName','phone','registration_date')
