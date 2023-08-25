from django import forms
from .models import Ads

class AdForm(forms.ModelForm):
    class Meta:
        model = Ads
        fields = "__all__"
    # title = forms.CharField(max_length = 150)
    # decription = forms.CharField(widjet = forms.Textarea)
    # price = forms.FloatField()
    # image = forms.ImageField()
    # type = forms.ChoiseField(max_length=100,choices= TYPE_OF_ADS)
    # subcategory = forms.IntegerField()
    # owner = forms.IntegerField()