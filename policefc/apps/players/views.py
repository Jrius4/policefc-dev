from apps.players.models import Player
from apps.players.serializers import PlayerSerializer
from rest_framework import generics

# Create your views here.
class PlayerListCreate(generics.ListCreateAPIView):
     queryset = Player.objects.all()
     serializer_class = PlayerSerializer