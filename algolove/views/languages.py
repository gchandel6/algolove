from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from algolove.models import Language



# View to get all snippets of a particular Langauge

def language_detail(request , slug):
	
	lang = get_object_or_404( Language , slug)
	return DetailView(request,
						query=language.snippet_set.all,
						paginate_by=20,
						template_name='algolove/language_detail.html',
						extra_context={'language' : language }
						)

	
