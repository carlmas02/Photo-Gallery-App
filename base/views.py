from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Image
from .forms import *

def home(request):
	if request.method == "POST":
		form = ImageUploadForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('home')

	else :		
		data = Image.objects.all()
		form = ImageUploadForm()
		context = {
			'data' : data,
			'form' : form
	    }

	return render(request, 'main.html', context=context)
