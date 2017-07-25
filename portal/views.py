from django.shortcuts import render, redirect, render_to_response
from portal.forms import ContactForm
#from portal.forms import UserForm,UserProfileForm
from django.template import RequestContext
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect,HttpResponse
#from registration.backends.simple.views import RegistrationView
from django.views.decorators.csrf import csrf_protect,csrf_exempt
from django.core.mail import send_mail, BadHeaderError
#The followings are added in 7/19/2017
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from . import forms

#Create a new class that redirects the user to the index page,if successful at logging
# Create your views here.

def patientsignup(request):
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.sex = form.cleaned_data['sex']
            g = Group.objects.get(name='Patient')
            user.groups.add(g)
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = forms.SignUpForm()
    return render(request, 'portal/signup.html', {'form': form})


def physiciansignup(request):
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.sex = form.cleaned_data['sex']
            g = Group.objects.get(name='Physician')
            user.groups.add(g)
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = forms.SignUpForm()
    return render(request, 'portal/signup.html', {'form': form})


def caregiversignup(request):
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.sex = form.cleaned_data['sex']
            g = Group.objects.get(name='Caregiver')
            user.groups.add(g)
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = forms.SignUpForm()
    return render(request, 'portal/signup.html', {'form': form})


# class SignUp(CreateView):
#     form_class = forms.UserCreateForm
#     success_url = reverse_lazy("login")
#     template_name = "portal/signup.html"


# def SignUp(request):
#     if request.method == 'POST':
#         form = forms.UserCreateForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             user.refresh_from_db()  # load the profile instance created by the signal
#             user.profile.birth_date = form.cleaned_data.get('birth_date')
#             user.save()
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=user.username, password=raw_password)
#             login(request, user)
#             return redirect('home')
#     else:
#         form = forms.UserCreateForm()
#     return render(request, 'portal/signup.html', {'form': form})


#direct to correponded html

def contacts(request):
	return email(request)

def frontpage(request):
	return render(request,'frontpage.html')

#@login_required(login_url = '/signin/')

def indextest(request):
    return render(request,'index.html')

#@login_required(login_url = 'signin/')
def mainpagetest(request):
    return render(request,'dashboard-top-menu.html')

def patientindex(request):
	return render(request,'patient-index.html')


#check the user type
def is_admin(user):
	return user.groups.filter(name = 'admin').exists();

def is_patient(user):
	return user.groups.filter(name = 'Patient').exists()

def is_doctor(user):
	return user.groups.filter(name = 'Doctors').exists()


# #to log out the user
#
# def logout_view(request):
# 	logout(request)
# 	return render(request,'frontpage.html')
#
# #to register as a doctor
# @csrf_exempt
# def register_doctors(request):
# 	context = RequestContext(request)
# 	registered = False
# 	if request.method == 'POST':
# 		user_form = UserForm(data=request.POST)
# 		if user_form.is_valid():
# 			user = user_form.save()
# 			user.groups.add(Group.objects.get(name = 'Doctors'))
# 			user.set_password(user.password)
# 			user.save()
# 			registered = True
# 			return HttpResponseRedirect('/picard/signindoctors/')
# 		else:
# 			print(user_form.errors)
# 	else:
# 		user_form = UserForm()
#
#
#
# 	return render_to_response(
# 			'sign-up-doctors.html',{'user_form':user_form,'registered':registered},context)
#
# #to register as a patient
#
# @csrf_exempt
# def register_patient(request):
#     context = RequestContext(request)
#
#
#     # A boolean value for telling the template whether the registration was successful.
#     # Set to False initially. Code changes value to True when registration succeeds.
#     registered = False
#     # If it's a HTTP POST, we're interested in processing form data.
#     #user_form = UserForm(request.POST or None)
#     if request.method == 'POST':
# 		user_form = UserForm(data=request.POST)
# 	#and user_form.is_valid():
# 	  # Attempt to grab information from the raw form information.
#         # Note that we make use of both UserForm and UserProfileForm.
#
#       #  profile_form = UserProfileForm(data=request.POST)
# 	  	test = "test"
#         # If the two forms are valid...
#         if user_form.is_valid():
# 			# and profile_form.is_valid():
#             # Save the user's form data to the database.
#  	 		#   user_form.process()
# 			#email = user_form.cleaned_data['email']
# 			#username = user_form.cleaned_data['username']
# 			#password = user_form.cleaned_data['password']
# 			#repeatpassword = user_form.clean_data['repeatpassword']
# 			user = user_form.save()
# 			user.groups.add(Group.objects.get(name = 'Patient'))
# 			#test  = "test2"
# 	   		# user = User.objects.create_user(username = user_form.cleaned_data['username'],password = user_form.cleaned_data['password'],email = user_form.cleaned_data['email'])
#             # Now we hash the password with the set_password method.
#             # Once hashed, we can update the user object.
#         	user.set_password(user.password)
#         	user.save()
# 			test = "test3"
# 	    	#user = authenticate(username = user.username,pasword = request.POST['password'])
# 	    	#user_login(request,user)
#             # Now sort out the UserProfile instance.
#             # Since1 we need to set the user attribute ourselves, we set commit=False.
#             # This elays saving the model until we're ready to avoid integrity problems.
#             #profile = profile_form.save(commit=False)
#             #profile.user = user
#
#             # Did the user provide a profile picture?
#             # If so, we need to get it from the input form and put it in the UserProfile model.
#             #if 'picture' in request.FILES:
#                # profile.picture = request.FILES['picture']
#
#             # Now we save the UserProfile model instance.
#             #profile.save()
#
#             # Update our variable to tell the template registration was successful.
# 			registered = True
# 			test = "test4"
# 			return HttpResponseRedirect('/picard/signin/')
#         	# Invalid form or forms - mistakes or something else?
#         	# Print problems to the terminal.
#         	# They'll also be shown to the user.
#     	else:
#         	print user_form.errors
#
#     # Not a HTTP POST, so we render our form using two ModelForm instances.
#     # These forms will be blank, ready for user input.
#     else:
#     	user_form = UserForm()
# 		#profile_form = UserProfileForm()
#     #variables = RequestContext(request,{'user_form',user_form})
#     #return render_to_response('sign-up.html',variables)
#     # Render the template depending on the context.
#     	return render_to_response('sign-up.html',{'user_form': user_form,'registered': registered},context)
#
#
# #to login as a doctor
#
# @csrf_exempt
# def doctors_login(request):
# 	notice  = "";
# 	context = RequestContext(request)
# 	if request.method == 'POST':
# 		username = request.POST['username']
# 		password = request.POST['password']
# 		user = authenticate(username = username, password = password)
# 		if user:
# 			if is_doctor(user) and user.is_active:
# 				login(request,user)
# 				return HttpResponseRedirect('/picard/index/')
# 			else:
# 				notie = "Your Picard Accound is disabled for Doctor login"
# 				return HttpResponse("Your Picard Accound is disabled")
# 				#return render_to_response('sign-in-doctors.html',{'notice',notice},context)
# 				#return HttpResponseRedirect('/loginfail/')
#
# 		else:
# 			print "Invalid login details : {0],{1}".format(username,password)
# 	else:
# 		return render_to_response('sign-in-doctors.html',{'notice',notice},context)
#
# #to login as a patient
#
# @csrf_exempt
# def patient_login(request):
#     # Like before, obtain the context for the user's request.
#     context = RequestContext(request)
#
#     # If the request is a HTTP POST, try to pull out the relevant information.
#     if request.method == 'POST':
#         # Gather the username and password provided by the user.
#         # This information is obtained from the login form.
# 		username = request.POST['username']
# 		password = request.POST['password']
# 		# Use Django's machinery to attempt to see if the username/password
#         # combination is valid - a User object is returned if it is.
#         user = authenticate(username=username, password=password)
#
#         # If we have a User object, the details are correct.
#         # If None (Python's way of representing the absence of a value), no user
#         # with matching credentials was found.
#         if user:
#             # Is the account active? It could have been disabled.
#             if is_patient(user) and user.is_active:
#                 # If the account is valid and active, we can log the user in.
#                 # We'll send the user back to the homepage.
#                 login(request, user)
# 				return HttpResponseRedirect('/picard/patientindex/')
# 	    	else:
# 				return HttpResponse("Your Picard account is disabled")
# 		else:
#             # Bad login details were provided. So we can't log the user in.
#             print "Invalid login details: {0}, {1}".format(username, password)
#             return HttpResponse("Invalid login details supplied.")
# 	# The request is not a HTTP POST, so display the login form.
#     # This scenario would most likely be a HTTP GET.
#     else:
#         # No context variables to pass to the template system, hence the
#         # blank dictionary object...
#         return render_to_response('sign-in.html', context)
#
#
# # to send email on the contact page
#
#
# @csrf_exempt
# def email(request):
#     context = RequestContext(request)
#     if request.method == 'GET':
#         form = ContactForm()
#     else:
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             subject = form.cleaned_data['subject']
#             from_email = form.cleaned_data['from_email']
#             message = form.cleaned_data['message']
#             try:
#                 send_mail(subject, message, from_email, ['picard@gmail.com'])
#             except BadHeaderError:
#                 return HttpResponse('Invalid header found.')
#             return redirect('thanks')
#     return render_to_response("contacts.html", {'form': form},context)
# #to give out message on the contact page after succesfully sending out email
# def thanks(request):
#     return HttpResponse('Thank you for your message.')
