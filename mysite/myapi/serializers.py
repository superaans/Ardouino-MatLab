from rest_framework import serializers

from .models import Dht11




class DhtSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dht11
        fields = ('temp', 'hum' , 'dt')