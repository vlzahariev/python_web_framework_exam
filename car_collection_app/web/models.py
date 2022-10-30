from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from car_collection_app.web.validators import MinLengthCustom, YearValidator


# Create your models here.


class Profile(models.Model):
    MAX_LEN_USERNAME = 10
    MIN_LEN_USERNAME = 2

    MAX_LEN_PASSWORD = 30
    MAX_LEN_FIRSTNAME = 30
    MAX_LEN_LASTNAME = 30

    username = models.CharField(
        max_length=MAX_LEN_USERNAME,
        validators=(MinLengthCustom(MIN_LEN_USERNAME),),
        blank=False,
        null=False,
    )

    email = models.EmailField(
        blank=False,
        null=False,
    )

    age = models.PositiveIntegerField(
        validators=(MinValueValidator(18),),
        blank=False,
        null=False,
    )

    password = models.CharField(
        max_length=MAX_LEN_PASSWORD,  # TODO: password field in forms
        blank=False,
        null=False,
    )

    first_name = models.CharField(
        max_length=MAX_LEN_FIRSTNAME,
        blank=True,
        null=True,
    )

    last_name = models.CharField(
        max_length=MAX_LEN_LASTNAME,
        blank=True,
        null=True,
    )

    profile_picture = models.URLField(
        blank=True,
        null=True,
    )


class Car(models.Model):
    MAX_LEN_TYPE = 10
    MAX_LEN_MODEL = 20
    MIN_LEN_MODEL = 2
    MAX_LEN_GENRE = 30

    SALOON = "Saloon"
    ESTATE = 'Estate'
    SPORTS_CAR = "Sports Car"
    PICKUP = "Pickup"
    CROSSOVER = "Crossover"
    MINIBUS = "Minibus"
    OTHER_CAR = "Other"

    CARS = (
        (SALOON, SALOON),
        (ESTATE, ESTATE),
        (SPORTS_CAR, SPORTS_CAR),
        (PICKUP, PICKUP),
        (CROSSOVER, CROSSOVER),
        (MINIBUS, MINIBUS),
        (OTHER_CAR, OTHER_CAR),
    )

    type = models.CharField(
        max_length=MAX_LEN_TYPE,
        choices=CARS,
        blank=False,
        null=False,

    )

    model = models.CharField(
        max_length=MAX_LEN_MODEL,
        validators=(MinLengthValidator(MIN_LEN_MODEL),),
        blank=False,
        null=False,
    )

    year = models.IntegerField(
        validators=(YearValidator,),
        blank=False,
        null=False,
    )

    image_url = models.URLField(
        blank=False,
        null=False,
    )

    price = models.FloatField(
        validators=(MinValueValidator(1),),
        blank=False,
        null=False,
    )

    class Meta:
        ordering = ('pk',)