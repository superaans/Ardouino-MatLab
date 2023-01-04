from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Dht11
from .serializers import DhtSerializer

import telegram
import requests


class Dhtviews(generics.CreateAPIView):
    queryset = Dht11.objects.all()
    serializer_class = DhtSerializer

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

def send_to_telegram(message):

    apiToken = '5775875672:AAFTJNjyuwOZ8qP0m55W0hZkRUz8m5vF4JM'
    chatID = '5080040962'
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
    except Exception as e:
        print(e)

