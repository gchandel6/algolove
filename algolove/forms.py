from django import forms
from django.contrib.auth.models import User


#	A Form for User Signups

class SignupForm(forms.Form):
	username=forms.CharField(max_length=20
							,widget=forms.TextInput(attrs={'placeholder': 'Username'}))
	email=forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
	password1=forms.CharField(max_length=20
							  ,widget=forms.PasswordInput(attrs={'placeholder': 'Password1'}))
	password2=forms.CharField(max_length=20
							  ,widget=forms.PasswordInput(attrs={'placeholder': 'Password2'}))	

	def clean_username(self):
		try:
			User.objects.get(username=self.cleaned_data['username'])
		except User.DoesNotExist:
			return self.cleaned_data['username']
		raise forms.ValidationError("Username not available : Try Again")

	def clean(self):
		if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
			if self.cleaned_data['password1'] != self.cleaned_data['password2']:
				raise forms.ValidationError("Passwords do not match : Try Again")


	def save(self):
		new_user=User.objects.create_user(username=self.cleaned_data['username'],
										email=self.cleaned_data['email'],
										password=self.cleaned_data['password1'])
		return new_user
		


#	A Form for User Login

class LoginForm(forms.Form):
	username=forms.CharField(max_length=20
							,widget=forms.TextInput(attrs={'placeholder': 'Username'}))
	password=forms.CharField(max_length=25
								,widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))