from django.db import models

class TrackingModel(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        abstract = True             #We shoulde not be using this model to create new instances
        ordering=('-created_at', )  # - for descending order, remove dash if you want ascending order