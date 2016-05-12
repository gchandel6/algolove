
from django.conf.urls import url
from . import views
#from django.views.generic.list import ListView 
#from django.views.generic.detail import DetailView

from algolove.models import Snippet



urlpatterns = [

	#   URL for Home Page
	
	url(r'^$' , views.home_page , name='home_page') ,
	

	#	URL for list of all snippets 

    url(r'^tutorials/$' , views.all_codes , name='all_codes') ,
	
]
