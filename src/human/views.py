
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.detail import DetailView

# Create your views here.
from .models import PersonType, Person
from .forms import PersonForm, PersonT, LoginForm, SignupForm
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import(
	authenticate,
	get_user_model,
	login,
	logout,
	)
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.decorators import login_required

from django.shortcuts import render,get_object_or_404
#from django.contrib.auth.form import UserCreationForm
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
#from .models import Profile, Choice
#from .forms import ProfileForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
'''
def index(request):
	#save_user=Profile(user=request.user)
	
	form=ProfileForm(request.POST, instance=save_user)
	if form.is_valid():
		obj=form.save(commit=False)
		obj.save()
		#return HttpResponseRedirect("/human/{num}".format(num=obj.id))
	#messages.success(request," submitted ur form")
	template='food/index.html'
	context={
		"form":form
	
	}
	return render(request,template,context)'''

def gmail(request):
    subject = "Hey Bro"
    message = "This msg using a django,user ur boss sachin"
    from_email = settings.EMAIL_HOST_USER
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ['maharanamahesh6@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/human/comman/')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')

def comman(request):
	return render(request,"comman.html",{})

def register(request):
	title="SignUp"
	form=UserCreationForm(request.POST or None)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect("/human")
	return render(request,'signup.html',{"form":form})
	
def login_v(request):
	title="Login"
	form=LoginForm(request.POST or None)
	if form.is_valid():
		username=form.cleaned_data.get("username")
		password=form.cleaned_data.get("password")
		user=authenticate(request, username=username,password=password)
		login(request,user)
	return render(request,"login.html",{"form":form,"title":title})

def logout_v(request):
	login(request)
	return redirect("/")

def person_about(request):
	return render(request,'about.html',{})

def person_delete(request,id=None):
	obj=get_object_or_404(Person,id=id)
	if request.method=='POST':
		obj.delete()
		messages.success(request,"Deleted Your Form")
		return HttpResponseRedirect("/human/")
	context={
		'obj':obj
	}
	template='person_delete.html'
	return render(request,template,context)

def person_update(request,id=None):
	obj=get_object_or_404(Person,id=id)
	form=PersonForm(request.POST or None)
	if form.is_valid():
		obj=form.save(commit=False)
		#print(form.cleaned_data)
		obj.save()
		return HttpResponseRedirect("/human/{num}".format(num=obj.id))
	messages.success(request,"Successfull Submitted Your Form")
	context={
		'obj':obj,
		'form':form
	}
	template='form.html'
	return render(request,template,context)

def person_list(request):
	query=request.GET.get('q',None)
	obj_list=Person.objects.all()
	if query is not None:
		obj_list=obj_list.filter(
				Q(first_name__icontains=query)
			)
	context={
		'obj_list':obj_list
	}
	template='person_list.html'
	return render(request,template,context)

def person_detail(request,id=None):
	obj=get_object_or_404(Person,id=id)
	context={
		'obj':obj
	}
	template='person_detail.html'
	return render(request,template,context)


def person(request):
	form=PersonForm(request.POST)
	if form.is_valid():
		obj=form.save(commit=False)
		#print(form.cleaned_data)
		obj.save()
		return HttpResponseRedirect("/human/{num}".format(num=obj.id))
	messages.success(request,"Successfull submitted ur form")
	context={
		'form':form
	}
	template='form.html'
	return render(request,template,context)

#def gmail(request):
#	form=LoginForm(request.POST or None)
#	if form.is_valid():
#		username=form.cleaned_data.get("username")
#		password=form.cleaned_data.get("password")
#		subject='site login form'
#		from_email=settings.EMAIL_HOST_USER
#		to_email=[from_email,'kundankukadiya059@gmail.com']
#		contact_message="%s: %s via %s"%(
#				username,
#				password,
#			)
#		some_messages="helooo"
#		send_mail=(
#			subject,
#			from_email,
#			to_email,
#			some_messages,
#			)
#	context={
#		'form':form
#	}
#	template='form.html'
#	return render(request,template,context)

