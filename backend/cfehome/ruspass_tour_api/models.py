from django.db import models


class Cities(models.Model):
    tour_city = models.CharField(max_length=200)


class Hotels(models.Model):
    hotel_star = models.TextChoices("HotelStars", "1 2 3 4 5")


class TourLength(models.Model):
    length = models.IntegerField(default=0)


class TourTypes(models.Model):
    tour_type = models.TextChoices("TourType", "фото винный активный спокойный романтический семейный")


class FeedRegimen(models.Model):
    tour_eating = models.TextChoices("TourEating", "завтрак, завтрак_и_ужин, все включено")


class Tours(models.Model):
    tour_city = models.ForeignKey(Cities, on_delete=models.CASCADE)
    tour_name = models.CharField(max_length=1000)
    tour_date_start = models.DateField()
    tour_date_end = models.DateField()
    tour_type = models.ForeignKey(TourTypes, on_delete=models.CASCADE)
    tour_length = models.ForeignKey(TourLength, on_delete=models.CASCADE)
    tour_eating = models.ForeignKey(FeedRegimen, on_delete=models.CASCADE)
    tour_price = models.IntegerField(default=0)
    tour_hotel_category = models.ForeignKey(Hotels, on_delete=models.CASCADE)
    tour_rating = models.IntegerField(default=0)
