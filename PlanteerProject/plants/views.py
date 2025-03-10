from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from .models import Plant
# Create your views here.


def add_plant_view(request:HttpRequest):
    if request.method == "POST":
        new_plant=Plant(name=request.POST['name'],about=request.POST['about'], used_for=request.POST['used_for'],is_edible= True if request.POST.get('is_edible')=="True" else False,category=request.POST['category'] , image=request.FILES['image'])
        new_plant.save()
        return redirect("main:home_view")
        # return redirect(request.GET.get("next", "/"))
    return render(request , "plants/new_plant.html" ,{"CategoryChoices": Plant.CategoryChoices.choices})