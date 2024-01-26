from rest_framework.decorators import api_view

from .models import Rate
from .operations import request_currency_rate
from .serializers import RateSerializer
from rest_framework.response import Response


@api_view(['GET'])
def get_rates(request):
    limit = 10
    rates = Rate.objects.all().order_by('-id')
    current_rate = rates[0]
    last_rates = rates[1:limit + 1]

    serializer_current_rate = RateSerializer(current_rate)
    serializer_last_rates = RateSerializer(last_rates, many=True)
    content = {
        'current_rate': serializer_current_rate.data,
        'last 10': serializer_last_rates.data
    }
    return Response(content)
