from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Inmates
from .serializers import *

@api_view(['GET', 'POST'])
def accounts_list(request):
    if request.method == 'GET':
        data = Inmates.objects.all()

        serializer = InmatesSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = InmatesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
def accounts_detail(request, pk):
    try:
        Inmates = Inmates.objects.get(pk=pk)
    except Inmates.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = InmatesSerializer(Inmates, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Inmates.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)