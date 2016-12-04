from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

app_name = 'financeapp'
urlpatterns = [
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            views.reset_confirm, name='password_reset_confirm'),
    url(r'^reset/$', views.reset, name='reset'),
    url(r'^loginredir/$', views.loginredir, name='loginredir'),
    url(r'^student/(?P<student_id>[0-9]+)/$', views.student, name='student'),
    url(r'^student/(?P<student_id>[0-9]+)/check_balance/$', views.checkbalanceview, name='check_balance'),
    url(r'^student/(?P<student_id>[0-9]+)/add_money/$', views.addmoneyview, name='add_money'),
    url(r'^student/(?P<student_id>[0-9]+)/doaddmoney/$', views.doaddmoney, name='doaddmoney'),
    url(r'^parenthome/$', views.parenthome, name='parenthome')
]
