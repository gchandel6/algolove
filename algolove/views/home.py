from django.shortcuts import render , redirect
from django.contrib.auth import authenticate,login,logout
from algolove.forms import SignupForm , LoginForm
from django.contrib.auth.models import User
from algolove.models import Algo_snippet,Coding_snippet
from django.utils import timezone


# Create your views here.

#	View for Home Page

def home_page(request):
	arr = Algo_snippet.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')
	return render(request , 'algolove/home_page.html' ,{'arr':arr } )


#	View for User Signup

def sign_up(request):
	if request.method == 'POST':
		form=SignupForm(request.POST)
		if form.is_valid():
			new_user=form.save()
			return redirect('log_in')

	else:
		form=SignupForm()

	return render(request,'algolove/sign_up.html',{	'form' : form })


#	View for User Login

def log_in(request):
	if request.method=='POST':
		form=LoginForm(request.POST)
		if form.is_valid():
			username=request.POST['username']
			password=request.POST['password']
			user=authenticate(username=username,password=password)
			if user is not None:
				if user.is_active:
					login(request,user)
					return redirect('home_page')
	else:
		form=LoginForm()

	return render(request,'algolove/log_in.html',{	'form' : form})


#	View for User Logout

def log_out(request):
	logout(request)
	return redirect('home_page')


#	View for User profile page

def profile_page(request,username):
	user=User.objects.get(username=username)
	return render(request,'algolove/user.html',{'user':user } )