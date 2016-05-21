from django.shortcuts import get_object_or_404,render,redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from algolove.models import Language,Algo_snippet
from django.contrib.auth.decorators import login_required
from django.forms import ModelForm

#	View for a snippet details page

def algo_snippet_page(request , algo_snippet_id):
	s = get_object_or_404(Algo_snippet , pk=algo_snippet_id)
	return render(request , 'algolove/algo_snippet_detail.html' , {	'snippet' : s 	})


class Algo_snippetForm(ModelForm):
	class Meta:
		model=Algo_snippet
		exclude=['author']


#	View for adding an Algo_Snippet

def add_algo_snippet(request):
	if request.method=='POST':
		form=Algo_snippetForm(request.POST)
		if form.is_valid():
			new_algo_snippet=form.save(commit=False)
			new_algo_snippet.author=request.user
			new_algo_snippet.save()
			return redirect(new_algo_snippet.get_absolute_url())
	else:
		form=Algo_snippetForm
	return render(request,'algolove/add_algo_snippet.html',{ 'form':form })

#add_algo_snippet=login_required(add_algo_snippet)