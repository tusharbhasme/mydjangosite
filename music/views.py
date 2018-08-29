from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.template import loader

from music.models import Album, Song


# def index(req):
#     all_albums = Album.objects.all()
#     template = loader.get_template('music/index.html')
#     context = {
#         'all_albums': all_albums
#     }
#     return HttpResponse(template.render(context, req))

def index(req):
    all_albums = Album.objects.all()
    return render(req, 'music/index.html', {'all_albums': all_albums})


# def detail(req, album_id):
#     try:
#         album = Album.objects.get(id=album_id)
#     except Album.DoesNotExist:
#         raise Http404("Album does not exist")
#     return render(req, 'music/detail.html', {'album': album})

def detail(req, album_id):
    album = get_object_or_404(Album, id=album_id)
    return render(req, 'music/detail.html', {'album': album})


def favorite(req, album_id):
    album = get_object_or_404(Album, id=album_id)
    try:
        selected_song = album.song_set.get(id=req.POST['song'])
    except (KeyError, Song.DoesNotExist):
        return render(req, 'music/detail.html', {
            'album': album,
            'error_message': "Not a valid song"
        })
    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(req, 'music/detail.html', {'album': album})
