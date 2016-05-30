from django.shortcuts import get_object_or_404,render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from algolove.models import Language,Algo_snippet



# View to get all snippets of a particular Langauge

def language_detail(request , slug):
	
	language = get_object_or_404( Language , slug=slug)
	snippets = Algo_snippet.objects.filter(language=language)
	return render(request,'algolove/language_detail.html'
					,{'codes':snippets , 'language':language })

	
