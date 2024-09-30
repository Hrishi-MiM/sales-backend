from rest_framework import serializers
from .models import Call, Log

class CallSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Call
        fields = '__all__'
        read_only_fields = ('created_by', 'created_on', 'updated_on')

class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = '__all__'
        read_only_fields = ('created_on', 'updated_on')
