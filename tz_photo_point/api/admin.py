from django.contrib import admin
from .models import Rate


class RateAdmin(admin.ModelAdmin):
    list_display = ('id', 'currency_rate', 'pub_date')
    list_filter = ('pub_date',)


admin.site.register(Rate, RateAdmin)
