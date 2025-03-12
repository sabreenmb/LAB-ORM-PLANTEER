from django.db import models

# Create your models here.


class Plant(models.Model):


    class CategoryChoices(models.TextChoices):
        TREE = 'TR','Trees'
        SHRUB = 'SH', 'Shrubs'
        HERB = 'HB','Herbs'
        FLOWER = 'FL','Flowers'
        FERN = 'FR','Ferns'
        GRASS = 'GR','Grasses'
        SUCCULENT = 'SU', 'Succulents and Cacti'
        VINE = 'VI','Vines and Climbing Plants'
        AQUATIC = 'AQ','Aquatic Plants'
        HOUSEPLANT = 'HP','Houseplants'

    name=models.CharField(max_length=1024)
    about=models.TextField()
    used_for=models.TextField()
    image=models.ImageField(upload_to="images/")
    category=models.CharField(choices=CategoryChoices.choices , max_length=1024)
    is_edible=models.BooleanField()
    created_at=models.DateTimeField(auto_now_add=True)

class Review(models.Model):
    plant =models.ForeignKey(Plant, on_delete=models.CASCADE)
    full_name= models.CharField(max_length=256)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)