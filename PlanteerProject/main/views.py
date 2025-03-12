from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from plants.models import Plant
from .models import Contact
# Create your views here.
def home_view(request:HttpRequest):
    plants= Plant.objects.all()[0:3]

    return render(request,"main/index.html" ,{"plants":plants})

def contact_view(request:HttpRequest):
    if request.method == "POST":
        new_mesg=Contact(first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'],message=request.POST['message'] )
        new_mesg.save()
    
        return redirect(request.GET.get("next", "/"))

    return render(request,"main/contact.html" )
