from django.contrib import admin
from django.urls import path
from movie_app import views as movie_app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/directors/', movie_app.directors_list_api_view),
    path('api/v1/directors/<int:id>/', movie_app.director_api_view),
    path('api/v1/movies/', movie_app.movies_list_api_view),
    path('api/v1/movies/<int:id>/', movie_app.movie_api_view),
    path('api/v1/reviews/<int:movie_id>/', movie_app.reviews_list_api_view),
    path('api/v1/reviews/<int:movie_id>/<int:id>/', movie_app.review_api_view),
    path('api/v1/movies/reviews/', movie_app.movies_reviews_api_view),
]
