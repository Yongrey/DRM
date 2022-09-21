from rest_framework import serializers
from .models import Director, Movie, Review


class DirectorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'id name'.split()


class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'id title description duration'.split()


class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text movie'.split()