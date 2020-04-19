from django.db import models
from django_google_maps import fields as map_fields

class Lead(models.Model):
    choices_measure = (
        ('KG', 'KG'),
        ('Gram', 'Gram'),
        ('Unit', 'Unit'),
    )

    def __str__(self):
        return "Food: %s - Kind of food: %s" % (self.food, self.kindoffood)


    email = models.EmailField(unique = True)   
    kindoffood = models.CharField("Kind",max_length=300, help_text="What kind of food the ducks are fed?")
    food = models.CharField("Food",max_length=300, help_text="What food the ducks are fed?")
    how_much_food = models.PositiveIntegerField("How much food?",help_text="KG, grams or units") #value in grams
    measure = models.CharField("Measure", max_length=4, help_text="What is the usual measure of the food the ducks are fed?", choices=choices_measure, default="KG")
    
    how_many_ducks = models.PositiveIntegerField("Number of ducks", help_text="How many ducks are fed?")
    fed_time = models.DateTimeField("Time", help_text="What time the ducks are fed?")
    
    #TODO: If 'fed_everyday' is true, everyday a new lead (copy) needs to be created 
    #heroku scheduler
    fed_everyday = models.BooleanField("Feed everyday?",blank=True, help_text="Do you feed the ducks everyday?")
    address = map_fields.AddressField(help_text="What is the address where the ducks are fed?", blank=True, max_length=200)
    geolocation = map_fields.GeoLocationField(help_text="What are the coordinates where the ducks are fed?", blank=True, max_length=100)
    created_at = models.DateTimeField(verbose_name="Data created in", auto_now_add=True)
    