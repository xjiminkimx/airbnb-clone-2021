# Generated by Django 2.2.5 on 2021-01-09 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0002_roomtype'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='room_type',
            field=models.ManyToManyField(blank=True, to='rooms.RoomType'),
        ),
    ]
