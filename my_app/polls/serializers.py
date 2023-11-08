from rest_framework import serializers
from .models import Person, Position


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


class PositionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ['name', 'description']