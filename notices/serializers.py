from django.forms import widgets
from rest_framework import serializers
from models import Message


class MessageSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    text = serializers.CharField(required=True, allow_blank=True, max_length=100)
    level = serializers.CharField(required=False, allow_blank=True, max_length=100, default='candidate')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return True
        return Message.objects.create(**validated_data)

