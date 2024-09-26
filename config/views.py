from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from .models import TwilioConfig
from .serializers import TwilioConfigurationSerializer
from rest_framework import status

class TwilioConfigurationList(APIView):
    def get(self, request):
        configurations = TwilioConfig.objects.all()
        serializer = TwilioConfigurationSerializer(configurations, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = TwilioConfigurationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TwilioConfigurationDetail(APIView):
    def get_object(self, id):
        try:
            return TwilioConfig.objects.get(id=id)
        except TwilioConfig.DoesNotExist:
            return None

    def get(self, request, id):
        configuration = self.get_object(id)
        if configuration is None:
            return JsonResponse({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = TwilioConfigurationSerializer(configuration)
        return JsonResponse(serializer.data)

    def put(self, request, id):
        configuration = self.get_object(id)
        if configuration is None:
            return JsonResponse({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

        data = JSONParser().parse(request)
        serializer = TwilioConfigurationSerializer(configuration, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        configuration = self.get_object(id)
        if configuration is None:
            return JsonResponse({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

        configuration.delete()
        return JsonResponse(status=status.HTTP_204_NO_CONTENT)
