from .views import (UserProfileViewSet, AgentDetailViewSet, AgentListAPIViewSet,
                    HousesViewSet, HousesDetailViewSet,HousesCreateViewSet ,HousesListAPIViewSet,
                    ReviewsViewSet, MainViewSet)
from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    # path('main/', MainViewSet.as_view(), name='main'),
    path('user_profile/', UserProfileViewSet.as_view(), name='user'),
    path('agents/', AgentListAPIViewSet.as_view(), name='agents'),
    path('agents/<int:pk>/', AgentDetailViewSet.as_view(), name='agents'),
    path('houses/', HousesListAPIViewSet.as_view(), name='house'),
    path('houses/<int:pk>/', HousesDetailViewSet.as_view(), name='house'),
    # path('houses/', HousesListAPIViewSet.as_view(), name='house'),
    path('houses/create', HousesCreateViewSet.as_view(), name='house_create'),
    # path('rent/', RentListAPIViewSet.as_view(), name='rent'),
    # path('rent/<int:pk>/', RentHousesDetailViewSet.as_view(), name='rent'),
    path('reviews/', ReviewsViewSet.as_view(), name='reviews'),

]