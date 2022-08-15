from django.contrib import admin
from django.urls import path, include
# from watchlist_app.api.views import movie_list, movie_details
from rest_framework.routers import DefaultRouter
from watchlist_app.api.views import ReviewCreate, ReviewDetailView, StreamPlatformSet, WatchListView, WatchDetailView, StreamPlatformView, StreamPlatformDetailView, ReviewList


router = DefaultRouter()
router.register(r'stream', StreamPlatformSet, basename = 'streamplaform')


urlpatterns = [
    path('list/',WatchListView.as_view(), name='movie-list'),
    path('<int:pk>/', WatchDetailView.as_view(), name='movie-details'),

    path(r'', include(router.urls)),

    # path('stream/', StreamPlatformView.as_view(), name = 'stream-list'),
    # path('stream/<int:pk>', StreamPlatformDetailView.as_view(), name = 'streamplatform-detail'),

    # path('review/', ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>', ReviewDetailView.as_view(), name='review-detail'),

    path('<int:pk>/review-create', ReviewCreate.as_view(), name='review-create'),

    path('<int:pk>/reviews', ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>', ReviewDetailView.as_view(), name='review-detail'),

]


