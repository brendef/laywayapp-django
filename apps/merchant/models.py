from django.db import models


class FrequencySettings(models.Model):
    nameAdjective = models.CharField(max_length=50, unique=True, null=False)
    nameSingular = models.CharField(max_length=50, unique=True, null=False)
    namePlural = models.CharField(max_length=50, unique=True, null=False)
    days = models.IntegerField(unique=True, null=False)
    min = models.IntegerField(unique=False, null=False)
    max = models.IntegerField(unique=False, null=True)

    def __str__(self):
        return self.nameAdjective


class InstallmentConfiguration(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False)
    frequency = models.ManyToManyField(FrequencySettings)
    active = models.BooleanField(default=False)
    requireDeposit = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name


class Merchant(models.Model):
    name = models.CharField(max_length=50, null=False)
    installmentConfiguration = models.OneToOneField(
        InstallmentConfiguration, on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

    # deductionDays: {
    #     days: [
    #         {
    #             name: 1,
    #             day: 1,
    #         }
    #     ],
    #     relative: true,
    # },
    # requireDeposit: true,
    # dates: [],
    # startDate: 0,
    # endDate: 0,
    # minimumDepositPercentage: 0,
    # minimumDepositAmount: 0,
    # currency: 1,
