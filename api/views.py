from django.shortcuts import render

#Rest Framework
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import InfoSerializer

from .models import Info
# Create your views here.

@api_view(['GET'])
def InfoOverview(request):
	api_url = {
		'Create': '/info-create/',
		'Read': '/info-read/<str:pk>/',
		'Update': '/info-update/<str:pk>/',
		'Delete': '/info-list/<str:pk>/',
		'List': '/info-list/',
	}
	return Response(api_url)

@api_view(['GET'])
def InfoList(request):
	infos = Info.objects.all()
	serializer = InfoSerializer(infos, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def InfoDetail(request, pk):
	info = Info.objects.get(id=pk)
	serializer = InfoSerializer(info, many=False)
	return Response(serializer.data)

@api_view(['POST'])
def InfoCreate(request):
	serializer = InfoSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)