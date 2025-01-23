import sqlite3
from django.core.management.base import BaseCommand
from location.models import Country, State, City, Location

class Command(BaseCommand):
    help = 'Import country, state, city, and zip code data from SQLite file'

    def handle(self, *args, **kwargs):
        conn = sqlite3.connect('allcountries.sqlite3') 
        cursor = conn.cursor()

        # Fetch countries
        cursor.execute('SELECT * FROM countries')
        countries = cursor.fetchall()
        for row in countries:
            country, created = Country.objects.get_or_create(name=row[3])  # Assuming name is in the 4th column

            # Fetch states for this country
            cursor.execute('SELECT * FROM states WHERE country_id = ?', (row[0],))
            states = cursor.fetchall()
            for state_row in states:
                state, created = State.objects.get_or_create(name=state_row[3], country=country)

                # Fetch cities for this state
                cursor.execute('SELECT * FROM zipcodes WHERE state_id = ?', (state_row[0],))
                zipcodes = cursor.fetchall()
                for zip_row in zipcodes:
                    city, created = City.objects.get_or_create(name=zip_row[3], state=state)

                    # Insert location data
                    Location.objects.create(
                        country=country,
                        state=state,
                        city=city,
                        zip_code=zip_row[1]
                    )
        conn.close()
        self.stdout.write(self.style.SUCCESS('Data imported successfully!'))
