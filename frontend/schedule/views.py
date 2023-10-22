from django.db.models import F
from django.http import JsonResponse

from django.shortcuts import render

from .models import Event


def index(request):
    return render(request, "schedule/index.html")


def getEvents(request):
    events = Event.objects.annotate(title=F("name"), start=F("start_time"), end=F("end_time")).values("title", "start", "end")
    return JsonResponse(list(events), safe=False)
