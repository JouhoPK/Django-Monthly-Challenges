from django.urls import path
from . import views

urlpatterns = [
    path("", views.main, name="index"),
    path("<int:month>", views.views_int),
    path("<str:month>", views.views, name="challenge")
]