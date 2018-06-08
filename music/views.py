from django.http import HttpResponse
from boto.connection import HTTPResponse
from .models import Album
def index(request):
    all_albums = Album.objects.all()
    html = ''
    for album in all_albums:
        url = '/music/' + str(album.id) + '/'
        html += '<a href = "' + url + '">' + album.album_title + '</a><br>'
    
    return HttpResponse(html)

def detail(request, album_id):
    return HttpResponse("<h2> details of album_id "+str(album_id)+ " </h2>") 