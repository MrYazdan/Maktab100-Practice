from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)



