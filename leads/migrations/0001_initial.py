# Generated by Django 2.2.12 on 2020-04-17 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='KindOfFood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('how_much_food', models.PositiveIntegerField(verbose_name='How much food the ducks are fed?')),
                ('how_many_ducks', models.PositiveIntegerField(verbose_name='How many ducks are fed?')),
                ('fed_time', models.DateTimeField(verbose_name='What time the ducks are fed?')),
                ('fed_everyday', models.BooleanField(blank=True, verbose_name='Do you feed the ducks everyday?')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Data created in')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='leads.Food', verbose_name='What food the ducks are fed?')),
            ],
        ),
        migrations.AddField(
            model_name='food',
            name='kindoffood',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='leads.KindOfFood', verbose_name='What kind of food the ducks are fed?'),
        ),
    ]