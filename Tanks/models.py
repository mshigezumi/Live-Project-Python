from django.db import models

GENERATION_CHOICES = [
    ('1st','1st'),
    ('2nd','2nd'),
    ('3rd','3rd'),
    ('4th','4th'),
]

TYPE_CHOICES = [

]

# change to tank variant?
class Tank(models.Model): # need 2 related tables and a widget linked to this class
    name = models.CharField(max_length=120, blank=False)
    country = models.CharField(max_length=120, default='-')
    generation = models.CharField(max_length=120, choices=GENERATION_CHOICES)
    year = models.IntegerField(default=0)
    weight = models.TextField(default='-')
    crew = models.CharField(max_length=120, default='-')
    main_armament = models.TextField(default='-')
    rounds = models.IntegerField(default=0)
    autoloader = models.BooleanField(default=False)
    secondary_armaments = models.TextField(default='-')
    remote_weapons_system = models.BooleanField(default=False)
    active_protection_system = models.BooleanField(default=False)
    engine = models.TextField(default='-')
    power_to_weight_ratio = models.CharField(max_length=120, default='-')
    transmission = models.TextField(default='-')
    suspension = models.TextField(default='-')
    maximum_speed = models.TextField(default='-')
    range = models.CharField(max_length=120, default='-')
    length = models.CharField(max_length=120, default='-')
    width = models.CharField(max_length=120, default='-')
    height = models.CharField(max_length=120, default='-')
    # type = models.CharField(max_length=60) #maybe shouldn't use type? since they're all MBTs

    objects = models.Manager()

    def __str__(self):
        return self.name

# add tech specs as a seperate catagory? Need to think of things that can be linked to multiple tanks so it can be reused and referenced in the database
# should probably reformat the database to have a country table link to all the tanks and possibly add all the following attributes to each tank entry?
# unless I can find common things that will link to multiple tanks

# need to create a model for country and one for base tank which is referenced by the Tank model, which is specifically that variant in which I can add the other attributes to

class Country(models.Model):
    country = models.CharField(max_length=60)

    objects = models.Manager()

class BaseTank(models.Model):
    name = models.CharField(max_length=60)

    objects = models.Manager()