from rest_framework import serializers
from Home.models import *

# Suggested code may be subject to a license. Learn more: ~LicenseLog:1830557239.
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"