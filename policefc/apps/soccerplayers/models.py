from django.db import models
from apps.posts.models import Author
from ckeditor_uploader.fields import RichTextUploadingField


class TeamPosition(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

class Leg(models.Model):
    leg = models.CharField(max_length=30)

    def __str__(self):
        return self.leg


class SoccerPlayer(models.Model):
    full_name = models.CharField(max_length=100)
    short_description = models.TextField()
    bio = RichTextUploadingField(blank=True, null=True)
    team_positions = models.ManyToManyField(TeamPosition)
    strongest_foot = models.ManyToManyField(Leg)
    ratings = models.IntegerField(default=0,null=True)
    dob = models.CharField(max_length=100)
    former_team = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    bio_picture = models.ImageField()
    featured_picture = models.ImageField()
    featured = models.BooleanField(default=True)

    def __str__(self):
        return self.full_name


class TechnicalTeam(models.Model):
    full_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    short_description = models.TextField()
    bio = RichTextUploadingField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    bio_picture = models.ImageField()
    featured_picture = models.ImageField()
    featured = models.BooleanField(default=True)

    def __str__(self):
        return self.full_name


class ExecutiveTeam(models.Model):
    full_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    short_description = models.TextField()
    bio = RichTextUploadingField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    bio_picture = models.ImageField()
    featured_picture = models.ImageField()
    featured = models.BooleanField(default=True)

    def __str__(self):
        return self.full_name
