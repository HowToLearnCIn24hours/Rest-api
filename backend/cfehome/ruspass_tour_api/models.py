from django.db import models

class Cities(models.Model):
    tour_city = models.CharField(max_length=200)

class Tours(models.Model):
    tour_city = models.ForeignKey(Cities, on_delete=models.CASCADE)
    tour_name = models.CharField(max_length=1000)
    tour_type = models.CharField(max_length=200)
    tour_length = models.IntegerField(default=0)
    tour_eating = models.CharField(max_length=200)
    tour_price = models.IntegerField(default=0)
