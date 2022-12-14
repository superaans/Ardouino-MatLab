from django.urls import include, path
from rest_framework import routers
from . import views

from .api import *

router = routers.DefaultRouter()
router.register(r'dht', views.DhtViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls',
    namespace='rest_framework')),
    path('api/list', Dlist, name='DHT11List'),
    path('api/post', AddDht, name='DHTPost'),

]