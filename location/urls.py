from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CountryViewSet, StateViewSet, CityViewSet, LocationViewSet

router = DefaultRouter()
router.register(r'countries', CountryViewSet)
router.register(r'states', StateViewSet)
router.register(r'cities', CityViewSet)
router.register(r'locations', LocationViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
