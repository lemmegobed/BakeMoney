from django.db import models
from django.contrib.auth.models import AbstractUser

class Transaction(models.Model):
    CATEGORY_CHOICES = [
        ('income', 'Income'),
        ('expense', 'Expense'),
    ]

    date = models.DateField(auto_now_add=True)
    description = models.CharField(max_length=255)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.description} ({self.get_category_display()}) - ฿{self.amount}"