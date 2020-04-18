from rest_framework import serializers
from .models import Lead

#Serializers are mandatory to enable operating on models through the REST API
class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = (
          'id', 'email', 'kindoffood', 'food', 
          'how_much_food','measure', 'how_many_ducks', 'fed_time',
          'fed_everyday', 'address', 'geolocation', 'created_at'
        )
        