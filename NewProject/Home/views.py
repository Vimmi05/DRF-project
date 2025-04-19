from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from Home.models import * 
from Home.serializers import StudentSerializer
from rest_framework.permissions import IsAuthenticated

def Index(request):
    return render (request, "Home/home.html")

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def Home(request):
    data = Student.objects.all()
    print("data : ", data)
    serData = StudentSerializer(data, many = True)
    print("serData : ", serData)
    return Response({
        "data ": serData.data
    }, status=200)


# Create
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createStudentApiView(request):
    # how to get data from frontend
    data = request.data #json format
    serData = StudentSerializer(data=data)
    try:
        if serData.is_valid():
            serData.save()
            return Response({
                "status": "Success"}, status=200
            )
        else:
            return Response({
            "status": "Failed {serData.errors}"}, status=400
        )
    except:
        return Response({
            "status": "Failed"}, status=400
        )

#UPDATE
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateStudentApiView(request, id):
    student = Student.objects.get(id=id)
    data = request.data
    serData = StudentSerializer(student, data=data, partial=True)
    try:
        if serData.is_valid():
            serData.save()
            return Response({
                "status":"Successfully Updated"}, status=200
            )
        else:
            return Response({
                "status":"Failed {serData.errors}"}, status=400
            )
    except:
        return Response({
            "status":"Failed"}, status=400
        )

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getStudentApiView(request, id):
    student = Student.objects.get(id=id)
    serData = StudentSerializer(student)
    return Response({
        "data": serData.data
    }, status=200)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteStudentApiView(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return Response({
        "status": "Successfully Deleted"
    }, status=200)
    print("student : ", student)

