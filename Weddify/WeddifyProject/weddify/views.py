from django.shortcuts import render
# from .models import User
# Create your views here.
def index(request):
    return render(request, "Weddify/index.html")

def register(request):
    if request.method == "POST":
        name = request.POST["name"]
        nameF = request.POST["name-f"]
        email = request.POST["email"]
        username = request.POST["login"]
        password = request.POST["password"]
    return render( request, "Weddify/register.html")
def venues(request):
    return render(request, "Weddify/venues.html")
