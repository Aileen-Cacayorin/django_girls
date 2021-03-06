from django.db import models
from django.utils import timezone




# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(default=timezone.now)
    likes = models.IntegerField(default=0)

    def publish(self):
        self.publish_date=timezone.now
        self.save()

    def __str__(self):
        return self.title
