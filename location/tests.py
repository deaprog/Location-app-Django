from django.test import TestCase
from django.db import connection
from .models import Country, State, City, Location

class BaseTestCase(TestCase):
    def setUp(self):
        with connection.cursor() as cursor:
            cursor.execute("PRAGMA foreign_keys=OFF;")
        
        with connection.schema_editor() as schema_editor:
            for model in [Country, State, City, Location]:
                schema_editor.create_model(model)

    def tearDown(self):
        with connection.schema_editor() as schema_editor:
            for model in [Country, State, City, Location]:
                schema_editor.delete_model(model)

        with connection.cursor() as cursor:
            cursor.execute("PRAGMA foreign_keys=ON;")
