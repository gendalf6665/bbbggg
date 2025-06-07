from django.contrib import admin
from .models import SimCard, MCC, MNCOperator, MOBIL
from .utils import ICCIDValidator

@admin.register(SimCard)
class SimCardAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'iccid', 'operator', 'status', 'balance', 'activation_date')
    list_filter = ('status', 'operator')
    search_fields = ('phone_number', 'iccid', 'owner_name')
    list_editable = ('status', 'balance')
    date_hierarchy = 'activation_date'
    actions = ['validate_iccid_action']

    def validate_iccid_action(self, request, queryset):
        """Кастомное действие для валидации ICCID выбранных SIM-карт."""
        validator = ICCIDValidator()
        for sim in queryset:
            if sim.iccid:
                result = validator.validate_iccid(sim.iccid)
                sim.operator = result["operator"] if result["is_valid"] else "Неизвестный оператор"
                sim.save()
                self.message_user(request, f"ICCID {sim.iccid}: {result['message']}")
            else:
                self.message_user(request, f"SIM-карта {sim.phone_number}: ICCID не указан")

    validate_iccid_action.short_description = "Валидировать ICCID выбранных SIM-карт"

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