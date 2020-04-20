# Default imports
import time
import uuid

# Scheduler dependencies
from django.core.management.base import BaseCommand, CommandError
from leads.models import Lead
 
# Class that will create the Lead entity as a copy if the original is marking 'fed everyday' as True
class Command(BaseCommand):
    help = 'Add a new (copy of) Lead if the opt fed_everyday is True, every day'

    def add_arguments(self, parser):
      parser.add_argument('lead_ids', nargs='+', type=int)

    def handle(self, *args, **options):
      for lead_id in options['lead_ids']:
        try:
          lead = Lead.objects.get(pk=lead_id)
        except Lead.DoesNotExist:
          raise CommandError('Lead "%s" does not exist' % lead_id)

        if lead.fed_everyday:
          lead_copy = Lead(            
            email="id_%s_of_%s_%s" % (lead.id, uuid.uuid4(), lead.email) ,
            food= lead.food, 
            kindoffood=  lead.kindoffood,
            how_much_food=  lead.how_much_food,
            measure= lead.measure,
            how_many_ducks= lead.how_many_ducks,
            fed_time= lead.fed_time,
            fed_everyday= lead.fed_everyday,
            address= lead.address,
            geolocation= lead.geolocation,
            created_at= time.strftime("%d-%m-%Y-%H-%M-%S")
          )
          lead_copy.save()
          self.stdout.write(self.style.SUCCESS('Successfully copied Lead "%s"' % lead_id))