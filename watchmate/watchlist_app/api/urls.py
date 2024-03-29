from django.urls import path, include
# from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import WatchDetailAV, WatchListAV, StreamPlatformAV, StreamPlatformDetailAV

urlpatterns = [
    path('movies/', WatchListAV.as_view(), name='movie-list'),
    path('movies/<int:pk>', WatchDetailAV.as_view(), name='movie-details'),
    path('stream/', StreamPlatformAV.as_view(), name='stream-list'),
    path('stream/<int:pk>', StreamPlatformDetailAV.as_view(),
         name='streamplatform-detail'),
]
