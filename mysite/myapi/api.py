from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Dht11
from .serializers import DhtSerializer

@api_view(['GET'])
def Dlist(request):
    all_data = Dht11.objects.all()
    data = DhtSerializer(all_data, many=True).data
    return Response({'data': data})

@api_view(['POST'])
def AddDht(request):
    serializer = DhtSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Dhtviews(generics.CreateAPIView):
    queryset = Dht11.objects.all()
    serializer_class = DhtSerializer