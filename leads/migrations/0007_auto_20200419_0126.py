# Generated by Django 2.2.12 on 2020-04-19 01:26

from django.db import migrations, models
import django_google_maps.fields


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0006_lead_measure'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='address',
            field=django_google_maps.fields.AddressField(max_length=200, verbose_name='What is the address where the ducks are fed?'),
        ),
        migrations.AlterField(
            model_name='lead',
            name='how_much_food',
            field=models.PositiveIntegerField(help_text='KG, grams or units', verbose_name='How much food the ducks are fed?'),
        ),
    ]