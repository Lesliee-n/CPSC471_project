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

class Cinema(models.Model):
    cinema_id = models.CharField(max_length=100, primary_key=True)
    city = models.CharField(max_length=100, null = True, blank=True)
    state = models.CharField(max_length=100, null = True, blank=True)
    zip = models.CharField(max_length=100, null = True, blank=True)
    cinema_email = models.EmailField(max_length=100, null = True, blank=True)
    cinema_phone = models.CharField(max_length=50, null = True, blank=True)

class Movie(models.Model):
    cinema_id = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    movie_id = models.CharField(max_length=100, primary_key=True)
    description = models.CharField(max_length=250, null=True, blank=True)
    duration = models.FloatField(null = True, blank=True)
    movie_title = models.CharField(max_length=50, null = True, blank=True)

class Concession_stand(models.Model):
    station_number = models.IntegerField(primary_key=True)
    menu = models.CharField(max_length=250, null=True, blank=True)
    cinema_id = models.ForeignKey(Cinema, on_delete=models.CASCADE)

class Show_time(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    start_time = models.IntegerField(null = True, blank=True)
    end_time = models.IntegerField(null = True, blank=True)
    date = models.CharField(max_length=50, null = True, blank=True)

class Ticket(models.Model):
    show_time_movie_id = models.ForeignKey(Show_time, on_delete=models.CASCADE)
    seat_number = models.IntegerField(null = True, blank=True)
    row_letter = models.CharField(max_length = 2, null = True, blank=True)
    classification = models.CharField(max_length=50, null = True, blank=True)
    price = models.FloatField(null = True, blank=True)
    date = models.CharField(max_length=50, null = True, blank=True)
    customer_account_number =  models.ForeignKey(Customer, on_delete=models.CASCADE)

class Order(models.Model):
    customer_account_number = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_number = models.IntegerField(primary_key=True)
    items_ordered = models.CharField(max_length=250, null=True, blank=True)
    pick_up_time = models.IntegerField(null=True, blank=True)
    concession_stand_number = models.ForeignKey(Concession_stand, on_delete=models.CASCADE)

class Transaction_receipt(models.Model):
    customer_account_number = models.ForeignKey(Customer, on_delete=models.CASCADE)
    transaction_number = models.IntegerField(primary_key=True)
    receipt = models.IntegerField(null=True, blank=True)
    amount = models.FloatField(null=True, blank=True)
    items = models.CharField(max_length=100, null = True, blank=True)
    date = models.CharField(max_length=50, null = True, blank=True)