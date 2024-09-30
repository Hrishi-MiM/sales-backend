from rest_framework import serializers
from .models import Call, Log
from assistant.serializers import AssistantSerializer

class CallSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')
    assistant_data = AssistantSerializer(source='assistant', read_only=True)

    class Meta:
        model = Call
        fields = ('id', 'session_name', 'assistant', 'assistant_data', 'created_by', 'created_on', 'updated_on')
        read_only_fields = ('created_by', 'created_on', 'updated_on')

class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = '__all__'
        read_only_fields = ('created_on', 'updated_on')
