from django.contrib import admin
from django.urls import path, include

from api.views import get_rates

from api.operations import create_new_currency_rate

urlpatterns = [
    path('get-current-usd/', get_rates),
    path("admin/", admin.site.urls)
]

