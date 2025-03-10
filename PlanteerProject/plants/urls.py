from . import views
from django.urls import path


app_name='plants'

urlpatterns=[
    path('new/' ,views.add_plant_view,name="add_plant_view")

]