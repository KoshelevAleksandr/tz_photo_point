from rest_framework import serializers

from .models import Rate


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('currency_rate', 'pub_date')
        model = Rate
