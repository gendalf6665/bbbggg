from django.db import models

class MCC(models.Model):
    code = models.CharField(max_length=3, unique=True, verbose_name='Код MCC')
    country = models.CharField(max_length=50, verbose_name='Страна')

    class Meta:
        verbose_name = 'MCC код'
        verbose_name_plural = 'MCC коды'

    def __str__(self):
        return f"{self.code} ({self.country})"

class MNCOperator(models.Model):
    code = models.CharField(max_length=3, unique=True, verbose_name='Код MNC')
    operator = models.CharField(max_length=50, verbose_name='Оператор')

    class Meta:
        verbose_name = 'MNC оператор'
        verbose_name_plural = 'MNC операторы'

    def __str__(self):
        return f"{self.code} ({self.operator})"

class MOBIL(models.Model):
    code = models.CharField(max_length=2, unique=True, verbose_name='Код MOBIL')
    country = models.CharField(max_length=50, verbose_name='Страна')

    class Meta:
        verbose_name = 'MOBIL код'
        verbose_name_plural = 'MOBIL коды'

    def __str__(self):
        return f"{self.code} ({self.country})"

class SimCard(models.Model):
    STATUS_CHOICES = (
        ('active', 'Активна'),
        ('inactive', 'Неактивна'),
        ('blocked', 'Заблокирована'),
    )

    iccid = models.CharField(max_length=20, unique=True, verbose_name='ICCID')
    phone_number = models.CharField(max_length=15, unique=True, verbose_name='Номер телефона')
    operator = models.CharField(max_length=50, verbose_name='Оператор', blank=True, default='Неизвестный оператор')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='inactive', verbose_name='Статус')
    activation_date = models.DateField(null=True, blank=True, verbose_name='Дата активации')
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name='Баланс')
    owner_name = models.CharField(max_length=100, blank=True, verbose_name='Владелец')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = 'SIM-карта'
        verbose_name_plural = 'SIM-карты'

    def validate_iccid(self):
        """Валидация ICCID и определение оператора и страны."""
        from .utils import ICCIDValidator
        validator = ICCIDValidator()
        if self.iccid:
            result = validator.validate_iccid(self.iccid)
            if result["is_valid"]:
                self.operator = result["operator"]
            else:
                self.operator = "Неизвестный оператор"
            return result
        return {"is_valid": False, "message": "ICCID не указан", "operator": None, "country": None}

    def save(self, *args, **kwargs):
        """Автоматическое определение оператора при сохранении."""
        self.validate_iccid()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.phone_number} ({self.iccid})"