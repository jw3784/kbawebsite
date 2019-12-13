
from django.db import models

class alumnus(models.Model):
    name = models.CharField(max_length=500)
    a_class = models.IntegerField()
    a_company = models.CharField(max_length=500)
    a_title = models.CharField(max_length=500)
    a_field = models.CharField(max_length=500)
    a_email = models.EmailField(max_length=254)
    a_city = models.CharField(max_length=500)
    a_country = models.CharField(max_length=500)
    def __str__(self):
        return self.name