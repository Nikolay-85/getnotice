from notices.serializers import MessageSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics

class MessageApi(mixins.CreateModelMixin, generics.GenericAPIView):
    """
    This API creates new message in system.

    New message will be bulished to all clients.

    'text' field limited to 100 characters.

    'level' field not limited to some strict list of predefined values.

    NOTE: 'silent' level will not publish message but emulate publishing.    
    """
    serializer_class = MessageSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
