from .models import Houses
from django_filters.rest_framework import FilterSet

class HousesFilter(FilterSet):
    class Meta:
       model = Houses
       fields = {
           'houses_name': ['exact'],
           'price': ['gt', 'lt']
       }

