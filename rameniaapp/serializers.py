from rameniaapp.models import Noodle, List
from rest_framework import serializers

class NoodleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Noodle
        fields = ['id', 'name', 'metadata']

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = ['id', 'name', 'user']
