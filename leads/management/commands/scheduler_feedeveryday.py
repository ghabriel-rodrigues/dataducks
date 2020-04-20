# Default imports
import time
import uuid

# Scheduler dependencies
from django.core.management.base import BaseCommand, CommandError
from leads.models import Lead
 
# Class that will create the Lead entity as a copy if the original is marking 'fed everyday' as True
class Command(BaseCommand):
    help = 'Add a new (copy of) Lead if the opt fed_everyday is True, every day'

    def handle(self, *args, **options):
      
      try:
        leadList = Lead.objects.all()
      except leadList.DoesNotExist:
        raise CommandError('leadList does not exist')

      for lead in leadList:
        if lead.fed_everyday:
          lead_copy = Lead( 
            #not so good solution needed to copy and register a unique field           
            email="id_%s_of_%s_%s" % (lead.id, uuid.uuid4(), lead.email) ,
            food= lead.food, 
            kindoffood=  lead.kindoffood,
            how_much_food=  lead.how_much_food,
            measure= lead.measure,
            how_many_ducks= lead.how_many_ducks,
            fed_time= lead.fed_time,
             #avoids false data progression
            fed_everyday= False,
            address= lead.address,
            geolocation= lead.geolocation,
            created_at= time.strftime("%d-%m-%Y-%H-%M-%S")
          )
          lead_copy.save()
          self.stdout.write(self.style.SUCCESS('Successfully copied Lead "%s"' % lead.id))