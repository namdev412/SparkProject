from django.db import models

# Create your models here.

class Manager(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=255, null=True)
    Password = models.CharField(max_length=120, null= True)
    Contact_Number = models.IntegerField()
    Created_Date= models.DateTimeField(auto_now_add=True)

class Customer(models.Model):
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=100)
    Password = models.CharField(max_length=80)
    Contact = models.IntegerField()
    Registration_date = models.DateTimeField(auto_now_add=True)

class SavingsAccount(models.Model):
    Member = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Account_no = models.IntegerField()
    Account_Balance = models.FloatField(max_length=100, null=True)
    Creted_date = models.DateTimeField(auto_now_add=True)

class Transactions(models.Model):
    Member = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Transaction_type = models.CharField(max_length=50)
    Transaction_amount = models.FloatField(max_length=50, null=True)
    Bal_before_tansaction = models.FloatField(max_length=50)
    Bal_after_transaction = models.FloatField(max_length=50)
    Transaction_Date = models.DateTimeField(auto_now_add=True)