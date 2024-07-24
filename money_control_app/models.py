from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class MoneyControl(models.Model):
    TRANSACTION_TYPES = (
        ('IN', 'In'),
        ('OUT', 'Out'),
    )
    ACCOUNT_TYPES = (
        ('Cash', 'Cash'),
        ('Card', 'Card'),
    )
    CATEGORIES = (
        ('Taxi', 'Taxi'),
        ('Food', 'Food'),
        ('Health', 'Health'),
        ('Home', 'Home'),
        ('Park', 'Park'),
        ('Others', 'Others'),
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=3, choices=TRANSACTION_TYPES)
    account = models.CharField(max_length=10, choices=ACCOUNT_TYPES)
    category = models.CharField(max_length=20, choices=CATEGORIES, null=True, blank=True)
    date = models.DateField(null=True)
    description = models.TextField(blank=True)


    def __str__(self):
        return f"{self.date} - {self.type} - {self.amount} - {self.account}"


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField(null=True, blank=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.age} "