from rameniaapp.models import Noodle, List
from rest_framework import serializers

class NoodleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Noodle
        fields = ['name', 'metadata']

    
