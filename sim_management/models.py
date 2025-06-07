from django.db import models

class Operator(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Название оператора')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = 'Оператор'
        verbose_name_plural = 'Операторы'

    def __str__(self):
        return self.name

class SimCard(models.Model):
    STATUS_CHOICES = (
        ('active', 'Активна'),
        ('inactive', 'Неактивна'),
        ('blocked', 'Заблокирована'),
    )

    iccid = models.CharField(max_length=20, unique=True, verbose_name='ICCID')
    phone_number = models.CharField(max_length=15, unique=True, verbose_name='Номер телефона')
    operator = models.ForeignKey(Operator, on_delete=models.SET_NULL, null=True, verbose_name='Оператор')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='inactive', verbose_name='Статус')
    activation_date = models.DateField(null=True, blank=True, verbose_name='Дата активации')
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name='Баланс')
    owner_name = models.CharField(max_length=100, blank=True, verbose_name='Владелец')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = 'SIM-карта'
        verbose_name_plural = 'SIM-карты'
        app_label = 'sim_management'

    def __str__(self):
        return f"{self.phone_number} ({self.iccid})"