from django.shortcuts import render
from rest_framework import generics, viewsets
from .serializers import (UserProfileSerializer,AgentListAPISerializers,
                          AgentDetailSerializers,
                          HousesSerializers,ReviewsSerializers,HousesCreateSerializer,
                          HousesDetailSerializers,HousesListAPISerializers,
                          HousesPhotoSerializers,MainSerializers)
from .models import (UserProfile,Agent,Amenity,
                     Houses,HousePhotos,
                     Rating,Main)
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class UserProfileViewSet(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class AgentListAPIViewSet(generics.ListAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentListAPISerializers

class AgentDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentDetailSerializers

class HousesListAPIViewSet(generics.ListAPIView):
    queryset = Houses.objects.all()
    serializer_class = HousesListAPISerializers
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['locations',]
    search_fields = ['name_houses', ]
    ordering_fields = ['price']


class HousesDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Houses.objects.all()
    serializer_class = HousesDetailSerializers

class HousesCreateViewSet(generics.CreateAPIView):
    queryset = Houses.objects.all()
    serializer_class = HousesCreateSerializer

class HousesViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Houses.objects.all()
    serializer_class = HousesSerializers

class ReviewsViewSet(generics.ListAPIView):
    queryset = Rating.objects.all()
    serializer_class = ReviewsSerializers


class MainViewSet(generics.ListAPIView):
    queryset = Main.objects.all()
    serializer_class = MainSerializers









