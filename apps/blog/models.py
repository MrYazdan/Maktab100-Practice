from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=256)
    parent = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.CharField(max_length=120)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    reply = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="replies")

    def __str__(self):
        return f"{self.id} > {self.content[:10]}"

