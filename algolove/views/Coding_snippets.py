from django.shortcuts import get_object_or_404,render,redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from algolove.models import Language,Coding_snippet
from django.contrib.auth.decorators import login_required
from django.forms import ModelForm


def coding_snippet_page(request , coding_snippet_id):
	s = get_object_or_404(Coding_snippet , pk=coding_snippet_id)
	return render(request , 'algolove/coding_snippet_detail.html' , {	'snippet' : s 	})


class Coding_snippetForm(ModelForm):
	class Meta:
		model=Coding_snippet
		exclude=['author']


#	View for adding an Algo_Snippet

def add_coding_snippet(request):
	if request.method=='POST':
		form=Coding_snippetForm(request.POST)
		if form.is_valid():
			new_coding_snippet=form.save(commit=False)
			new_coding_snippet.author=request.user
			new_coding_snippet.save()
			return redirect(new_coding_snippet.get_absolute_url())
	else:
		form=Coding_snippetForm
	return render(request,'algolove/add_coding_snippet.html',{ 'form':form })

#add_algo_snippet=login_required(add_algo_snippet)