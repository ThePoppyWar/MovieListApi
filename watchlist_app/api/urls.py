from django.contrib import admin
from django.urls import path, include
# from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import WatchListView, WatchDetailView, StreamPlatformView, StreamPlatformDetailView

urlpatterns = [
    path('list/',WatchListView.as_view(), name='movie-list'),
    path('list/<int:pk>/', WatchDetailView.as_view(), name='movie-details'),

    path('stream/', StreamPlatformView.as_view(), name = 'stream-list'),
    path('stream/<int:pk>', StreamPlatformDetailView.as_view(), name = 'streamplatform-detail'),

]
