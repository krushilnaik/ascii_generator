from django.db import models
from django.core.validators import MinLengthValidator


class Letter(models.Model):
    """
    Model for a character.

    Example:

    Character "A" has representation

    .####.
    #....#
    #....#
    ######
    #....#
    #....#
    ......

    condensed to one "|"-seperated line
    """

    letter = models.CharField(max_length=1, unique=True)

    representation = models.TextField()
