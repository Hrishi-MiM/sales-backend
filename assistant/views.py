from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from .models import Assistant
from .serializers import AssistantSerializer
from rest_framework import status

class AssistantList(APIView):
    def get(self, request):
        assistants = Assistant.objects.all()
        serializer = AssistantSerializer(assistants, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = AssistantSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AssistantDetail(APIView):
    def get_object(self, id):
        try:
            return Assistant.objects.get(id=id)
        except Assistant.DoesNotExist:
            return None

    def get(self, request, id):
        assistant = self.get_object(id)
        if assistant is None:
            return JsonResponse({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = AssistantSerializer(assistant)
        return JsonResponse(serializer.data)

    def put(self, request, id):
        assistant = self.get_object(id)
        if assistant is None:
            return JsonResponse({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

        data = JSONParser().parse(request)
        serializer = AssistantSerializer(assistant, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        assistant = self.get_object(id)
        if assistant is None:
            return JsonResponse({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

        assistant.delete()
        return JsonResponse(status=status.HTTP_204_NO_CONTENT)
