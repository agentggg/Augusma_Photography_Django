from django.shortcuts import render
from django.views.generic.edit import CreateView
#   Import django CreateView
from .models import identity


from .models import user_login
#   Imports the .models lib which is used for DB tracking info
def user_login(request):
    #   The regular template for rendering views
    if request.method == "POST":
        #   The if statement that checks if a form has been submited
        login = user_login()
        #   Creates a DB model named "test_model"
        login.DB_field_name = request.POST["username"]
        login.DB_field_name = request.POST["password"]
        #   Assigns the form input identified by field_name to test_model.DB_field_name
        login.save()
        #   Saves the form data to the database
        return render(request, "registration/login.html")



from django.contrib.auth import authenticate
def login_view(request):
    username = request.POST("username")
    password = request.POST("password")
    user = authenticate(request, username=username, password=password)
    if user is not None:
        return redirect("index.html")
    else:
        return HttpResponse("Invalid Credentials!")



# Create your views here.
def index(request):
    return render(request, "web_app_1/index.html")

def contact(request):
    return render(request, "web_app_1/contact.html")

def about(request):
    return render(request, "web_app_1/about.html")

def portfolio(request):
    return render(request, "web_app_1/portfolio.html")

def login(request):
    return render(request, "registration/login.html")
