from django.contrib import admin
from .models import SimCard, MCC, MNCOperator, MOBIL, ExternalBot

@admin.register(SimCard)
class SimCardAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'iccid', 'status', 'balance', 'updated_at')
    list_filter = ('status',)
    search_fields = ('phone_number', 'iccid')

@admin.register(MCC)
class MCCAdmin(admin.ModelAdmin):
    list_display = ('code', 'country')
    search_fields = ('code', 'country')

@admin.register(MNCOperator)
class MNCOperatorAdmin(admin.ModelAdmin):
    list_display = ('code', 'operator')
    search_fields = ('code', 'operator')

@admin.register(MOBIL)
class MOBILAdmin(admin.ModelAdmin):
    list_display = ('code', 'country')
    search_fields = ('code', 'country')

@admin.register(ExternalBot)
class ExternalBotAdmin(admin.ModelAdmin):
    list_display = ('name', 'api_url', 'is_active', 'updated_at')
    list_filter = ('is_active',)
    search_fields = ('name', 'api_url')