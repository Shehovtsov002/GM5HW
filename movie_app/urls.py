from django.urls import path
from . import views

urlpatterns = [
    path('directors/', views.directors_list_api_view),
    path('directors/<int:id>/', views.director_api_view),
    path('movies/', views.movies_list_api_view),
    path('movies/<int:id>/', views.movie_api_view),
    path('reviews/<int:movie_id>/', views.reviews_list_api_view),
    path('reviews/<int:movie_id>/<int:id>/', views.review_api_view),
    path('movies/reviews/', views.movies_reviews_api_view),
]