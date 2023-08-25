from django.shortcuts import render
from django.urls import path

from .views import (
    # ads_list,
    AdsListView,
    category_list,
    create_ad,
    # update_ad,
    AdsUpdateView,
    AdsDeleteView,
    retrieve_ad,
    # delete_ad)
    AdsDetailView,
    AdsCreateView
    )

urlpatterns = [
    path("", AdsListView.as_view(), name="ads-list"),
    # path("", ads_list, name="ads-list"),
    path("category",category_list, name="category-list"),
    path('create',  AdsCreateView.as_view(), name="create_ad"),
    path('update/<int:pk>/', AdsUpdateView.as_view(), name="update_ad"),
    path('<int:pk>/', retrieve_ad, name = "retrieve_ad"),
    path('delete/<int:pk>', AdsDeleteView.as_view(), name = "delete_ad")
    ]