# Generated by Django 3.0.8 on 2020-08-03 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20200803_1433'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sinter_process',
            old_name='a',
            new_name='A',
        ),
        migrations.RenameField(
            model_name='sinter_process',
            old_name='b',
            new_name='B',
        ),
        migrations.RenameField(
            model_name='sinter_process',
            old_name='cheak_emplotee_id',
            new_name='check_employee_id',
        ),
    ]