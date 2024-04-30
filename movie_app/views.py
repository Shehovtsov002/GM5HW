from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from movie_app import models
from movie_app import serializers


@api_view(['GET', 'POST'])
def directors_list_api_view(request):
    if request.method == 'GET':
        directors = models.Director.objects.all()
        directors_ = serializers.DirectorsSerializer(directors, many=True).data
        return Response(data=directors_)
    elif request.method == 'POST':
        serializer = serializers.DirectorsValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        name = serializer.validated_data.get('name')
        director = models.Director.objects.create(name=name)
        return Response(data={'director_id': director.id}, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def director_api_view(request, id):
    try:
        director = models.Director.objects.get(id=id)
    except models.Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        director_ = serializers.DirectorsSerializer(director).data
        return Response(data=director_)
    elif request.method == 'PUT':
        serializer = serializers.DirectorsValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        director.name = serializer.validated_data.get('name')
        director.save()
        return Response(data=serializers.DirectorsSerializer(director).data, status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def movies_list_api_view(request):
    if request.method == 'GET':
        movies = models.Movie.objects.all()
        movies_ = serializers.MoviesSerializer(movies, many=True).data
        return Response(data=movies_)
    elif request.method == 'POST':
        serializer = serializers.MovieValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        title = serializer.validated_data.get('title')
        description = serializer.validated_data.get('description')
        duration = serializer.validated_data.get('duration')
        director_id = serializer.validated_data.get('director_id')
        movie = models.Movie.objects.create(title=title,
                                            description=description,
                                            duration=duration,
                                            director_id=director_id)
        return Response(data={'movie_id': movie.id}, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_api_view(request, id):
    try:
        movie = models.Movie.objects.get(id=id)
    except models.Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        movie_ = serializers.MovieDetailSerializer(movie).data
        return Response(data=movie_)
    elif request.method == 'PUT':
        serializer = serializers.MovieValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        movie.title = serializer.validated_data.get('title')
        movie.description = serializer.validated_data.get('description')
        movie.duration = serializer.validated_data.get('duration')
        movie.director_id = serializer.validated_data.get('director_id')
        movie.save()
        return Response(data=serializers.MovieDetailSerializer(movie).data, status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def reviews_list_api_view(request, movie_id):
    if request.method == 'GET':
        try:
            movie = models.Movie.objects.get(id=movie_id)
            reviews = models.Review.objects.filter(movie=movie)
        except models.Review.DoesNotExist:
            reviews = []

        reviews_ = serializers.ReviewsSerializer(reviews, many=True).data
        return Response(data=reviews_)
    elif request.method == 'POST':
        serializer = serializers.ReviewsValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        text = serializer.validated_data.get('text')
        movie_id = serializer.validated_data.get('movie_id')
        stars = serializer.validated_data.get('stars')
        review = models.Review.objects.create(movie=movie_id, text=text, stars=stars)
        return Response(data={'review_id': review.id}, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def review_api_view(request, movie_id, id):
    try:
        review = models.Review.objects.get(id=id)
    except models.Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        review_ = serializers.ReviewsDetailSerializer(review).data
        return Response(data=review_)
    elif request.method == 'PUT':
        serializer = serializers.ReviewsValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        review.text = serializer.validated_data.get('text')
        review.stars = serializer.validated_data.get('stars')
        review.save()
        return Response(data=serializers.ReviewsDetailSerializer(review).data, status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def movies_reviews_api_view(request):
    movies = models.Movie.objects.all()
    movies_ = serializers.MoviesReviewsSerializer(movies, many=True).data
    return Response(data=movies_)
