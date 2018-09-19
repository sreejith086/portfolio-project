from django.db import models
import datetime
from django.utils import timezone
# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=60)
    pub_date=models.DateTimeField(default=timezone.now)
    body=models.TextField()
    image=models.ImageField(upload_to='images/')
