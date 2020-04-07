from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from .models import Pin
from .forms import PinCreateForm


def index(request):
    images = Pin.objects.all().order_by('-created')
    return render(request, 'pinterest/index.html', {
                'images': images,
                'index': 'Home'
        })


def my_post(request):
    user = request.user
    context = {}
    if user:
        images = Pin.objects.filter(user=user).order_by('-created')
        message = "Your pinned images"
    else:
        message = "You have no images pinned"
    context = {
        'images': images,
        'message': message,
        'my_post': 'My Posts'
    }
    return render(request, 'pinterest/index.html', context)


# @login_required
def image_create(request):
    if request.method == 'POST':

        form = PinCreateForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()
            messages.success(request, 'Image added successfully')
            return redirect('pinterest:my_post')

    else:
        form = PinCreateForm()
    return render(request, 'pinterest/pin/create.html', {
        'section': 'images',
        'form': form,
        'create': 'New Post'
    })


def delete_image(request, id):
    pin = get_object_or_404(Pin, id=id)
    pin.delete()
    return redirect("pinterest:my_post")


def like_image(request):
    user = request.user
    id = request.POST.get('id')
    action = request.POST.get('action')
    if id and action:
        pin = Pin.objects.get(id=id)
        if action == "like":
            pin.user_like.add(user)
        else:
            pin.user_like.remove(user)
        return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'ko'})
