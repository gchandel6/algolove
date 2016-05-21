from django.shortcuts import render , redirect
from django.contrib.auth import authenticate,login,logout
from algolove.forms import SignupForm , LoginForm


# Create your views here.

#	View for Home Page

def home_page(request):
	
	return render(request , 'algolove/home_page.html')


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
					return render(request,'algolove/home_page.html',{ 'user' : user })
	else:
		form=LoginForm()

	return render(request,'algolove/log_in.html',{	'form' : form})


#	View for User Logout

def log_out(request):
	logout(request)
	return redirect('home_page')