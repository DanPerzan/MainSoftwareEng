from django.conf.urls import url

from . import views

app_name = 'financeapp'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logincheck/$', views.logincheck, name='logincheck')
]