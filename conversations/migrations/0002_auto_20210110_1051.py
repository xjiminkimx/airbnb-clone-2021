# Generated by Django 2.2.5 on 2021-01-10 01:51

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('conversations', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Conversations',
            new_name='Conversation',
        ),
    ]
