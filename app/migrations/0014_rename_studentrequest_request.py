# Generated by Django 3.2.12 on 2022-05-04 13:41

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0013_auto_20220504_1250'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='StudentRequest',
            new_name='Request',
        ),
    ]