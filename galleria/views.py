from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt

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