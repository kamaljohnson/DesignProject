from django.db import models
from discussions.models import Discussion, Feed

# Create your models here.


class Tag(models.Model):
    tag = models.CharField(max_length=20, null=True)


class Idea(models.Model):
    DOC = models.DateField(auto_now=True)  # Date of Creation


class Project(models.Model):
    DOC = models.DateField(auto_now=True)  # Date of Creation


class Activity(models.Model):
    name = models.CharField(max_length=100)
    project_id = models.OneToOneField(Project, on_delete=models.SET_NULL, null=True)
    idea_id = models.OneToOneField(Idea, on_delete=models.SET_NULL, null=True)
    discussion_id = models.OneToOneField(Discussion, on_delete=models.SET_NULL, null=True)
    tags = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)

    up_votes = models.IntegerField(default=0)
    down_votes = models.IntegerField(default=0)

    def __str__(self):
        return self.name

