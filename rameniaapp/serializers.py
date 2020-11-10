from rameniaapp.models import Noodle, List, Tag, NoodleImage, Review
from rest_framework import serializers

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class NoodleImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoodleImage
        fields = ['image', 'main']
        

class NoodleSerializer(serializers.HyperlinkedModelSerializer):
    tags = TagSerializer(many=True, required=False)
    images = NoodleImageSerializer(source='noodleimage_set', many=True, required=False)

    class Meta:
        model = Noodle
        fields = ['id', 'name', 'metadata', 'tags', 'images']

class ReviewSerializer(serializers.ModelSerializer):
    noodle = NoodleSerializer(required=True)

    class Meta:
        model = Review
        fields = ['title', 'reviewer', 'noodle', 'rating', 'body']

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = ['id', 'name', 'user']
