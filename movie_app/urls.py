from django.urls import path
from . import views

urlpatterns = [
    path('directors/', views.DirectorAPIView.as_view({'get': 'list', 'post': 'create'})),
    path('directors/<int:id>/', views.DirectorAPIView.as_view({'get': 'retrieve',
                                                               'put': 'update',
                                                               'delete': 'destroy'})),
    path('movies/', views.MovieAPIView.as_view({'get': 'list', 'post': 'create'})),
    path('movies/<int:id>/', views.MovieAPIView.as_view({'get': 'retrieve',
                                                         'put': 'update',
                                                         'delete': 'destroy'})),
    path('reviews/', views.ReviewAPIView.as_view({'get': 'list', 'post': 'create'})),
    path('reviews/<int:id>/', views.ReviewAPIView.as_view({'get': 'retrieve',
                                                           'put': 'update',
                                                           'delete': 'destroy'})),
]
