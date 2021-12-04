from django.db import models
from datetime import datetime
now = datetime.now()

# Create your models here.
class identity(models.Model):
    #Creates a model named Owner, via class
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    age = models.IntegerField(default=18)

# Create your models here.
class history(models.Model):
    #Creates a model named Owner, via class
    career_name = models.CharField('Career name', max_length=100)
    industry = models.CharField('Industry', max_length=20)
    years = models.CharField('Years in industry', max_length=120)
    salary = models.IntegerField(default=1)
    last_name = models.DateTimeField(now)

# Create your models here.
class user_login(models.Model):
    #Creates a model named Owner, via class
    login_username = models.CharField(max_length=20)
    login_password = models.CharField(max_length=20)
