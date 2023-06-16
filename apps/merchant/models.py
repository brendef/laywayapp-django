from django.db import models
from django.core.validators import int_list_validator


class FrequencySettings(models.Model):
    nameAdjective = models.CharField(max_length=50, unique=True, null=False)
    nameSingular = models.CharField(max_length=50, unique=True, null=False)
    namePlural = models.CharField(max_length=50, unique=True, null=False)
    days = models.IntegerField(unique=True, null=False)
    min = models.IntegerField(unique=False, null=False)
    max = models.IntegerField(unique=False, null=True)

    def __str__(self):
        return self.nameAdjective


class Merchant(models.Model):
    name = models.CharField(max_length=50, null=False)
    frequency = models.CharField(validators=[int_list_validator()], max_length=100)
    requireDeposit = models.BooleanField(default=False)
    minimumDepositPercentage = models.IntegerField(unique=False, null=False, default=0)
    minimumDepositAmount = models.IntegerField(unique=False, null=False, default=0)

    def __str__(self):
        return self.name
