from . import views
from django.urls import path


app_name='plants'

urlpatterns=[
    path('new/' ,views.add_plant_view,name="add_plant_view"),
    path('all/' ,views.all_plants_view,name="all_plants_view"),
    path('search/' ,views.search_plants_view,name="search_plants_view"),
    path('<plant_id>/detail/' ,views.plant_details_view,name="plant_details_view"),
    path('<plant_id>/delete/' ,views.delete_plant_view,name="delete_plant_view"),
    path('<plant_id>/update/' ,views.update_plant_view,name="update_plant_view"),
    path("add/review/<plant_id>/", views.add_review_view, name="add_review_view"),


]