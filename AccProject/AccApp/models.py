from django.db import models

# Create your models here.

class User(models.Model):
    userName = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Account(models.Model):
    accountName = models.CharField(max_length=50)
    accountType = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    userName = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Category(models.Model):
    categoryName = models.CharField(max_length=50)
    categoryType = models.CharField(max_length=50)
    userName = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    transactionType = models.CharField(max_length=50)
    transactionAmount = models.DecimalField(max_digits=10, decimal_places=2)
    transactionDate = models.DateField()
    accountName = models.ForeignKey(Account, on_delete=models.CASCADE)
    categoryName = models.ForeignKey(Category, on_delete=models.CASCADE)
    shopName = models.CharField(max_length=50)
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.name
