from django.shortcuts import render
from .models import Snippet

# Create your views here.


def home_page(request):
	
	return render(request , 'algolove/home_page.html')



def all_codes(request):
	
	codes=Snippet.objects.all()
	
	return render(request , 'algolove/all_codes.html', {'codes':codes  })
