from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DirectorListSerializer, MovieListSerializer, ReviewListSerializer
from .models import Movie, Director, Review
from rest_framework import status


@api_view(['GET'])
def movie_view(request):
    movies = Movie.objects.all()
    data = MovieListSerializer(movies, many=True).data
    return Response(data=data)


@api_view(['GET'])
def director_view(request):
    directors = Director.objects.all()

    data = DirectorListSerializer(directors, many=True).data
    return Response(data=data)


@api_view(['GET'])
def review_view(request):
    reviews = Review.objects.all()
    data = ReviewListSerializer(reviews, many=True).data
    return Response(data=data)


@api_view(['GET'])
def movie_reviews_view(request):

    reviews = Review.objects.all()

    data = ReviewListSerializer(reviews, many=True).data
    return Response(data=data)



@api_view(['GET'])
def movie_item_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'error':'movie not found'})
    serializer = MovieListSerializer(movie)
    return Response(data=serializer.data)


@api_view(['GET'])
def director_item_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'error':'director not found'})
    serializer = DirectorListSerializer(director)
    return Response(data=serializer.data)


@api_view(['GET'])
def review_item_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'error':'Product not found'})
    serializer = ReviewListSerializer(review)
    return Response(data=serializer.data)

