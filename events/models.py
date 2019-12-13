from django.db import models
from datetime import date

class event(models.Model):
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    event_title = models.CharField(max_length=2000)
    event_date = models.DateField(default=date.today)
    event_stime = models.TimeField()
    event_etime = models.TimeField()
    event_address = models.CharField(max_length=2000)
    event_content = models.TextField(blank=True)
    event_cn = models.BooleanField()
    event_s = models.BooleanField()
    def __str__(self):
        return self.event_title
