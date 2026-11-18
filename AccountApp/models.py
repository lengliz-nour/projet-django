
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator, RegexValidator


# Validateur du numéro de téléphone
phone_validator = RegexValidator(
    regex=r"^\d{8}$",
    message="Le téléphone doit contenir 8 chiffres."
)


class User(AbstractUser):
    pass


class Specialty(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Doctor(User):
    license_number = models.CharField(
        max_length=6,
        unique=True,
        validators=[MinLengthValidator(6)]
    )

    phone = models.CharField(
        max_length=8,
        validators=[phone_validator]
    )

    specialties = models.ManyToManyField(Specialty)

    def __str__(self):
        return self.username


class Patient(User):
    national_id = models.CharField(
        max_length=8,
        unique=True,
        validators=[MinLengthValidator(8)]
    )

    phone = models.CharField(
        max_length=8,
        validators=[phone_validator]
    )

    birth_date = models.DateField()

    def __str__(self):
        return self.username
