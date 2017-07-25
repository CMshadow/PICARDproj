from django.conf.urls import include,url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
# The followings are added in 7/19/2017
# login / logout views in Django 1.11
from django.contrib.auth import views as auth_views

app_name = 'portal'

urlpatterns = [
	url(r'^login/$', auth_views.LoginView.as_view(template_name='portal/login.html'),name='login'),
	url(r'^logout/$', auth_views.LogoutView.as_view(),name='logout'),
	url(r'^patientsignup/$', views.patientsignup,name='patientsignup'),
    url(r'^physiciansignup/$', views.physiciansignup,name='physiciansignup'),
    url(r'^caregiversignup/$', views.caregiversignup,name='caregiversignup'),


	#url(r'^signup/',views.frontpage,name = 'signup'),
	#url(r'^signin/',views.frontpage,name = 'signin'),
	url(r'^admin/',include(admin.site.urls)),
	url(r'^test/',views.mainpagetest, name = 'test'),
	url(r'^signupdoctors/',views.frontpage,name = 'signupdoctors'),
	url(r'^signindoctors/',views.frontpage,name = 'signindoctors'),
	url(r'^frontpage/',views.frontpage,name = 'frontpage'),
	url(r'^indextest/',views.indextest,name = 'indextest'),
	url(r'^patientindex/',views.patientindex,name='patientindex'),
	url(r'^contacts/',views.contacts,name='contacts'),
]
