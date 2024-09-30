from rest_framework import serializers
from .models import TwilioConfig

class TwilioConfigurationSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = TwilioConfig
        fields = '__all__'
        read_only_fields = ('created_by', 'created_on', 'updated_on')
