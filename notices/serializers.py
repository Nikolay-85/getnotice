from django.forms import widgets
from rest_framework import serializers
import redis, json
from django.conf import settings
from datetime import datetime
import calendar


class MessageSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    text = serializers.CharField(required=True, allow_blank=False, max_length=100)
    level = serializers.CharField(required=False, allow_blank=True, max_length=100, default='candidate')

    def create(self, validated_data):
        """
        Create message and publish.
        """
        d = datetime.utcnow()
        unixtime = calendar.timegm(d.utctimetuple())

        message = {
            "text": validated_data["text"],
            "level": validated_data["level"],
            "time": unixtime
        }
        if message["level"] != 'silent':
            r = redis.Redis(connection_pool=settings.REDIS_POOL)
            r.publish('broadcast', json.dumps(message))
        return message
        