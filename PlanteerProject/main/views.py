from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from plants.models import Plant
from .models import Contact
from django.core.paginator import Paginator

# Create your views here.
def home_view(request:HttpRequest):
    plants= Plant.objects.all()

    page_number =request.GET.get("page",1)
    paginator =Paginator(plants,3)
    plants_page =paginator.get_page(page_number)

    return render(request,"main/index.html" ,{"plants":plants_page})

def contact_view(request:HttpRequest):
    if request.method == "POST":
        new_mesg=Contact(first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'],message=request.POST['message'] )
        new_mesg.save()
    
        return redirect(request.GET.get("next", "/"))

    return render(request,"main/contact.html" )
