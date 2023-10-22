from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("getevents/", views.get_events, name="events"),
    path("createdemodata/", views.create_demo_data, name="create_demo_data"),
]