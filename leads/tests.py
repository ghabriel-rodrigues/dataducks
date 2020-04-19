# Default imports
import datetime 
import pytz

# Test dependencies
from django.test import TestCase

# Model dependencies
from .models import Lead
from .forms import LeadTestForm

# Class to test data, run "python manage.py test leads" in cmd line to see it running 
class ProjectTests(TestCase):  

    # Page/Form tests
    def test_home_exists(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_leadredirect_exists(self):
        response = self.client.get('/lead/')
        self.assertEqual(response.status_code, 200)

    def test_leadform_content(self):
        response = self.client.get('/')
        labels = ['Email', 'Kind', 
          'Food','How much food?', 'Measure', 'Number of ducks',
          'Time', 'Do you feed the ducks everyday?','What is the address where the ducks are fed?']

        for i in labels:
          self.assertContains(response, i)

#    # Model tests
#     def test_fields(self):
#         lead = Lead(
#           email="email", 
#           food="food", 
#           kindoffood="kindoffood",
#           how_much_food="how_much_food",
#           measure="measure",
#           how_many_ducks="how_many_ducks",
#           fed_time="fed_time",
#           fed_everyday="fed_everyday",
#           address="address",
#           geolocation="geolocation",
#           created_at="created_at",
#         )

#         self.assertEqual(lead.email, "email")
#         self.assertEqual(lead.food, "food")
#         self.assertEqual(lead.kindoffood, "kindoffood")
#         self.assertEqual(lead.how_much_food, "how_much_food")
#         self.assertEqual(lead.measure, "measure")
#         self.assertEqual(lead.how_many_ducks, "how_many_ducks")
#         self.assertEqual(lead.fed_time, "fed_time")
#         self.assertEqual(lead.fed_everyday, "fed_everyday")
#         self.assertEqual(lead.address, "address")
#         self.assertEqual(lead.geolocation, "geolocation")
#         self.assertEqual(lead.created_at, "created_at")

    def test_validform_data(self):      
      form = LeadTestForm(
        {
        "email": "email@email.com",
        "food": "Corn", 
        "kindoffood": "Seeds",
        "how_much_food": 2,
        "measure": "KG",
        "how_many_ducks": 200,
        "fed_time": "2020-04-19 12:00:00",
        "fed_everyday": True,
        "address": "Fortaleza, Ceará, Brasil",
        "geolocation": "12, 12",
        "created_at": "2020-04-19 12:00:00"
        }
      )
      self.assertTrue(form.is_valid())

      lead = form.save()

      self.assertEqual(lead.email, "email@email.com")
      self.assertEqual(lead.food, "Corn")
      self.assertEqual(lead.kindoffood, "Seeds")
      self.assertEqual(lead.how_much_food, 2)
      self.assertEqual(lead.measure, "KG")
      self.assertEqual(lead.how_many_ducks, 200)
      self.assertEqual(lead.fed_everyday, True)
      self.assertEqual(lead.address, "Fortaleza, Ceará, Brasil")
        
    def test_string_representation(self):
        lead = Lead(food="Food", kindoffood="Kind")
        self.assertEqual(str(lead), "Food: %s - Kind of food: %s" % (lead.food, lead.kindoffood))

    
