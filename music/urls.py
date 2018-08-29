from django.urls import path
from . import views

app_name = 'music'
urlpatterns = [
    # /music/
    path('', views.index, name='index'),
    #/music/:id/
    path('<album_id>/', views.detail, name='detail'),
    #/music/:id/favorite
    path('<album_id>/favorite', views.favorite, name='favorite'),
]
