from django.db import models


class MeasurementData(models.Model):
    """
    This Model is the database class that stores measured time series data.
    """
    data = models.FileField(upload_to='uploads/')
