from django.contrib import admin
from django.urls import path, include

from api.views import get_rates

urlpatterns = [
    path('get-current-usd/', get_rates),
]
