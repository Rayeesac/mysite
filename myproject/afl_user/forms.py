from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Newsletter,Contact,Profile
from django.forms import ModelForm

class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class NewsLetterForm(forms.ModelForm):
	class Meta:
		model = Newsletter
		fields = ('email',)

class ContactUsForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = ('first_name','last_name','email','phoneno','msg')

class DateInput(forms.DateInput):
	input_type = 'date'

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('user','img', 'address','country','state','pin','DOB')
		widgets = { 'DOB': DateInput(),}

class UpdateProfileForm(ProfileForm):
	first_name = forms.CharField(max_length=User._meta.get_field('first_name').max_length)
	last_name = forms.CharField(max_length=User._meta.get_field('last_name').max_length)
	email = forms.CharField(max_length=User._meta.get_field('email').max_length)

	class Meta(ProfileForm.Meta):
		fields = ProfileForm.Meta.fields+ ('first_name','last_name','email')