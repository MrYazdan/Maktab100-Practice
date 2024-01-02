from django.db import models


class About(models.Model):
    name_and_surname = models.CharField(max_length=256)
    phone_number = models.CharField(max_length=11, blank=True)
    email = models.EmailField(blank=True)
    subject_of_request = models.CharField(max_length=256, blank=True)
    upload_file = models.FileField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name_and_surname
