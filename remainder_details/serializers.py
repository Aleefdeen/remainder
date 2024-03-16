from rest_framework import serializers
from .models import RemainderDetails
class RemainderDetailsSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = RemainderDetails
        fields = "__all__"