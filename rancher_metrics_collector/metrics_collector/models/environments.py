from django.db import models


class RancherEnvironments(models.Model):
    id = models.CharField(max_length=20, primary_key=True)