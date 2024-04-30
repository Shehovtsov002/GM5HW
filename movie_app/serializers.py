from rest_framework import serializers
from rest_framework.exceptions import ValidationError
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


class DirectorsValidateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, min_length=2)


class MovieValidateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100, min_length=2)
    description = serializers.CharField(required=False, allow_blank=True)
    duration = serializers.FloatField()
    director_id = serializers.IntegerField(min_value=1)

    def validate_director_id(self, director_id):
        try:
            Director.objects.get(id=director_id)
        except Director.DoesNotExist:
            raise ValidationError('Director does not exist')
        return director_id


class ReviewsValidateSerializer(serializers.Serializer):
    text = serializers.CharField()
    movie_id = serializers.IntegerField(required=False)
    stars = serializers.IntegerField(min_value=1, max_value=5)

    def validate_movie_id(self, movie_id):
        try:
            Movie.objects.get(id=movie_id)
        except Movie.DoesNotExist:
            raise ValidationError('Movie does not exist')
        return movie_id
