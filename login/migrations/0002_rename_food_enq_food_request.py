# Generated by Django 4.1.5 on 2023-01-21 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='food_enq',
            new_name='food_request',
        ),
    ]