from django.conf.urls import url

from . import views

app_name = 'financeapp'
urlpatterns = [
    url(r'^student/(?P<student_id>[0-9]+)/$', views.student, name='student'),
    url(r'^login/$', views.loginview, name='login'),
    url(r'^logincheck/$', views.logincheck, name='logincheck'),
    url(r'^logout/$', views.logoutview, name='logout'),
    url(r'^student/(?P<student_id>[0-9]+)/check_balance/$', views.checkbalanceview, name='check_balance'),
    url(r'^student/(?P<student_id>[0-9]+)/add_money/$', views.addmoneyview, name='add_money'),
    url(r'^student/(?P<student_id>[0-9]+)/doaddmoney/$', views.doaddmoney, name='doaddmoney'),
    url(r'^parenthome/$', views.parenthome, name='parenthome')
]