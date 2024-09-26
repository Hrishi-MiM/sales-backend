from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from .models import Call, Log
from .serializers import CallSerializer, LogSerializer
from rest_framework import status

class CallList(APIView):
    def get(self, request):
        calls = Call.objects.all()
        serializer = CallSerializer(calls, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = CallSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CallDetail(APIView):
    def get_object(self, id):
        try:
            return Call.objects.get(id=id)
        except Call.DoesNotExist:
            return None

    def get(self, request, id):
        call = self.get_object(id)
        if call is None:
            return JsonResponse({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = CallSerializer(call)
        return JsonResponse(serializer.data)

    def put(self, request, id):
        call = self.get_object(id)
        if call is None:
            return JsonResponse({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

        data = JSONParser().parse(request)
        serializer = CallSerializer(call, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        call = self.get_object(id)
        if call is None:
            return JsonResponse({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

        call.delete()
        return JsonResponse(status=status.HTTP_204_NO_CONTENT)

class LogList(APIView):
    def get(self, request, call_id):
        logs = Log.objects.filter(call_id=call_id)
        serializer = LogSerializer(logs, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, call_id):
        data = JSONParser().parse(request)
        data['call'] = call_id  # Associate the log with the call
        serializer = LogSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
