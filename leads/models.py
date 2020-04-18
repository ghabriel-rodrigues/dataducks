from django.db import models
from django_google_maps import fields as map_fields

class Lead(models.Model):
    choices_measure = (
        ('KG', 'KG'),
        ('Gram', 'Gram'),
        ('Unit', 'Unit'),
    )

    email = models.EmailField(unique = True)   
    kindoffood = models.CharField(max_length=300, verbose_name="What kind of food the ducks are fed?")
    food = models.CharField(max_length=300, verbose_name="What food the ducks are fed?")
    how_much_food = models.PositiveIntegerField(verbose_name="How much food the ducks are fed?") #value in grams
    measure = models.CharField(max_length=4, verbose_name="What is the usual measure of the food the ducks are fed?", choices=choices_measure, default="KG")
    
    how_many_ducks = models.PositiveIntegerField(verbose_name="How many ducks are fed?")
    fed_time = models.DateTimeField(verbose_name="What time the ducks are fed?")
    
    #TODO: If 'fed_everyday' is true, everyday a new lead (copy) needs to be created 
    #heroku scheduler
    fed_everyday = models.BooleanField(blank=True, verbose_name="Do you feed the ducks everyday?")
    address = map_fields.AddressField(verbose_name="What is the address where the ducks are fed?", blank=True, max_length=200)
    geolocation = map_fields.GeoLocationField(verbose_name="What are the coordinates where the ducks are fed?", blank=True, max_length=100)
    created_at = models.DateTimeField(verbose_name="Data created in", auto_now_add=True)
    