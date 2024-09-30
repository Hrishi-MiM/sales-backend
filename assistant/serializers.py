from rest_framework import serializers
from .models import Assistant

class AssistantSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Assistant
        fields = '__all__'
        read_only_fields = ('created_by', 'created_on', 'updated_on')
