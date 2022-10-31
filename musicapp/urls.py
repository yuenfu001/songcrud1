from django.urls import path
# from musicapp import views
from . import views

urlpatterns = [
    path('artist', views.artist_list),
    path('artist/<str:pk>', views.uniqueArtist),
    path('song', views.song_list),
    path('song/<str:pk>', views.uniqueSong),
    path('lyrics', views.lyrics_list),
    path('lyrics/<str:pk>', views.uniqueLyrics),
]