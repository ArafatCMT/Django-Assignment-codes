from django.shortcuts import render
from cars import models

def home(request, slug=None):
    cars = models.CarModel.objects.all()
    brands = models.CarBrande.objects.all()

    if slug is not None:
        brand = models.CarBrande.objects.get(slug = slug) # slug name er object ta neye aslam
        cars = models.CarModel.objects.filter(brand = brand)
        
    return render(request, 'home.html', {'cars': cars, 'brands': brands})