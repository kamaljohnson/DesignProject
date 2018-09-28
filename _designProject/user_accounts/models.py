from django.db import models
from activity.models import *

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=25)


    def __str__(self):
        return self.name




