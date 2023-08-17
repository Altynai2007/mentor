from django.db import models

class Ads(models.Model):
    title = models.CharField(max_length = 150)
    decription = models.TextField()
    price = models.FloatField()

    def __str__(self) ->str:
        return self.title

    class Meta:
        verbose_name = 'Ads'
        verbose_name_plural = 'Ads'
