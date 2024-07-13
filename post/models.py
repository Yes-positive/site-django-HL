from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=15)
    content = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    media = models.FileField(upload_to="media_post/", blank=True, null=True)