from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from .models import Plant,Review
from django.db.models import Q

# Create your views here.



def add_plant_view(request:HttpRequest):
    if request.method == "POST":
        new_plant=Plant(name=request.POST['name'],about=request.POST['about'], used_for=request.POST['used_for'],is_edible= True if request.POST.get('is_edible')=="True" else False,category=request.POST['category'] , image=request.FILES['image'])
        new_plant.save()
        return redirect("main:home_view")
        # return redirect(request.GET.get("next", "/"))
    return render(request , "plants/new_plant.html" ,{"CategoryChoices": Plant.CategoryChoices.choices})

def all_plants_view(request:HttpRequest):
    # category = request.COOKIES.get("category", "all")
    is_edible = request.COOKIES.get("Edible", "False")
    plants =Plant.objects.all()

    if 'category' in request.GET:
        category=request.GET.get('category')
        if category!='All':
            plants=plants.filter(category=category)
    
    if 'Edible' in request.GET:
        is_edible=request.GET.get('Edible')
        if is_edible!='All':
            plants=plants.filter(is_edible=is_edible)




    # plants= Plant.objects.filter(
    #         Q(category=category) & Q(is_edible=is_edible)
    #     )
    return render(request , "plants/all_plants.html" ,{"plants":plants ,"CategoryChoices": Plant.CategoryChoices.choices})

def search_plants_view(request:HttpRequest):
    plants =Plant.objects.all()
    if 'search' in request.GET:
        search_term = request.GET.get('search')
        plants = plants.filter(
            Q(used_for__icontains=search_term) | Q(name__icontains=search_term)
        )

    return render(request , "plants/search_plant.html" ,{"plants":plants})

def plant_details_view(request:HttpRequest, plant_id :int):
    plant =Plant.objects.get(pk=plant_id)
    reviews= Review.objects.filter(plant=plant)
    related_plants=Plant.objects.filter(category=plant.category).exclude(pk=plant_id)[0:3]
    return render(request , "plants/plant_details.html" ,{"plant":plant , "related_plants":related_plants ,"reviews":reviews})


def delete_plant_view(request:HttpRequest, plant_id :int):
    plant =Plant.objects.get(pk=plant_id)
    plant.delete()
    response = redirect(request.GET.get("next", "/"))
    return response

def update_plant_view(request:HttpRequest, plant_id :int):

    plant =Plant.objects.get(pk=plant_id)
    if request.method == "POST":
        plant.name = request.POST["name"]
        plant.about = request.POST["about"]
        plant.used_for = request.POST["used_for"]
        plant.category = request.POST["category"]
        plant.is_edible = True if request.POST.get('is_edible')=="True" else False
        if "image" in request.FILES:
            plant.image = request.FILES["image"]
        plant.save()



        return redirect("plants:plant_details_view", plant_id=plant.id)

    return render(request , "plants/plant_update.html" ,{"plant":plant ,"CategoryChoices": Plant.CategoryChoices.choices})


def add_review_view(request:HttpRequest,plant_id:int):
    if request.method == "POST":
        selected_plant=Plant.objects.get(pk=plant_id)
        new_review=Review(plant=selected_plant,full_name=request.POST['full_name'],content=request.POST['content'])
        new_review.save()
    
    return redirect("plants:plant_details_view",plant_id =plant_id)






