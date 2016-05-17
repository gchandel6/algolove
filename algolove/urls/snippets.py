

from django.conf.urls import url
from algolove.views import Algo_snippets,Coding_snippets
from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView
from django.shortcuts import render , get_object_or_404

from algolove.models import Algo_snippet,Coding_snippet


query1 = Algo_snippet.objects.all()
query2 = Coding_snippet.objects.all()

urlpatterns = [

	# URL for list of all views -- (Generic View)

	url(r'^$',
			ListView.as_view(queryset=query1,
							 	paginate_by=20,
							 	),
							name="algo_codes_list"
			),

	url(r'^$',
			ListView.as_view(queryset=query2,
							 	paginate_by=20,
							 	),
							name="compete_codes_list"
			),

	url(r'^(?P<snippet_id>\d+)/$' ,
			Algo_snippets.algo_snippet_page,
							name="code_detail"
		),	
	
]
