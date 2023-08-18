from django.db import models
from django.utils import timezone
from users.models import User

class Category(models.Model):
    title = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Subcategory(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)




class Ads(models.Model):
    LEARN = 'Хочу научиться'
    TEACH = 'Могу научить'
    TYPE_OF_ADS = [
        (LEARN,'Хочу научиться'),
        (TEACH,'Мoгу научить')
    ]

    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, null=True, blank=True, related_name='ads')
    title = models.CharField(max_length = 150)
    decription = models.TextField()
    price = models.FloatField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ads', null = True, blank = True)
    type = models.CharField(max_length=100,choices= TYPE_OF_ADS,default = LEARN)
    created_at = models.DateTimeField(default=timezone.now)
    upddated_at = models.DateTimeField(default=timezone.now)

    def __str__(self) ->str:
        return self.title

    class Meta:
        verbose_name = 'Ads'
        verbose_name_plural = 'Ads'
