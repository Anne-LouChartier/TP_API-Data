from django.shortcuts import render
from rest_framework import generics
from TP_api_django.models import EggGroup, Item, Location, Move, Pokemon, PokemonEggGroup, PokemonFormGeneration, PokemonMove, PokemonStat, PokemonType, Stat, Type
from TP_api_django.serializers import EggGroupSerializer, ItemSerializer, LocationSerializer, MoveSerializer, PokemonSerializer, PokemonEggGroupSerializer, PokemonFormGenerationSerializer, PokemonMoveSerializer, PokemonStatSerializer, PokemonTypeSerializer, StatSerializer, TypeSerializer


# Create your views here.
class EggGroupList(generics.ListCreateAPIView):
    queryset = EggGroup.objects.all()
    serializer_class = EggGroupSerializer

class EggGroupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EggGroup.objects.all()
    serializer_class = EggGroupSerializer

class ItemList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class LocationList(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class MoveList(generics.ListCreateAPIView):
    queryset = Move.objects.all()
    serializer_class = MoveSerializer

class MoveDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Move.objects.all()
    serializer_class = MoveSerializer

class PokemonList(generics.ListCreateAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

class PokemonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

class PokemonEggGroupList(generics.ListCreateAPIView):
    queryset = PokemonEggGroup.objects.all()
    serializer_class = PokemonEggGroupSerializer

class PokemonEggGroupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PokemonEggGroup.objects.all()
    serializer_class = PokemonEggGroupSerializer

class PokemonFormGenerationList(generics.ListCreateAPIView):
    queryset = PokemonFormGeneration.objects.all()
    serializer_class = PokemonFormGenerationSerializer

class PokemonFormGenerationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PokemonFormGeneration.objects.all()
    serializer_class = PokemonFormGenerationSerializer

class PokemonMoveList(generics.ListCreateAPIView):
    queryset = PokemonMove.objects.all()
    serializer_class = PokemonMoveSerializer

class PokemonMoveDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PokemonMove.objects.all()
    serializer_class = PokemonMoveSerializer

class PokemonStatList(generics.ListCreateAPIView):
    queryset = PokemonStat.objects.all()
    serializer_class = PokemonStatSerializer

class PokemonStatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PokemonStat.objects.all()
    serializer_class = PokemonStatSerializer

class PokemonTypeList(generics.ListCreateAPIView):
    queryset = PokemonType.objects.all()
    serializer_class = PokemonTypeSerializer

class PokemonTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PokemonType.objects.all()
    serializer_class = PokemonTypeSerializer

class StatList(generics.ListCreateAPIView):
    queryset = Stat.objects.all()
    serializer_class = StatSerializer

class StatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stat.objects.all()
    serializer_class = StatSerializer

class TypeList(generics.ListCreateAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

class TypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
