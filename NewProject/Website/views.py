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

@api_view(['POST'])
def CreateTask(request):
    data =  TaskModel.objects.all()
    serData = TaskSerializer(data, many=True)

    if serData.is_valid():
        serData.save()
        return Response({"status":"created"}, status=200)
    else:
        return Response({"status ": f"Failed {serData.errors}"}, status=400)

@api_view(['PUT'])
def UpdateTask(request, id):
    TaskData = TaskModel.objects.get(id=id)
    data = request.data #from frontend
    serData = TaskSerializer(TaskData, data=data, partial=True)

    if serData.is_valid():
        serData.save()
        print("Updated")
        return Response({"status ": "Updated"}, status=200)
    else:
        return Response({"status ": f"Failed {serData.errors}"}, status=400)

@api_view(['DELETE'])
def DeleteTask(request, id):
    data = TaskModel.objects.get(id=id)
    data.delete()
    return Response({"status ": "Deleted"}, status=200)