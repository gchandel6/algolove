from django.shortcuts import get_object_or_404,render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from algolove.models import Language,Algo_snippet


def algo_snippet_page(request , algo_snippet_id):
	s = get_object_or_404(Algo_snippet , pk=algo_snippet_id)
	return render(request , 'algolove/algo_snippet_detail.html' , {	'snippet' : s 	})