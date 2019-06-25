# Import from peewee
from peewee import *
from flask import session

# load our config file
from config import Config

# Connect to the PostgresqlDatabase
db = PostgresqlDatabase(database=Config.DATABASE, user=Config.USERNAME, password=Config.SECRET_KEY,
host=Config.HOST, port=Config.PORT)

db.connect()

# class Earthquake(Model):
#     idearthquake = IntegerField(primary_key=True)
#     name = CharField()
#     magnitude = DecimalField()
#     latepc = DecimalField()
#     longepc = DecimalField()
#     date = DateTimeField()

#     class Meta:
#         database = db
#         db_table = 'earthquakes'

class AssessmentTable(Model):
    friendly_name = CharField()
    table_group = CharField(primary_key=True)
    select_helper = CharField()
    model = CharField()
    class Meta:
        database = db
        db_table = 'assessment_groups'

class AssessmentFramework(Model):
    id_af = PrimaryKeyField()
    path = CharField()
    title = CharField()
    short_title = CharField()
    table_group = CharField()
    class Meta:
        database = db
        db_table = 'assessment'



class Response_2d(Model):
    idsite = IntegerField(primary_key=True)
    idearthquake = IntegerField()
    idbuilding = IntegerField()
    sdr = DecimalField()
    pfa = DecimalField()
    idresponse = IntegerField()
    class Meta:
        database = db
        db_table = 'responses'

class Response_3d(Model):
    idsite = IntegerField(primary_key=True)
    idearthquake = IntegerField()
    idbuilding = IntegerField()
    psdr = DecimalField()
    pfa = DecimalField()
    idresponse = IntegerField()
    class Meta:
        database = db
        db_table = 'responses_3d'

class Building(Model):
    idbuilding = IntegerField(primary_key=True)
    level = IntegerField()
    data_type = CharField()
    class Meta:
        database = db
        db_table = 'buildings'    

class Sites(Model):
    idsite = IntegerField(primary_key=True)
    latitude = DecimalField()
    longitude = DecimalField()
    class Meta:
        database = db
        db_table = 'site_locations'

class Earthquake(Model):
    quakeid = IntegerField(primary_key=True)
    magnitude = DecimalField()
    earthquake = CharField()
    date = DateTimeField()

    class Meta:
        database = db
        db_table = 'earthquakes'