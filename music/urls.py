from django.urls import path
from .views import *

urlpatterns = [
    path("", MainView.as_view(), name="home-page"),
    path("bands/", AllBandView.as_view(), name="bands-page"),
    path("artists/", AllArtistView.as_view(), name="artists-page"),
    path("songs/", SongsView.as_view(), name="songs-page"),
    path("albums/", AlbumsView.as_view(), name="albums-page"),
    path("<slug:slug>", BandView.as_view(), name="band-page"),
    path("albums/<slug:album_slug>", AlbumView.as_view(), name="album-page"),
    path("songs/<slug:slug>", SongView.as_view(), name="song-page"),
]
