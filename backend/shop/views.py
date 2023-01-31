from rest_framework import generics
from shop.serializer import TestSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from shop.models import ApiModel


class TestListView(generics.UpdateAPIView, generics.ListAPIView, generics.ListCreateAPIView):  # GET, PUT, POST
    serializer_class = TestSerializer
    queryset = ApiModel.objects.all()
