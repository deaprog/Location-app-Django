# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Counties(models.Model):
    state_id = models.IntegerField(blank=True, null=True)
    abbr = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    county_seat = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'counties'
        unique_together = (('state_id', 'abbr', 'name'),)


class Countries(models.Model):
    alpha2 = models.CharField(unique=True, max_length=2)
    alpha3 = models.CharField(max_length=3, blank=True, null=True)
    iso = models.CharField(max_length=3, blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'countries'


class DjangoAdminLog(models.Model):
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class LocationCity(models.Model):
    name = models.CharField(max_length=100)
    state = models.ForeignKey('LocationState', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'location_city'


class LocationCountry(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'location_country'


class LocationLocation(models.Model):
    zip_code = models.CharField(max_length=10, blank=True, null=True)
    city = models.ForeignKey(LocationCity, models.DO_NOTHING, blank=True, null=True)
    country = models.ForeignKey(LocationCountry, models.DO_NOTHING, blank=True, null=True)
    state = models.ForeignKey('LocationState', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'location_location'


class LocationState(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(LocationCountry, models.DO_NOTHING)
    abbr = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'location_state'


class Meta(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'meta'


class States(models.Model):
    country_id = models.IntegerField()
    abbr = models.CharField(max_length=2)
    name = models.CharField(unique=True, max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'states'
        unique_together = (('abbr', 'country_id'),)


class Zipcodes(models.Model):
    code = models.CharField(max_length=10)
    state_id = models.IntegerField(blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    area_code = models.CharField(max_length=3, blank=True, null=True)
    lat = models.TextField(blank=True, null=True)  # This field type is a guess.
    lon = models.TextField(blank=True, null=True)  # This field type is a guess.
    accuracy = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zipcodes'
        unique_together = (('state_id', 'code', 'city'),)
