# Generated by Django 2.2.12 on 2020-04-18 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='fed_time',
            field=models.TimeField(verbose_name='What time the ducks are fed?'),
        ),
    ]
