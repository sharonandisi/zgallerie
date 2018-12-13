from django.shortcuts import render,redirect
from django.http import HttpResponse
import datetime as dt
from django.http import HttpResponse,Http404
from .models import Photo

# Create your views here.

def archived_photos(request,past_date):
    try:
    #converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
    except ValueError:
        # Raise 404 error when ValueError is thrown raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(photos_today)
    
    news = Photo.days_photos(date)
    return render(request, 'all-photos/archived-photos.html', {"date": date, "news":news})

def photos_today(request):
    date = dt.date.today()
    photos = Photo.todays_photos()
    return render(request, 'all-photos/recent-photos.html',{"date":date,"photos":photos})

def search_results(request):

    if 'photo' in request.GET and request.GET["photo"]:
        search_term = request.GET.get("photo")
        searched_photos = Photo.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-photos/search.html',{"message":message,"photos": searched_photos})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-photos/search.html',{"message":message})

def photo(request,photo_id):
    try:
        photo = Photo.objects.get(id = photo_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-photos/photo.html", {"photo":photo})