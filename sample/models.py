from django.db import models
from django.contrib.auth.models import User

class Issuer(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.name

class Profile(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    accredited = models.BooleanField(blank=True, null=True)

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name
    
class Offering(models.Model):
    offering_name = models.CharField(max_length=30, blank=True, null=True)
    issuer = models.ForeignKey(Issuer, on_delete=models.CASCADE)
    notes = models.TextField(default='', blank=True, null=True)

    def __str__(self):
        return self.offering_name

class Investment(models.Model):
    amount = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



