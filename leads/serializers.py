from rest_framework import serializers
from .models import Lead, Food, KindOfFood

#Serializers are mandatory to enable operating on models through the REST API
class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = (
          'id', 'email', 'food', 
          'how_much_food','how_many_ducks','fed_time',
          'fed_everyday','created_at'
        )

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = (
          'id', 'name', 'kindoffood', 'created_at'
        )

class KindOfFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = KindOfFood
        fields = (
         'id', 'name', 'created_at'
        )
        