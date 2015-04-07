#from django.contrib.auth.models import Message
from helloRest.models import Box, Hello
from rest_framework import serializers

class BoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Box
        fields = ('name', 'spin')

class HelloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hello
        fields = ('box', 'date')