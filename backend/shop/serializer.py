from .models import ApiModel
from rest_framework import serializers


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiModel
        fields = '__all__'
