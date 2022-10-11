from rest_framework import serializers
from api.models import Item



class itemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"