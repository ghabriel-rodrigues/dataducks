from django.db import models

class Lead(models.Model):
    email = models.EmailField(unique = True)   
    kindoffood = models.CharField(max_length=300, verbose_name="What kind of food the ducks are fed?")
    food = models.CharField(max_length=300, verbose_name="What food the ducks are fed?")
    how_much_food = models.PositiveIntegerField(verbose_name="How much food the ducks are fed?") #value in grams
    how_many_ducks = models.PositiveIntegerField(verbose_name="How many ducks are fed?")
    fed_time = models.DateTimeField(verbose_name="What time the ducks are fed?")
    
    #TODO: If 'fed_everyday' is true, everyday a new lead (copy) needs to be created 
    fed_everyday = models.BooleanField(blank=True, verbose_name="Do you feed the ducks everyday?")
    #where the ducks are fed?
    #address = Address
    #geolocation = Coordinates 
    created_at = models.DateTimeField(verbose_name="Data created in", auto_now_add=True)
    