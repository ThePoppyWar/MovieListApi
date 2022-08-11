from django.contrib import admin
from django.urls import path, include
# from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import MovieListView, MovieDetailView

urlpatterns = [
    path('list/', MovieListView.as_view(), name='movie-list'),
    path('list/<int:pk>/', MovieDetailView.as_view(), name='movie-details'),

]
