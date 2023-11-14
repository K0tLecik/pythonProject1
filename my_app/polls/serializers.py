from rest_framework import serializers
from .models import Person, Position
from django.utils import timezone


class PersonSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(required=True)
    second_name = serializers.CharField(required=True)
    gender = serializers.ChoiceField(choices=Person.genders)
    position = serializers.PrimaryKeyRelatedField(queryset=Position.objects.all(), required=True)

    def create(self, validated_data):
        return Person.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.second_name = validated_data.get('second_name', instance.second_name)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.position = validated_data.get('position', instance.position)
        instance.save()
        return instance

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