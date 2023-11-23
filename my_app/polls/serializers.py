from rest_framework import serializers
from .models import Person, Position
from django.utils import timezone
from django.contrib.auth.models import User


class PersonSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(required=True)
    second_name = serializers.CharField(required=True)
    gender = serializers.ChoiceField(choices=Person.genders)
    position = serializers.PrimaryKeyRelatedField(queryset=Position.objects.all(), required=True)

    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)

    class Meta:
        model = Person
        fields = '__all__'

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['owner'] = user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if instance.owner != self.context['request'].user:
            raise serializers.ValidationError("Nie masz uprawnień do edycji tego obiektu.")
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.second_name = validated_data.get('second_name', instance.second_name)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.position = validated_data.get('position', instance.position)
        instance.save()
        return super().update(instance, validated_data)

    def validate_first_name(self, data):
        if not data.isalpha():
            raise serializers.ValidationError("Pole 'first_name' może zawierać tylko litery.")
        return data



    def validate_second_name(self, data):
        if not data.isalpha():
            raise serializers.ValidationError("Pole 'second_name' może zawierać tylko litery.")
        return data



    def validate_date_added(self, data):
        if data > timezone.now():
            raise serializers.ValidationError("Data dodania nie może być z przyszłości.")
        return data


class PositionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ['name', 'description']