from django.db import models
from activity.models import Activity
# Create your models here.


class Discussion(models.Model):
    activity_id = models.ForeignKey(Activity, on_delete=models.CASCADE)

class Feed(models.Model):
    feed = models.TextField()
    discussion_id = models.ForeignKey(Discussion, on_delete=models.CASCADE)
