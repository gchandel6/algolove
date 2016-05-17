from django.shortcuts import get_object_or_404,render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from algolove.models import Language,Coding_snippet


def coding_snippet_page(request , coding_snippet_id):
	s = get_object_or_404(Coding_snippet , pk=coding_snippet_id)
	return render(request , 'algolove/coding_snippet_detail.html' , {	'snippet' : s 	})