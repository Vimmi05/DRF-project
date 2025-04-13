from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from Home.models import * 
from Home.serializers import StudentSerializer

def Index(request):
    return render (request, "Home/home.html")

@api_view(['GET'])
def Home(request):
    data = Student.objects.all()
    print("data : ", data)
    serData = StudentSerializer(data, many = True)
    print("serData : ", serData)
    return Response({
        "data ": serData.data
    }, status=200)


# Create
@api_view(['POST']) #checking if request.method == POST by self, no need to explictly mention that
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
def getStudentApiView(request, id):
    student = Student.objects.get(id=id)
    serData = StudentSerializer(student)
    return Response({
        "data": serData.data
    }, status=200)

@api_view(['DELETE'])
def deleteStudentApiView(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return Response({
        "status": "Successfully Deleted"
    }, status=200)
    print("student : ", student)
