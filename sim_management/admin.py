from django.contrib import admin
from .models import SimCard, Operator

@admin.register(Operator)
class OperatorAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(SimCard)
class SimCardAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'iccid', 'operator', 'status', 'balance', 'activation_date')
    list_filter = ('status', 'operator')
    search_fields = ('phone_number', 'iccid', 'owner_name')
    list_editable = ('status', 'balance')
    date_hierarchy = 'activation_date'
    list_select_related = ('operator',)