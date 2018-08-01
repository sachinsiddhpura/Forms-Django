from django.conf.urls import url, include
from django.contrib import admin
from .views import (
	person, 
	person_detail,
	person_list,
	person_update,
	person_delete,
	person_about,
	login_v,
	logout_v,
	register,
	gmail,
	comman,
	)
urlpatterns = [
	#url(r'^$', index,name='food'),
	url(r'^$', person_list,name='list'),
    url(r'^create/$', person,name='create'),
    url(r'^login/$', login_v,name='login'),
    url(r'^gmail/$', gmail,name='gmail'),
    url(r'^comman/$', comman,name='comman'),
    url(r'^register/$', register,name='signup'),
    url(r'^logout/$', logout_v,name='logout'),
    url(r'^about/$', person_about,name='about'),
    url(r'^(?P<id>\d+)/$', person_detail,name='detail'),
    url(r'^(?P<id>\d+)/edit/$', person_update,name='update'),
    url(r'^(?P<id>\d+)/delete/$', person_delete,name='delete'),
]