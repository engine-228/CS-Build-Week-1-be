# Generated by Django 3.0.4 on 2020-03-06 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('undefined_world_rooms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='map',
            field=models.TextField(default='ROOM MAP', max_length=1500),
        ),
    ]
