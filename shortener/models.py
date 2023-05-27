from django.db import models
from datetime import datetime, timedelta
from .utility import hash_url

def get_expiration_date():
    return datetime.now() + timedelta(365)

# Create your models here.
class Url(models.Model):
    # short_url = models.CharField(max_length=30, db_index=True)
    original_url = models.CharField(max_length=1000)
    hash = models.CharField(max_length=10, db_index=True, blank=True)
    views = models.PositiveIntegerField(default=0)
    expiration_date = models.DateTimeField(default=get_expiration_date)
    
    def save(self, *args, **kwargs):
        if self.original_url:
            self.hash = hash_url(self.original_url)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.original_url
    
    @property
    def short_url(self, domain):
       return f"http://{domain}/api/go/{self.hash}"
