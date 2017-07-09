from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from . import views, form

app_name = "accounts"
urlpatterns = [
    url(r'^$', views.profile, name="index"),
    url(r'^profile/$', views.profile, name="profile"),
    url(r'^update/$', views.update, name="update"),
    url(r'^login/$', auth_views.login, {'template_name': 'accounts/login.html', 'authentication_form': form.LoginForm}, name="login"), 
    url(r'^logout/$', auth_views.logout, {'next_page': '/accounts/login'}, name="logout"),  
    #url(r'^admin/addusers/$', auth_views.logout, {'next_page': '/accounts/login'}, name="logout"),  
]

