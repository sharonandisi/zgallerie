from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt
from django.http import HttpResponse,Http404

# Create your views here.
def welcome(request):
    return HttpResponse('Welcome')

def photos_of_the_day(request):
    date = dt.date.today()
    html = f'''
        <html>
            <body>
                <h1> photos for {day} {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)
def convert_dates(dates):

    #Function that gets the weekday number for the date.

    day_number = dt.date.weekday(dates)
    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

    #Returning the actual day of the week
    days = days[day_number]
    return day

def archived_photos(request,past_date):
    try:
    #converts data from the string Url
    date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
    except ValueError:
        # Raise 404 error when ValueError is thrown raise Http404()
    day = convert_dates(date)
    html = f'''
    <html>
        <body>
            <h1>News for {day} {date.day}-{date.month}-{date.year}</h1>
        </body>
    </html>
            '''
    return HttpResponse(html)
