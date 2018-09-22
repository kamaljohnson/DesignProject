from django.db import models

# Create your models here.


class Discussion(models.Model):
    pass

class Feed(models.Model):
    feed = models.TextField()
    discussion_id = models.ForeignKey(Discussion, on_delete=models.CASCADE)
