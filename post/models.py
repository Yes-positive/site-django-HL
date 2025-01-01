from django.db import models
from django.conf import settings

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=15, default="")
    content = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    media = models.FileField(upload_to="post_media/", blank=True, null=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="post", default="")

    def get_absolute_url(self):
        return self.task.get_absolute_url()