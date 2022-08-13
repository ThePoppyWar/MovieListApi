from django.contrib import admin
from django.urls import path, include
# from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import ReviewCreate, ReviewDetailView, WatchListView, WatchDetailView, StreamPlatformView, StreamPlatformDetailView, ReviewList

urlpatterns = [
    path('list/',WatchListView.as_view(), name='movie-list'),
    path('list/<int:pk>/', WatchDetailView.as_view(), name='movie-details'),

    path('stream/', StreamPlatformView.as_view(), name = 'stream-list'),
    path('stream/<int:pk>', StreamPlatformDetailView.as_view(), name = 'streamplatform-detail'),

    # path('review/', ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>', ReviewDetailView.as_view(), name='review-detail'),

    path('stream/<int:pk>/review-create', ReviewCreate.as_view(), name='review-create'),

    path('stream/<int:pk>/review', ReviewList.as_view(), name='review-list'),
    path('stream/review/<int:pk>', ReviewDetailView.as_view(), name='review-detail'),

]
