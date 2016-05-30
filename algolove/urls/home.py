
from django.conf.urls import url
from algolove.views import home
#from django.views.generic.list import ListView 
#from django.views.generic.detail import DetailView




urlpatterns = [

	#   URL for Home Page
	
	url(r'^$' , home.home_page , name='home_page') ,

	#	URL for user signup's

	url(r'^users/new/$',home.sign_up,name="sign_up"),
	
	#	URL for user Login

	url(r'^accounts/login/$',home.log_in,name="log_in"),

	#	URL for user Logout

	url(r'^logout/$',home.log_out,name="log_out"),

	#	URL for user profile page

	url(r'^users/(?P<username>\w+)/$', home.profile_page , name="profile_page")
]
