import threading
from datetime import datetime

from django.db.models import F
from django.http import JsonResponse

from django.shortcuts import render

from .models import Event

from .utils import get_new_event


def index(request):
    return render(request, "schedule/index.html")


def get_events(request):
    events = Event.objects.annotate(title=F("name"), start=F("start_time"), end=F("end_time")).values("title", "start", "end")
    return JsonResponse(list(events), safe=False)


def create_demo_data(request):
    Event.objects.create(name="Event 1", start_time=datetime(2023, 10, 21, 19, 0, 0), end_time=datetime(2023, 10, 21, 20, 0, 0))
    Event.objects.create(name="Event 2", start_time=datetime(2023, 10, 22, 8, 0, 0), end_time=datetime(2023, 10, 22, 10, 0, 0))
    return JsonResponse({"success": True})


def post_prompt(request):
    if request.method == "POST":
        prompt = request.POST.get("prompt", "")
        threading.Thread(target=get_new_event, args=(prompt,)).start()
        return JsonResponse({"success": True, "prompt": prompt})
    else:
        return JsonResponse({"success": False, "detail": "Invalid request method"})
