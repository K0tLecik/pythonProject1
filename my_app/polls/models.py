import uuid

from django.db import models
from django.contrib.auth.models import User

# static choices
MONTHS = models.IntegerChoices('Miesiace', 'Styczeń Luty Marzec Kwiecień Maj Czerwiec Lipiec Sierpień Wrzesień Październik Listopad Grudzień')

SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )


class Team(models.Model):
    name = models.CharField(max_length=60)
    country = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.name}"


##Dublowało się z lab3
# class Person(models.Model):
#
#     name = models.CharField(max_length=60)
#     shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES, default=SHIRT_SIZES[0][0])
#     month_added = models.IntegerField(choices=MONTHS.choices, default=MONTHS.choices[0][0])
#     team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.SET_NULL)
#
#     def __str__(self):
#         return self.name

class Position(models.Model):
    # id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.name}"


class Person(models.Model):
    genders = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    )
    owner = models.ForeignKey(User, related_name='owned_people', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=genders)
    position = models.ForeignKey(Position, null=True, on_delete=models.SET_NULL)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name + ' ' + self.second_name}"