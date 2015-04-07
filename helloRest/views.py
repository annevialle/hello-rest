from django.shortcuts import render
#from django.contrib.auth.models import Message
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework import generics
from helloRest.models import Box, Hello
from helloRest.serializers import BoxSerializer, HelloSerializer
from django.views.decorators.csrf import csrf_exempt


class BoxDetail(generics.RetrieveUpdateAPIView):
	queryset = Box.objects.all()
	serializer_class = BoxSerializer

class DeactivateBox(generics.RetrieveUpdateAPIView):
	queryset = Box.objects.all()
	serializer_class = BoxSerializer

class HelloDetail(generics.RetrieveUpdateAPIView):
	queryset = Hello.objects.all()
	serializer_class = HelloSerializer

@csrf_exempt
def activate_box(request, sender, receiver):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'PUT':
        box_receiver = Box.objects.get(pk=receiver)
        box_receiver.spin = True
        box_receiver.save()

        box_sender = Box.objects.get(pk=sender)

        message = Hello.objects.create(boxSender=box_sender, boxReceiver=box_receiver)
        message.save()

        return HttpResponse(status=201)
    else:
    	return HttpResponse(status=404)

@csrf_exempt
def deactivate_box(request, pk):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'PUT':
        box = Box.objects.get(pk=pk)
        box.spin = False
        box.save()
        return HttpResponse(status=201)
    else:
    	return HttpResponse(status=404)
