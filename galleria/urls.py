from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.welcome,name='welcome'),
    url('^today/$',views.photos_of_the_day,name='photosToday')
    url(r'^archives/(\d{4}-\d{2})/$',views.archived_photos,name='archivePhotos')
]