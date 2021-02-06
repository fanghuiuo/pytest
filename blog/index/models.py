from django.db import models


class blog(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()


# Create your models here.
