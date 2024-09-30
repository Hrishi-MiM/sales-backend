from rest_framework import serializers
from .models import Assistant
from config.serializers import TwilioConfigurationSerializer 

class AssistantSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')
    config_data = TwilioConfigurationSerializer(source='config', read_only=True)

    class Meta:
        model = Assistant
        fields = '__all__'
        read_only_fields = ('created_by', 'created_on', 'updated_on')
