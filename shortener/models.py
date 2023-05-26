from django.db import models
from datetime import datetime, timedelta

def get_expiration_date():
    return datetime.now() + timedelta(365)

# Create your models here.
class Url(models.Model):
    short_url = models.CharField(max_length=20, db_index=True)
    original_url = models.CharField(max_length=1000)
    hash = models.CharField(max_length=10, db_index=True, blank=True)
    views = models.PositiveIntegerField(default=0)
    expiration_date = models.DateTimeField(default=get_expiration_date)

    def __str__(self):
        return self.short_url