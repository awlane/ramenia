from django.db import models
from django.conf import settings

class Review(models.Model):

    class Ratings(models.IntegerChoices):
        ONE_STAR = 1
        TWO_STAR = 2
        THREE_STAR = 3
        FOUR_STAR = 4
        FIVE_STAR = 5

    title = models.CharField(max_length=60)
    body = models.CharField(max_length=1000)
    rating = models.IntegerField(choices=Ratings.choices)
    reviewer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    noodle = models.ForeignKey("rameniaapp.Noodle", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)

class ReviewImage(models.Model):
    image = models.ImageField()
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    timestamp = models.DateField(auto_now_add=True)
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
