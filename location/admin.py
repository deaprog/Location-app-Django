from django.contrib import admin
from .models import Country, State, City, Location

admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Location)
