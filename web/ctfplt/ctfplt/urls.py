from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r"^", include("scoreboard.urls")),
    url(r"^problems/", include("problems.urls")),
    url(r"^accounts/", include("accounts.urls")),
    url(r"^scoreboard/", include("scoreboard.urls")),
    url(r"^guides/", include("guides.urls")),
    url(r'^markdownx/', include('markdownx.urls')),
]

