from django.db import models

class RancherHost(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=255)