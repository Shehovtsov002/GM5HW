from rest_framework import serializers

from movie_app.models import Director, Movie, Review


class DirectorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'id name movies_count'.split()


class DirectorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'


class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'id title duration'.split()


class MovieDetailSerializer(serializers.ModelSerializer):
    director = DirectorsSerializer(many=False)

    class Meta:
        model = Movie
        fields = '__all__'


class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id stars'.split()


class ReviewsDetailSerializer(serializers.ModelSerializer):
    movie = MoviesSerializer(many=False)

    class Meta:
        model = Review
        fields = '__all__'


class MoviesReviewsSerializer(serializers.ModelSerializer):
    reviews = ReviewsSerializer(many=True)

    class Meta:
        model = Movie
        fields = 'id title duration rating reviews'.split()
