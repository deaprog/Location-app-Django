from django.db import models

class Country(models.Model):
    id = models.IntegerField(primary_key=True)
    alpha2 = models.CharField(max_length=2, blank=True, null=True)
    alpha3 = models.CharField(max_length=3, blank=True, null=True)
    iso = models.CharField(max_length=3, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False 
        db_table = 'countries'

class State(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    abbr = models.TextField(blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True) 

    class Meta:
        managed = False 
        db_table = 'states'

class City(models.Model):
    id = models.IntegerField(primary_key=True) 
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE, db_column='state_id')

    class Meta:
        managed = False 
        db_table = 'counties'

    def __str__(self):
        return self.name

class AbstractLocation(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.city}, {self.state}, {self.country}"

    class Meta:
        abstract = True

class Location(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=10, null=True, blank=True) 
    state_id = models.IntegerField(null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)  
    area_code = models.CharField(max_length=10, null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)
    accuracy = models.IntegerField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'zipcodes'
