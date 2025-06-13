from django.db import models

class MCC(models.Model):
    code = models.CharField(max_length=3, unique=True)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.code} ({self.country})"

class MNCOperator(models.Model):
    code = models.CharField(max_length=3, unique=True)
    operator = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.code} ({self.operator})"

class MOBIL(models.Model):
    code = models.CharField(max_length=3, unique=True)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.code} ({self.country})"

class SimCard(models.Model):
    iccid = models.CharField(max_length=22, unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    status = models.CharField(max_length=20, choices=[
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('suspended', 'Suspended'),
    ])
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.phone_number} ({self.iccid})"

class ExternalBot(models.Model):
    name = models.CharField(max_length=100, unique=True)
    api_token = models.CharField(max_length=100)
    api_url = models.URLField(max_length=200)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name