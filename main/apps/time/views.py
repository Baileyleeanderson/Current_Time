from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from datetime import datetime


def showtime(request):
  realtime = {
  "time": strftime("%B %d, %Y", gmtime()),
  "hour": strftime("%H:%M %p", gmtime())
   }
    
  return render(request,'time/index.html', context=realtime)




