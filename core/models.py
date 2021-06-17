from django.db import models
from django.conf import settings
from datetime import datetime
# Create your models here.

class Client(models.Model):
    """Client's model"""
    payer = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        help_text="Payer name",
        verbose_name="payer",
    )
    points = models.IntegerField(
        null=False,
        blank=False,
        help_text="Points",
        verbose_name="points",
    )
    timestamp = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        # return the string representation
        return self.payer


class Spend(models.Model):
    """Client's spend model"""
    # payer = models.CharField(
    #     max_length=255,
    #     null=False,
    #     blank=False,
    #     help_text="Payer name",
    #     verbose_name="payer",
    # )
    points = models.IntegerField(
        null=False,
        blank=False,
        help_text="Points",
        verbose_name="points",
    )
    timestamp = models.DateTimeField(
        auto_now_add=True
    )
    #
    # def __str__(self):
    #     # return the string representation
    #     return self.points


class PointBalance(models.Model):
    """Client's Point Balance model"""
    payer = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        help_text="Payer name",
        verbose_name="payer",
    )
    points = models.IntegerField(
        null=False,
        blank=False,
        help_text="Points",
        verbose_name="points",
    )
    timestamp = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        # return the string representation
        return self.payer


class SpendFinal(models.Model):
    """Client's SpendFinal model"""
    payer = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        help_text="Payer name",
        verbose_name="payer",
    )
    points = models.IntegerField(
        null=False,
        blank=False,
        help_text="Points",
        verbose_name="points",
    )
    timestamp = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        # return the string representation
        return self.payer