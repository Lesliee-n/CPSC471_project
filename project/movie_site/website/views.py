from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect 
from .forms import CreateUserForm

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def test(request):
    return render(request, 'test.html', {})

def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('home')
			

		context = {'form':form}
		return render(request, 'register.html', context)