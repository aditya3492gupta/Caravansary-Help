# Generated by Django 4.1.5 on 2023-06-04 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0009_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Laundry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('admn', models.CharField(max_length=15)),
                ('inputp', models.CharField(max_length=2)),
                ('inputj', models.CharField(max_length=2)),
                ('inputs', models.CharField(max_length=2)),
                ('inputt', models.CharField(max_length=2)),
                ('inputk', models.CharField(max_length=2)),
                ('inputpy', models.CharField(max_length=2)),
                ('inputtp', models.CharField(max_length=2)),
                ('inputsho', models.CharField(max_length=2)),
                ('inputun', models.CharField(max_length=2)),
                ('inputb', models.CharField(max_length=2)),
                ('inputsp', models.CharField(max_length=2)),
                ('inputbs', models.CharField(max_length=2)),
                ('inputpc', models.CharField(max_length=2)),
                ('inputht', models.CharField(max_length=2)),
                ('inputhc', models.CharField(max_length=2)),
                ('inputbt', models.CharField(max_length=2)),
                ('inputo', models.CharField(max_length=2)),
                ('ttl', models.CharField(max_length=2)),
            ],
        ),
    ]
