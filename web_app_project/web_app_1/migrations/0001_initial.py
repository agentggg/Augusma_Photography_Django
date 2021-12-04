# Generated by Django 3.2.8 on 2021-11-25 06:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='history',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('career_name', models.CharField(max_length=100, verbose_name='Career name')),
                ('industry', models.CharField(max_length=20, verbose_name='Industry')),
                ('years', models.CharField(max_length=120, verbose_name='Years in industry')),
                ('salary', models.IntegerField(default=1)),
                ('last_name', models.DateTimeField(verbose_name=datetime.datetime(2021, 11, 25, 1, 34, 3, 582151))),
            ],
        ),
        migrations.CreateModel(
            name='identity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, verbose_name='Last name')),
                ('gender', models.CharField(max_length=10, verbose_name='Gender, Male or Female')),
                ('age', models.IntegerField(default=18)),
                ('last_name', models.DateTimeField(verbose_name=datetime.datetime(2021, 11, 25, 1, 34, 3, 582151))),
            ],
        ),
    ]