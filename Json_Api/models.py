from django.db import models
from datetime import datetime,date
import pytz

# Create your models here.

class UserData(models.Model):
    # id = models.AutoField(primary_key = True)
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))
    userid = models.CharField(max_length = 100, primary_key=True)
    name = models.CharField(max_length = 200)
    timezone = models.CharField(max_length = 100, choices = TIMEZONES, default='UTC')

    def __str__(self):
        return self.name

class ActivePeriod(models.Model):
    # start_time = models.DateTimeField(auto_now = False, auto_now_add=False)
    start_time = models.CharField(max_length=100)
    # end_time = models.DateTimeField(auto_now = False, auto_now_add=False)
    end_time = models.CharField(max_length=100)
    user = models.ForeignKey(UserData, on_delete = models.CASCADE)
