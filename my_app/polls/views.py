from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Person, Position
from .serializers import PersonSerializer, PositionModelSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


@api_view(['GET', 'PUT', 'DELETE'])
def person_detail(request, pk):
    try:
        person = Person.objects.get(pk=pk)
    except Person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PersonSerializer(person)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def person_list(request):
    if request.method == 'GET':
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def person_list_by_name(request, search_string):
    if request.method == 'GET':
        persons = Person.objects.filter(first_name__icontains=search_string)
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def position_detail(request, pk):
    try:
        position = Position.objects.get(pk=pk)
    except Position.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PositionModelSerializer(position)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PositionModelSerializer(position, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        position.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def position_list(request):
    if request.method == 'GET':
        positions = Position.objects.all()
        serializer = PositionModelSerializer(positions, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def add_person(request):
    serializer = PersonSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def add_position(request):
    serializer = PositionModelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
