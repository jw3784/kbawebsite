from django.db import models

class boardmember(models.Model):
    name = models.CharField(max_length=500)
    title = models.CharField(max_length=1000)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    def __str__(self):
        return self.name

