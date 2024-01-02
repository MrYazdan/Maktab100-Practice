from django.shortcuts import render
from rest_framework import generics, serializers

from apps.core.models import About


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'


class AboutListCreateApiView(generics.ListCreateAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
