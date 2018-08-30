from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Pin
from .forms import PinCreateForm

def index(request):
	images = Pin.objects.all()
	return render(request,'pinterest/index.html',{
		'images':images	
	})

# @login_required
def image_create(request):
	print("image_create")
	if request.method == 'POST':
		
		form = PinCreateForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			new_item = form.save(commit=False)
			new_item.user = request.user
			new_item.save()
			messages.success(request,'Image added successfully')
			return redirect(new_item.get_absolute_url())
		
	else:
		form = PinCreateForm()
	return render(request,'pinterest/pin/create.html',{
		'section':'images',
		'form':form	
	})


def image_detail(request, id ,slug):
	image = get_object_or_404(Pin,id=id, slug=slug)
	return render(request,'pinterest/pin/detail.html',{
		'section':'images',
		'image':image	
	})