from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:month>", views.month, name="month-challenge"),
    path("redirect/<int:month>", views.redirect)
]