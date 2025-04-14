from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *

@api_view(['GET'])
def Website(request):
    return Response({
        "status":"success"
    }, status=200)

@api_view(['GET'])
def GetTask(request):
    data = TaskModel.objects.all()
    serData = TaskSerializer(data, many=True)
    data = serData.data
    return Response({"data":data}, status=200)
