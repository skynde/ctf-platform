from django.conf.urls import include, url
from . import views

app_name = "guides"
urlpatterns = [
    url(r"^$", views.index, name="index"),
    url(r"^(?P<articleTitle>[\w\s]+)/$", views.detail, name="detail"),
]

