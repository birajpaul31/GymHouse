from django.conf.urls import url

from . import views

app_name = 'online' #This enables namespacing (eg. using links in templates <a href="{% url mainpage:index'%}")
urlpatterns = [
    url(r'^$', views.online_view, name='online_view'),
]