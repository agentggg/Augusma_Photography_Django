from django.shortcuts import render
from .forms import identity
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = identity(request.POST or None)
        if form.is_valid():
            form.save()
            print("form saved")
    return render(request, "message_me/index.html")

def instructions(request):
    return render(request, "message_me/contact.html")

def about(request):
    return render(request, "message_me/about.html")
