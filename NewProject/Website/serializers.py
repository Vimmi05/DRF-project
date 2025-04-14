from rest_framework.serializers import ModelSerializer
from .models import *

class TaskSerializer(ModelSerializer):
    class Meta:
        model = TaskModel
        fields = '__all__'