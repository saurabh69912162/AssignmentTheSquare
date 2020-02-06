from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

from .views import *
urlpatterns = [
    path('', index),
    path('movie_name/<int:movie_id>/', details, name="details"),
    path('add-new-movie', new_movie, name='new_movie'),
    path('edit-movie/<int:id>/', edit_new_movie, name='edit-movie'),
    path('search', search, name='search'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)