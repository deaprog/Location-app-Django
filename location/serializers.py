from rest_framework import serializers
from .models import Country, State, City, Location

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'alpha2', 'alpha3', 'iso', 'name']

class StateSerializer(serializers.ModelSerializer):
    country = serializers.SerializerMethodField()

    class Meta:
        model = State
        fields = ['id', 'name', 'country', 'country_id', 'abbr']

    def get_country(self, obj):
        country = Country.objects.filter(id=obj.country_id).first()
        return CountrySerializer(country).data if country else None


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name', 'state_id']

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'code', 'state_id', 'city', 'area_code', 'lat', 'lon', 'accuracy'] 
