# models.py
from django.db import models

class Experiment(models.Model):
    id = models.CharField(max_length=20, primary_key=True)  # Unique alphanumeric ID
    title = models.CharField(max_length=255)  # Experiment name (make sure this matches the view)
    file = models.FileField(upload_to='experiments/', null=True)  # Allow null values

    def __str__(self):
        return self.title  # Return the title for better representation
