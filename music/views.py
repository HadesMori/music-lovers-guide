from typing import Any
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import View, DetailView, ListView
from .models import *
from .forms import *

class MainView(View):

    def get(self, request):
        latest_songs = Song.objects.all().order_by('-year')[:10]
        return render(request, "music/main.html", context={
            'latest_songs': latest_songs,
        })
    
class BandView(DetailView):
    template_name = "music/band.html"
    model = Band

    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        songs = self.object.songs.all() 
        albums = self.object.albums.all() 
        context['songs'] = songs
        context['albums'] = albums
        return context
    
class AlbumView(DetailView):
    template_name = "music/album.html"
    model = Album

    slug_field = 'slug'
    slug_url_kwarg = 'album_slug'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        songs = self.object.songs.all() 
        context['songs'] = songs
        return context

class AllBandView(ListView):
    template_name = "music/all-bands.html"
    model = Band

    context_object_name = "bands"

class AllArtistView(ListView):
    template_name = "music/all-artists.html"
    model = Artist

    context_object_name = "artists"

class SongsView(ListView):
    template_name = "music/songs.html"
    model = Song

    context_object_name = "songs"

class SongView(DetailView):
    template_name = "music/song.html"
    model = Song

    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    
    def post(self, request, slug):
        song = self.get_object()
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.song = song
            comment.save()
            return HttpResponseRedirect(reverse("song-page", args=[song.slug]))
        else:
            context = {
                "form": comment_form,
                "comments": song.comments.all().order_by('-id'),
            }
            return render(request, "music/song.html", context)
        
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        comments = self.object.comments.all() 
        form = CommentForm()
        context['comments'] = comments
        context['form'] = form
        return context

class AlbumsView(ListView):
    template_name = "music/albums.html"
    model = Album

    context_object_name = "albums"