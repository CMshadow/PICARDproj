#creating on 1/2/17

#addUserForm and UserProfileForm for registration

from portal.models import Contact
#from portal.models import UserProfile
from django.contrib.auth.models import User
from django import forms
#from django.core.validators import validate_email
from django.core.exceptions import ValidationError
#The followings are added in 7/19/2017
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    email = forms.EmailField(max_length=254, required=True, help_text='Required')

    SEX_CHOICES=(('M','Male'),('F','Female'),('O','Other'))
    sex = forms.ChoiceField(choices=SEX_CHOICES)
    # ssn = forms.CharField(required=True, help_text='Required. Format: 000-00-0000')
    # birthday = forms.DateField(required=True, help_text='Required. Format: YYYY-MM-DD')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'sex', 'password1', 'password2',)


class ContactForm(forms.ModelForm):
	from_email = forms.EmailField(widget = forms.TextInput(attrs = {'class':'form-control','placeholder':'Email'}))
	subject = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Subject'}))
	message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Message'}))
	def clean(self):
		from_email = self.cleaned_data.get('from_email')
		subject = self.cleaned_data.get('subject')
		message = self.cleaned_data.get('message')

	class Meta:
		model = Contact
		fields =('from_email','subject','message')


# class UserForm(forms.ModelForm):
# 	email = forms.CharField(widget = forms.TextInput(attrs = {'class':'form-control','placeholder':'Email'}))
# 	username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
# 	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
# 	repeatpassword = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Repeat Password'}))
#
#
# 	def clean(self):
# 		email = self.clean_email()
# 		username = self.clean_username()
# 		password = self.clean_password()
# 		#repeatpassword = self.cleaned_data.get('repeatpassword')
# 		#repeatpassword = self.cleaned_data['repeatpassword']
# 		return self.cleaned_data
#
# 	def clean_email(self):
# 		email = self.cleaned_data.get('email')
# 		try:
# 			#validate_email('email')
# 			return email
# 		except ValidationError:
# 			raise forms.ValidationError('Please Enter the Correct Email')
#
#
# 	def clean_password(self):
# 		password = self.cleaned_data.get('password')
# 		repeatpassword = self.cleaned_data.get('repeatpassword')
# 		#if not password:
# 		#		raise forms.ValidationError('Please enter a valid password')
# 		#if not repeatpassword:
# 		#		raise forms.ValidationError('You must confirm your password')
#
# 		if (password and repeatpassword and (password != repeatpassword)):
#
# 				raise forms.ValidationError('Passwords do not match')
# 		else:
# 				return self.cleaned_data.get('password')
#
#
# 	def clean_username(self):
# 		username = self.cleaned_data.get('username')
# 		try:
# 			user = User.objects.exclude(pk=self.instance.pk).get(username=username)
# 			#bjects.filter(username).exists():
# 		#return username
# 		except:
# 			return username
# 		raise forms.ValidationError('Username "%s" is already in use.'% username)
# 	class Meta:
# 		model = User
# 		fields = ('username','email','password','repeatpassword')
#
#
#
# class UserProfileForm(forms.ModelForm):
# 	class Meta:
# 		model = UserProfile
# 		fields = ('picture',)
