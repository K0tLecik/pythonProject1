>>> from polls.models import Person, Position
>>> from polls.serializers import PersonSerializer, PositionModelSerializer
>>> from rest_framework.renderers import JSONRenderer
>>> from rest_framework.parsers import JSONParser  
>>> person = Person(first_name='Adam', second_name='Nowak', gender='M', position=Position.objects.first())
>>> person.save()
>>> person_serializer = PersonSerializer(person)
>>> person_serializer.data
{'id': 7, 'first_name': 'Adam', 'second_name': 'Nowak', 'gender': 'M', 'position': 1}
>>> content = JSONRenderer().render(person_serializer.data)
>>> content
b'{"id":7,"first_name":"Adam","second_name":"Nowak","gender":"M","position":1}'
>>> import io
>>> stream = io.BytesIO(content)
>>> data = JSONParser().parse(stream)
>>> deserializer = PersonSerializer(data=data)
>>> deserializer.is_valid()
True
>>> deserializer.validated_data
OrderedDict([('first_name', 'Adam'), ('second_name', 'Nowak'), ('gender', 'M'), ('position', <Position: Nauczyciel>)])
>>> deserializer.save()
<Person: Adam Nowak>
>>> deserializer.data
{'id': 8, 'first_name': 'Adam', 'second_name': 'Nowak', 'gender': 'M', 'position': 1}
>>> exit()
