from django.db import models

SEX_CHOICES = (
    ("FEMALE", "Female"),
    ("MALE", "Male"),
    ("OTHER", "other")
)


# Create your models here.
class Employee(models.Model):
    employee_account_number = models.CharField(max_length=100, primary_key=True)
    ssn = models.CharField(max_length=100, null = True, blank=True)
    employee_email = models.EmailField(max_length=100, null = True, blank=True)
    first_name = models.CharField(max_length=100, null = True, blank=True)
    last_name = models.CharField(max_length=100, null = True, blank=True)
    middle_name = models.CharField(max_length=100, null = True, blank=True)
    employee_sex = models.CharField(max_length=50, choices=SEX_CHOICES, default="OTHER", null = True, blank=True)

class Customer(models.Model):
    customer_account_number = models.CharField(max_length=100, primary_key=True)
    customer_email = models.EmailField(max_length=100, null = True, blank=True)
    first_name = models.CharField(max_length=100, null = True, blank=True)
    last_name = models.CharField(max_length=100, null = True,blank=True)
    middle_name = models.CharField(max_length=100, null = True, blank=True)
    age = models.IntegerField(null = True, blank=True)
