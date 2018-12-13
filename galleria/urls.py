from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    url(r'^$',views.photos_today,name='photosToday'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.archived_photos,name='archivePhotos'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^photo/(\d+)',views.photo,name ='photo')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)