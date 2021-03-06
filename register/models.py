from django.db import models
from register.validators import isalphavalidator
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone

# Create your models here.


class Team(models.Model):
    c1_first_name = models.CharField(max_length=80, blank=False)
    c1_last_name = models.CharField(max_length=80, blank=False)
    c1_email = models.EmailField(unique=True)
    c1_phone_number = PhoneNumberField(blank=False)
    c1_college = models.CharField(max_length=80)

    c2_first_name = models.CharField(max_length=80, blank=False)
    c2_last_name = models.CharField(max_length=80, blank=False)
    c2_email = models.EmailField(unique=True)
    c2_phone_number = PhoneNumberField(null=True, blank=True)
    c2_college = models.CharField(max_length=80)

    c3_first_name = models.CharField(max_length=80, blank=False)
    c3_last_name = models.CharField(max_length=80, blank=False)
    c3_email = models.EmailField(unique=True)
    c3_phone_number = PhoneNumberField(null=True, blank=True)
    c3_college = models.CharField(max_length=80)

    # contestant1 = models.ForeignKey(Leader, on_delete=models.CASCADE)
    # contestant2 = models.ForeignKey(Contestant, on_delete=models.CASCADE)
    # contestant3 = models.ForeignKey(Contestant, on_delete=models.CASCADE)
    registration_time = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=100, validators=[isalphavalidator], blank=False)

    def __str__(self):
        return self.name


# class Leader(models.Model):
#     first_name = models.CharField(max_length=80, blank=False)
#     last_name = models.CharField(max_length=80, blank=False)
#     email = models.EmailField(unique=True)
#     phone_number = PhoneNumberField()
#     college = models.CharField(max_length=80)
#
#
# class Contestant(models.Model):
#     first_name = models.CharField(max_length=80, blank=False)
#     last_name = models.CharField(max_length=80, blank=False)
#     email = models.EmailField(unique=True)
#     phone_number = PhoneNumberField(blank=True)
#     college = models.CharField(max_length=80)
#

