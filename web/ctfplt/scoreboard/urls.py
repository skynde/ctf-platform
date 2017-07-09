from django.conf.urls import include, url
from . import views

app_name = "scoreboard"
urlpatterns = [
    url(r"^$", views.statistics, name="index"),
    url(r"^graphData/$", views.graphData, name="graphData"),
    url(r"^allUsers/$", views.allUsers, name="allUsers"),
]

