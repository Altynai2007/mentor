from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django. utils import timezone
import datetime
from users.models import User
from django.views import View
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from .models import Ads, Category
from .forms import AdForm

def category_list(request):
    all_categories = Category.objects.all()
    context = {
        'all_categories':all_categories
    }
    return render(request, 'category.html', context = context)

# def ads_list(request):
#     all_ads = Ads.objects.all()
def AdsView(View):
    template_name = 'index.html'

    def get(self,request,*args,**kwargs):
        all_ads = Ads.objects.all()
        return render(request,self.template_name,{'all_ads':all_ads} )


    # all_ads = Ads.objects.filter( created_at__lte=timezone.now())
    # all_ads = Ads.objects.filter( title__icontains = 'test')
    # all_ads = Ads.objects.filter( owner__is_null = True)(owner = None)
    # all_ads = Ads.objects.filter(decription__icontains='b',created_at__year = 2023)
    # admin = User.objects.get(username='admin')
    # all_ads = Ads.objects.filter( owner =admin)
    # all_ads = Ads.objects.filter( price__lt = 200,price__lt = 1500,price__lt = 342,price__lt = 700)(price__in[200,1500,300,342])


    

    print(all_ads)
    context = {
        'all_ads':all_ads
    }
    return render(request, 'index.html', context = context)

def create_ad(request):
    if request.method == "POST":
        form = AdForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ads-list')
    else:
        form_of_ad = AdForm()
    return render(request,'create_ad.html',{'form_of_ad':form_of_ad})

def update_ad(request, pk):
    ad = get_object_or_404(Ads, id =pk)
    if request.method == "POST":
        form = AdForm(request.POST, request.FILES, instance =ad )
        if form.is_valid():
            form.save()
            return HttpResponse('<h1> Success edited </h1>')
        else:  
            return HttpResponse('<h1> Error edited </h1>')
    else:
        form_of_ad = AdForm(instance=ad)
        return render(request,'create_ad.html',{'form_of_ad':form_of_ad})

def retrieve_ad(request,pk):
    ad = Ads.objects.get(id = pk)
    context = {
        'ad':ad
    }
    return render(request,'retrieve_ad.html',context=context)

def delete_ad(request,pk):
    ad = Ads.objects.get(id = pk)
    ad.delete()
    messages.success(request,'Обьект успешно удален.')
    return redirect('ads-list')

class AdsListView(ListView):
    template_name = "index.html"
    queryset = Ads.objects.all()
    context_object_name = "all_ads"

class AdsDeleteView(DeleteView):
    template_name = "delete_ad.html"
    queryset = Ads.objects.all()
    success_url = reverse_lazy('ads-list')



class AdsDetailView(DetailView):
    template_name = "retrieve_ad.html"
    queryset = Ads.objects.all()
    success_url = reverse_lazy('ads-list')

class AdsUpdateView(UpdateView):
    template_name = "update_ad.html"
    queryset = Ads.objects.all()
    form_class = AdForm

    def get_success_url(self):
        return reverse('ads-list')

class AdsCreateView(CreateView):
    template_name = "create_ad.html"
    queryset = Ads.objects.all()
    form_class = AdForm

    def get_success_url(self):
        return reverse('ads-list')






    


