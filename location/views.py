from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Country, State, City, Location
from .serializers import CountrySerializer, StateSerializer, CitySerializer, LocationSerializer


class CountryViewSet(ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class StateViewSet(ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer

    def list(self, request, *args, **kwargs):
        country_id = request.query_params.get('country_id')
        if country_id:
            queryset = self.queryset.filter(country_id=country_id)
        else:
            queryset = self.queryset
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)



class CityViewSet(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

    def list(self, request, *args, **kwargs):
        state_id = request.query_params.get('state_id')
        if state_id:
            queryset = self.queryset.filter(state_id=state_id)
        else:
            queryset = self.queryset
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    def list(self, request, *args, **kwargs):
        state_id = request.query_params.get('state_id')
        
        if state_id:
            queryset = self.queryset.filter(state_id=state_id) 
        else:
            queryset = self.queryset

        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
