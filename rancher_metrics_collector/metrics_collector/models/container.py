from django.db import models
from metrics_collector.models.host import RancherHost

class RancherContainer(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    host = models.ForeignKey(RancherHost)
    name = models.CharField(max_length=255)

class ContainerMetrics(models.Model):
    container = models.ForeignKey(RancherContainer)
    name = models.CharField(max_length=255)

