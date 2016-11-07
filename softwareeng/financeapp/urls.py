from django.conf.urls import url

from . import views

app_name = 'financeapp'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.loginview, name='login'),
    url(r'^logincheck/$', views.logincheck, name='logincheck'),
    url(r'^logout/$', views.logoutview, name='logout')
]