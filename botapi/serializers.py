# serializers.py
from rest_framework import serializers

from .models import Chat

class ChatSerializer(serializers.HyperlinkedModelSerializer):
    q = serializers.CharField(max_length=100)
    a = serializers.CharField(max_length=100)