import graphene
from graphene_django import DjangoObjectType

from my_app.polls.models import Person, Position


class PersonType(DjangoObjectType):
    class Meta:
        model = Person
        fields = ("id", "owner", "first_name", "second_name", "gender", "position", "date_added")


class PositionType(DjangoObjectType):
    class Meta:
        model = Position
        fields = ("id", "name", "description")


class Query(graphene.ObjectType):
    all_teams = graphene.List(PositionType)
    person_by_id = graphene.Field(PersonType, id=graphene.Int(required=True))
    all_persons = graphene.List(PersonType)
    person_by_name = graphene.Field(PersonType, name=graphene.String(required=True))
    find_persons_name_by_phrase = graphene.List(PersonType, substr=graphene.String(required=True))

    def resolve_all_posiitons(root, info):
        return Position.objects.all()

    def resolve_person_by_id(root, info, id):
        try:
            return Person.objects.get(pk=id)
        except Person.DoesNotExist:
            raise Exception('Invalid person Id')

    def resolve_person_by_name(root, info, name):
        try:
            return Person.objects.get(first_name=name)
        except Person.DoesNotExist:
            raise Exception(f'No Person with name \'{name}\' found.')

    def resolve_all_persons(root, info):
        """ zwraca również wszystkie powiązane obiekty team dla tego obiektu Person"""
        return Person.objects.select_related("position").all()

    def resolve_find_persons_name_by_phrase(self, info, substr):
        return Person.objects.filter(first_name__icontains=substr)

    filter_persons_by_name_fragment = graphene.List(PersonType, fragment=graphene.String(required=True))

    def resolve_filter_persons_by_name_fragment(root, info, fragment):
        return Person.objects.filter(first_name__icontains=fragment) | Person.objects.filter(second_name__icontains=fragment)

    filter_persons_by_gender = graphene.List(PersonType, gender=graphene.String(required=True))

    def resolve_filter_persons_by_gender(root, info, gender):
        return Person.objects.filter(gender=gender)

    filter_persons_by_position = graphene.List(PersonType, position_id=graphene.Int(required=True))

    def resolve_filter_persons_by_position(root, info, position_id):
        return Person.objects.filter(position_id=position_id)


schema = graphene.Schema(query=Query)
