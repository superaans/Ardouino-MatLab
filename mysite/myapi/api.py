from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Dht11
from .serializers import DhtSerializer

import requests as rq



class Dhtviews(generics.CreateAPIView):
    queryset = Dht11.objects.all().order_by('dt')
    serializer_class = DhtSerializer


@api_view(['GET'])
def Dlist(request):
    all_data = Dht11.objects.all().order_by('dt')
    data = DhtSerializer(all_data, many=True).data
    return Response({'data': data})



def send_to_oussama(message):

    apiToken = '5775875672:AAFTJNjyuwOZ8qP0m55W0hZkRUz8m5vF4JM'
    chatID = '5080040962'
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    try:
        response = rq.post(apiURL, json={'chat_id': chatID, 'text': message})
    except Exception as e:
        print(e)


def send_to_ouidad(message):
    apiToken = '5775875672:AAFTJNjyuwOZ8qP0m55W0hZkRUz8m5vF4JM'
    chatID = '1064897564'
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    try:
        response = rq.post(apiURL, json={'chat_id': chatID, 'text': message})
    except Exception as e:
        print(e)


@api_view(['POST'])
def AddDht(request):
    serializer = DhtSerializer(data=request.data)
    if serializer.is_valid():

        serializer.save()
        if int(serializer.data.get('temp')) >= 20:
            Alerts.i +=1
            print( Alerts.i)
            if  Alerts.i >= 2:
                send_to_oussama(serializer.data.get('temp'))
                send_to_ouidad(serializer.data.get('temp'))
            if  Alerts.i >= 1 : send_to_oussama(serializer.data.get('temp'))

        else : Alerts.i=0
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Dhtviews(generics.CreateAPIView):
    queryset = Dht11.objects.all().order_by('dt')
    serializer_class = DhtSerializer

class Alerts:
    i = 0
