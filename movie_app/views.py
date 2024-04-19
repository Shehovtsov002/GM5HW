from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from movie_app import models
from movie_app import serializers


@api_view(['GET'])
def directors_list_api_view(request):
    directors = models.Director.objects.all()
    directors_ = serializers.DirectorsSerializer(directors, many=True).data
    return Response(data=directors_)


@api_view(['GET'])
def director_api_view(request, id):
    try:
        director = models.Director.objects.get(id=id)
    except models.Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    director_ = serializers.DirectorsSerializer(director).data
    return Response(data=director_)


@api_view(['GET'])
def movies_list_api_view(request):
    movies = models.Movie.objects.all()
    movies_ = serializers.MoviesSerializer(movies, many=True).data
    return Response(data=movies_)


@api_view(['GET'])
def movie_api_view(request, id):
    try:
        movie = models.Movie.objects.get(id=id)
    except models.Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    movie_ = serializers.MovieDetailSerializer(movie).data
    return Response(data=movie_)


@api_view(['GET'])
def reviews_list_api_view(request, movie_id):
    try:
        movie = models.Movie.objects.get(id=movie_id)
        reviews = models.Review.objects.filter(movie=movie)
    except models.Review.DoesNotExist:
        reviews = []

    reviews_ = serializers.ReviewsSerializer(reviews, many=True).data
    return Response(data=reviews_)


@api_view(['GET'])
def review_api_view(request, movie_id, id):
    try:
        review = models.Review.objects.get(id=id)
    except models.Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    review_ = serializers.ReviewsDetailSerializer(review).data
    return Response(data=review_)
