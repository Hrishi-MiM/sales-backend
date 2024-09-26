from rest_framework import serializers
from .models import TwilioConfig

class TwilioConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TwilioConfig
        fields = '__all__'
