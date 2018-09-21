from django.db import models
import datetime
from django.utils import timezone
# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=60)
    pub_date=models.DateTimeField(default=timezone.now)
    body=models.TextField()
    image=models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]
    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
