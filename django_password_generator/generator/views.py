from django.shortcuts import render
# from generator import views
import random


# Create your views here.
def about(request):
    return render(request, "generator/about.html")

def home(request):
    return render(request, "generator/home.html")

def password(request):
    
    characters = list("aasrwqhiwqoikcxznmvfsdlkfdgoijn")
    generated_password = " "

    lenght = int(request.GET.get("lenght"))

    if request.GET.get("uppercase"):
        characters.extend(list("ABCDFGHTLTOGUSNDSNKTUYFASDBFEWSUODTS"))

    if request.GET.get("special"):
        characters.extend(list("!@#$%&/()=ñÑ"))
    
    if request.GET.get("numbers"):
        characters.extend(list("1234567890"))

    for x in range(lenght):
        generated_password += random.choice(characters)

    return render(request, "generator/password.html", {"password": generated_password})