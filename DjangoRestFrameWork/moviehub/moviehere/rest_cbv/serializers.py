from rest_framework import serializers
from moviehere.models import Movies


class MoviesSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=248)
    description = serializers.CharField(required=True, max_length=495)

    def create(self, validated_data):
        """
        Create and return a new `Movies` instance, given the validated data.
        """
        return Movies.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Movies` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance