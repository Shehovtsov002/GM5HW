from rest_framework.viewsets import ModelViewSet

from movie_app import models
from movie_app import serializers


class CustomViewSetAPIView(ModelViewSet):
    serializer_list_class = None
    serializer_action_class = None
    serializer_detail_class = None

    def get_serializer_class(self):
        if self.action == 'list' and self.serializer_list_class:
            return self.serializer_list_class
        elif self.action == 'retrieve' and self.serializer_detail_class:
            return self.serializer_detail_class
        elif self.action in ['create', 'update', 'partial_update'] and self.serializer_action_class:
            return self.serializer_action_class
        return super().get_serializer_class()


class DirectorAPIView(CustomViewSetAPIView):
    queryset = models.Director.objects.all()
    serializer_list_class = serializers.DirectorsSerializer
    serializer_detail_class = serializers.DirectorDetailSerializer
    serializer_action_class = serializers.DirectorsValidateSerializer
    lookup_field = 'id'


class MovieAPIView(CustomViewSetAPIView):
    queryset = models.Movie.objects.all()
    serializer_list_class = serializers.MoviesSerializer
    serializer_detail_class = serializers.MovieDetailSerializer
    serializer_action_class = serializers.MovieValidateSerializer
    lookup_field = 'id'


class ReviewAPIView(CustomViewSetAPIView):
    queryset = models.Review.objects.all()
    serializer_list_class = serializers.ReviewsSerializer
    serializer_detail_class = serializers.ReviewsDetailSerializer
    serializer_action_class = serializers.ReviewsValidateSerializer
    lookup_field = 'id'
