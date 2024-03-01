from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length = 2045)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    