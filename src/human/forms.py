from .models import Person,PersonType
from django.forms import ModelForm
from django import forms
from django.contrib.auth import(
	authenticate,
	get_user_model,
	login,
	logout,
	)

from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

#from .models import Profile, Choice
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)



CHOICES=[
	(1,'India'),
	(2,'US'),
	(3,'UK'),
]
User=get_user_model()
'''
QUESTION_CHOICES = (
    ("vada_paw", "Vada Paw"),
    ("paw_bhaji", "Paw Bhaji"),
    ("ghughra", "Ghughra"),
    ("pani_puri", "Pani Puri"),
    ("dal_pakwan", "Dal Pakwan"),
    ("fruit_salad", "Fruit Salad"),
    ("sandwhich", "Sandwhich"),
    ("bhajiya", "Bhajiya"),
    ("punjabi", "Punjabi"),
    ("pizza", "Pizza"),
    ("dabeli", "Dabeli"),
    ("manchurian", "Manchurian"),
)

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Choice
		exclude=('user',)'''

class SignupForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Person
        fields = ('first_name',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
#	password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
#	password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

#	class Meta:
#	    model = Person
#	    fields = ('first_name',)

#	def clean_password2(self):
	    # Check that the two password entries match
#	    password1 = self.cleaned_data.get("password1")
#	    password2 = self.cleaned_data.get("password2")
#	    if password1 and password2 and password1 != password2:
#	        raise forms.ValidationError("Passwords don't match")
#	    return password2

#	def save(self, commit=True):
	    # Save the provided password in hashed format
#	    user = super().save(commit=False)
#	    user.set_password(self.cleaned_data["password1"])
#	    if commit:
#	        user.save()
#	    return user

class LoginForm(forms.Form):
	username	=forms.CharField()
	password 	=forms.CharField(widget=forms.PasswordInput)

	def clean(self,*args,**kwargs):
		username=self.cleaned_data.get("username")
		password=self.cleaned_data.get("password")

		if username and password:
			user=authenticate(username=username,password=password)
			if not user:
				raise forms.ValidationError("This User Does Not Exists")
			if user.check_password(password):
				raise forms.ValidationError("Incorrect Password")
			if not user.is_active:
				raise forms.ValidationError("This User Not Longer Active")
		return super(LoginForm,self).clean(*args,**kwargs)

class PersonForm(forms.ModelForm):
	class Meta:
		model 	=Person
		County 	=forms.CharField(max_length=240,widget=forms.Select(choices=CHOICES))
		exclude	=('user','website',)

class PersonT(forms.Form):
	class Meta:
		model =PersonType
		fields=('title',)
	County 	=forms.CharField(max_length=240,widget=forms.Select(choices=CHOICES))

	def clean_first_name(self,*args,**kwargs):
		first_name=self.cleaned_data.get('first_name')
		print(first_name)
