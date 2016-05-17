
from django.conf.urls import url
from algolove.views import home
#from django.views.generic.list import ListView 
#from django.views.generic.detail import DetailView




urlpatterns = [

	#   URL for Home Page
	
	url(r'^$' , home.home_page , name='home_page') ,
	
	
]
