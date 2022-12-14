from rest_framework import viewsets

from .serializers import DhtSerializer
from .models import Dht11

class DhtViewSet(viewsets.ModelViewSet):
    queryset = Dht11.objects.all().order_by('dt')
    serializer_class = DhtSerializer