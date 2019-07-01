from django.shortcuts import render
from .forms import SubscriberForm
from products.models import *
# Create your views here.


def landing(request):
    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)

        new_form = form.save()

    return render(request, 'landing\landing.html', locals())


def home(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True)
    return render(request, 'landing/home.html', locals())