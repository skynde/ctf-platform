from django.conf.urls import include, url
from . import views

app_name = "problems"
urlpatterns = [
    url(r"^$", views.index, name="index"),
    url(r"^(?P<problemTitle>[\w\s]+)/$", views.detail, name="detail"),
    url(r"^(?P<problemTitle>[\w\s]+)/unlockhint/$", views.unlockHint, name="unlockHint"),
    url(r"^(?P<problemTitle>[\w\s]+)/submit/$", views.submit, name="submit"),
]

