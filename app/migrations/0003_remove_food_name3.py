# Generated by Django 3.0.8 on 2020-07-31 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_restaurant_addressc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='name3',
        ),
    ]