from django.db import models
from user_accounts.models import User


# Create your models here.


class Tag(models.Model):
    tag = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.tag


class Activity(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)

    up_votes = models.IntegerField(default=0)
    down_votes = models.IntegerField(default=0)

    def __str__(self):
        return self.name + " by " + self.owner.name


class Info(models.Model):
    info = models.TextField()


class Idea(models.Model):
    DOC = models.DateField(auto_now=True)  # Date of Creation
    activity_id = models.ForeignKey(Activity, on_delete=models.CASCADE, null=True)  # The activity associated with the idea
    info_id = models.ForeignKey(Info, on_delete=models.SET_NULL, null=True)


class Project(models.Model):
    DOC = models.DateField(auto_now=True)  # Date of Creation
    idea_id = models.ForeignKey(Idea, on_delete=models.SET_NULL, null=True)  # If derived from an idea
    activity_id = models.ForeignKey(Activity, on_delete=models.CASCADE)  # The activity associated with the project
    info_id = models.ForeignKey(Info, on_delete=models.SET_NULL, null=True)