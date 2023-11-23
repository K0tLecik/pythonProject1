from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Person, Position
from .serializers import PersonSerializer
from .permissions import IsOwner

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def person_list(request):
    """
    Lista wszystkich obiektów modelu Person.
    """
    if request.method == 'GET':
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsOwner])
def person_detail(request, pk):
    """
    Zwraca pojedynczy obiekt typu Person.
    """
    try:
        person = Person.objects.get(pk=pk)
    except Person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = PersonSerializer(person)
    return Response(serializer.data)

@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])  # Ustawienie autentykacji za pomocą tokena
@permission_classes([IsOwner, IsAuthenticated])
def person_delete(request, pk):
    """
    Widok pozwalający na edycję i usuwanie obiektów typu Person.
    """
    try:
        person = Person.objects.get(pk=pk)
    except Person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsOwner, IsAuthenticated])
def person_update(request, pk):
    """
    Widok pozwalający na edycję i usuwanie obiektów typu Person.
    """
    try:
        person = Person.objects.get(pk=pk)
    except Person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def position_members(request, stanowisko_id):
    """
    Widok wyświetlający wszystkie osoby przypisane do danego stanowiska.
    """
    try:
        stanowisko = Position.objects.get(pk=stanowisko_id)
    except Position.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        osoby = Person.objects.filter(stanowisko=stanowisko)
        serializer = PersonSerializer(osoby, many=True)
        return Response(serializer.data)