from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login 
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView

from django.views.generic import View

from django.contrib.auth.forms import AuthenticationForm as LoginForm
from django.contrib import messages

from django.contrib.auth.forms import PasswordResetForm
from django.views.generic.edit import FormView
from django.views.decorators.csrf import csrf_protect

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

from django.contrib.messages.views import SuccessMessageMixin

from django.shortcuts import render, get_object_or_404

from .forms import NewsLetterForm
from .models import Newsletter

from django.core.mail import send_mail

from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from .forms import ContactUsForm
from .models import Contact

import json
import urllib

from .models import Profile,State,Country
from .forms import ProfileForm

########### Print Function ###############

from django.conf import settings
import builtins
from pprint import pprint
def pp(*args):
	if settings.DEBUG:
		for arg in args:
			pprint(arg)
		pass
builtins.pp = pp 

#####################################

def home(request):
	html_message = 'watch/news_letter_email.html'
	if request.method == 'POST':
		news = NewsLetterForm(request.POST)
		if news.is_valid():			
			news.save()
			subject = 'Newsletter'
			html_message = render_to_string('watch/news_letter_email.html', {'context': 'values'})
			plain_message = strip_tags(html_message)
			from_email = 'Mysite <developer4mysite@gmail.com>'
			to = news.cleaned_data['email']
			pp(to)
			mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)
			messages.add_message(request,messages.SUCCESS, 'Submitted Successfully.!')
			return redirect('home')
		else:
			messages.add_message(request,messages.ERROR, "Already updated your email..")
	else:
		news = NewsLetterForm()
	return render(request, 'watch/home.html',{'news':news})

############ SignUp #################

class signup(View):
	def post(self,request):
		form = SignUpForm(request.POST)
		if form.is_valid():			
			user = form.save()
			messages.add_message(request,messages.SUCCESS, 'Registered successfully.!')		
			auth_login(request,user)
			return redirect('home')
		else:
			messages.add_message(request,messages.ERROR, "Registration failed..!!")	
		return render(request, 'user/signup.html', {'form':form})			
	def get(self,request):
		form = SignUpForm()		
		return render(request, 'user/signup.html', {'form':form})	

############ reCAPTCHA Validation ########################

def recaptcha_validate(request):
	recaptcha_response = request.POST.get('g-recaptcha-response')
	url = 'https://www.google.com/recaptcha/api/siteverify'
	values = {
	'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
	'response': recaptcha_response
	}
	data = urllib.parse.urlencode(values).encode()
	req =  urllib.request.Request(url, data=data)
	response = urllib.request.urlopen(req)
	result = json.loads(response.read().decode())
	if result['success']:
		return True
	else:
		return False		

############ LogIn #################

def login(request):
	if request.method == 'POST':
		form = LoginForm(data=request.POST)
		if form.is_valid():
			result = recaptcha_validate(request)
			if result:
				user = form.get_user()
				auth_login(request, user)
				messages.add_message(request,messages.SUCCESS, 'Login Success.!')
				return redirect('home')
			else:
				messages.add_message(request,messages.ERROR, 'Invalid reCAPTCHA. Please try again.')
		else:
			messages.add_message(request,messages.ERROR, 'Invaild Login.!')
	else:
		form = LoginForm()
	return render(request, 'user/login.html', {'form': form})
	
############ Update Account #################

@method_decorator(login_required(login_url='/user/'), name='dispatch')
class UserUpdateView(SuccessMessageMixin,UpdateView):
	model = User
	fields = ('first_name', 'last_name', 'email' )
	template_name = 'user/my_account.html'

	def get_object(self):
		return self.request.user

	def form_valid(self, form):
		fname_user = self.request.user.first_name
		lname_user = self.request.user.last_name
		email_user = self.request.user.email
		fname = form.cleaned_data['first_name']
		lname = form.cleaned_data['last_name']    	
		email = form.cleaned_data['email'] 

		msgs=[]
		if fname_user =='' and lname_user =='' and fname =='' and lname == ''and  email == '' and email_user == '':
			msgs.append('Form..!!')
		elif (fname == '' and fname_user == ''and lname == '' and lname_user ==''): 
			msgs.append('Firstname and Lastname')
		elif (fname == '' and fname_user == '' and email == '' and email_user ==''): 
			msgs.append('Firstname and Email Address')
		elif (fname == '' and fname_user == ''): 
			msgs.append('Firstname')
		elif (lname == '' and lname_user =='' and email == '' and email_user ==''): 
			msgs.append('Lastname and Email Address')
		elif (lname == '' and lname_user ==''): 
			msgs.append('Lastname')
		elif (email == '' and email_user ==''): 
			msgs.append('Email Address')
		else:
			messages.add_message(self.request,messages.SUCCESS,"Saved Your Profile")

		for msg in msgs:
			messages.add_message(self.request,messages.ERROR,"Please Fill "+ msg)
		pp(msgs)	
		form.save()
		return redirect('my_account')

########## check email ##############

def email_present(email):
	if User.objects.filter(email=email).exists():
		return True
	return False

########## password context ######### 

class PasswordContext:
	extra_context = None

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context.update({
			'title': self.title,
			**(self.extra_context or {})
		})
		return context

########### Password Reset ##################        

class PasswordResetView(PasswordContext, FormView):
	template_name = 'user/password_reset.html'
	email_template_name = 'user/password_reset_email.html'
	subject_template_name = 'user/password_reset_subject.txt'
	form_class = PasswordResetForm
	success_url = reverse_lazy('password_reset_done')
	title = ('Password reset')

	@method_decorator(csrf_protect)
	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)
			
	def form_valid(self, form):
		opts = {
			'use_https': self.request.is_secure(),
			'email_template_name': self.email_template_name,
			'subject_template_name': self.subject_template_name,
			'request': self.request,
		}
		form_email = form.cleaned_data['email']
		pp(form_email)
		email_status = email_present(form_email)
		pp(email_status)
		if email_status:
			messages.add_message(opts['request'],messages.INFO,"Please check your email")
			form.save(**opts)
			return super().form_valid(form)        	
		else:
			messages.add_message(opts['request'],messages.ERROR,"Enter Registered Email")
			return redirect('password_reset')

############# Change Password ###############

@login_required(login_url='/user/')
def password_change(request):
	if request.method == 'POST':
		form = PasswordChangeForm(user=request.user, data=request.POST)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			messages.add_message(request,messages.SUCCESS,"Password Changed Successfully")
			return redirect('password_change_done')
		else:
			messages.add_message(request,messages.ERROR,"Please Try Again")
	else:
		form = PasswordChangeForm(user=request.user)

	return render(request, 'user/password_change.html', {'form':form})

################# Error Page ######################

def error_view(request):
	return render(request,'includes/404.html',status=404)

################# Generic page ###################

def generic(request):
	return render(request,'watch/generic.html')	

################ contact us ###################

def contactus(request):
	html_message = 'watch/contact_us_email.html'
	if request.method == 'POST':
		form = ContactUsForm(request.POST)
		if form.is_valid():
			emailid = form.cleaned_data['email']
			email_status = False
			fname = form.cleaned_data['first_name']
			lname = form.cleaned_data['last_name']
			pno = form.cleaned_data['phoneno']
			msg = form.cleaned_data['msg']       
			subject = 'Contact Us'
			if Contact.objects.filter(email=emailid).exists():
				email_status = True
			if email_status:
				messages.add_message(request,messages.ERROR,'Email Address is Already Taken..!!')            
			else:
				html_message = render_to_string('watch/contact_us_email.html', {'first_name' : fname,'last_name' : lname, 'email' : emailid, 'phoneno' : pno, 'msg' : msg, })
				plain_message = strip_tags(html_message)
				from_email = 'Mysite <developer4mysite@gmail.com>'
				to = form.cleaned_data['email']
				mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message) 
				form.save()
				messages.add_message(request,messages.SUCCESS,'Submitted successfully')            
			return redirect('home')
		else:
			messages.add_message(request,messages.ERROR,'Failed..')
	else:
		form = ContactUsForm()
	return render(request, 'watch/contact.html' , {'form':form})  

############## Edit Profile ########################

class UpdateProfile(View):
	def post(self,request):
		form = ProfileForm(request.POST,request.FILES)
		if form.is_valid():			
			form.save()
			messages.add_message(request,messages.SUCCESS, 'Registered successfully.!')		
			# auth_login(request,user)
			return redirect('home')
		else:
			pp("form.errors")
			pp(form.errors)
			messages.add_message(request,messages.ERROR,"failed")	
		return render(request, 'user/update_profile.html', {'form':form})			
	def get(self,request):
		form = ProfileForm()		
		return render(request, 'user/update_profile.html', {'form':form})

def load_states(request):
    country_id = request.GET.get('country')
    states = State.objects.filter(country_id=country_id).order_by('name')
    return render(request, 'includes/states_dropdown.html', {'states': states})