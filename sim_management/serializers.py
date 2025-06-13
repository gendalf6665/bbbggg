from rest_framework import serializers
from .models import SimCard, ExternalBot

class SimCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimCard
        fields = ['id', 'iccid', 'phone_number', 'status', 'balance', 'created_at', 'updated_at']

class ExternalBotSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExternalBot
        fields = ['id', 'name', 'api_token', 'api_url', 'is_active']