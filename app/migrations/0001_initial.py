# Generated by Django 3.0.8 on 2020-07-31 09:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(default=None, max_length=20)),
                ('serial', models.CharField(default=None, max_length=20)),
                ('pwd', models.CharField(default=None, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('price', models.DecimalField(decimal_places=0, max_digits=3)),
                ('comment', models.CharField(blank=True, max_length=50)),
                ('is_spicy', models.BooleanField()),
                ('name1', models.CharField(max_length=20)),
                ('name3', models.CharField(max_length=20)),
                ('update_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='更新时间')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, help_text='一个部门的名字应该唯一', max_length=20, unique=True, verbose_name='部门名')),
                ('phone_number', models.CharField(max_length=15)),
                ('address', models.CharField(blank=True, max_length=50)),
            ],
        ),
    ]
