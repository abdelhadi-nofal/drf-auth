from django.urls import path,include
from django.contrib import admin
from .views import CarsListView,CarDetailsView

urlpatterns = [
    path('', CarsListView.as_view(), name='cars_api'), # /api/v1/posts/
    path('<int:pk>', CarDetailsView.as_view(), name='post_details_api'),
]