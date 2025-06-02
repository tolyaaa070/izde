from rest_framework import serializers
from .models import (UserProfile,Agent,Amenity,
                     Houses,HousePhotos,
                     Rating,Main)

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username','last_name','first_name','email']


class AgentListAPISerializers(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = ['last_name', 'first_name','position','image']

class AgentDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = ['last_name','first_name','email','phone_number',
                  'position','image','language','company','areas','active_listing',
                  'experience','phone_number']

class AgentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = '__all__'

class AmenitySerializers(serializers.ModelSerializer):
    class Meta :
        model = Amenity
        fields = '__all__'

class HousesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Houses
        fields= ['name_houses',]
class ReviewsSerializers(serializers.ModelSerializer):
    houses = HousesSerializers(read_only=True, many=True)
    class Meta:
        model = Rating
        fields = ['houses','rating','comment']

class HousesListAPISerializers(serializers.ModelSerializer):
    get_avg_rating = serializers.SerializerMethodField()
    class Meta :
        model = Houses
        fields = ['get_avg_rating','name_houses','locations','price','square',
                  'bathroom','bathroom_icon','amenity']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()


class HousesDetailSerializers(serializers.ModelSerializer):
    amenity = AmenitySerializers(read_only=True, many=True)
    agent = AgentListAPISerializers(read_only=True, many=True)
    get_count_reviews = serializers.SerializerMethodField()
    get_avg_rating = serializers.SerializerMethodField()
    class Meta:
        model = Houses
        fields = ['get_count_reviews','get_avg_rating','name_houses', 'type','locations', 'price', 'square',
                  'bathroom', 'bathroom_icon', 'amenity', 'series', 'rooms',
                  'parking', 'parking_icon', 'floor','floor_icon','total_floors', 'about_property', 'rating', 'agent',
                  'min_stay', 'deposit']
    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

    def get_count_reviews(self, obj):
        return obj.get_count_reviews()


class HousesPhotoSerializers(serializers.ModelSerializer):
    class Meta :
        model = HousePhotos
        fields = '__all__'
class HousesCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Houses
        fields = '__all__'
class MainSerializers(serializers.ModelSerializer):
    houses = HousesSerializers(read_only=True,many=True)
    agents = AgentListAPISerializers(read_only=True,many = True)
    class Meta:
        model = Main
        fields = ['agents','houses']

