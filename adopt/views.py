from django.http import HttpResponse
from django.shortcuts import render
import random
from .models import Pet
from .forms import PetForm

# Create your views here.

#def all_pets(request):
#    text = ''
#    pets = Pet.objects.all()
#    for pet in pets:
#        text += pet.name + ','
#    return HttpResponse(text)

def all_pets(request):
    pets = Pet.objects.all()
    context = {
            'pets':pets,
    }
    return render(request,'adopt/all.html',context)



def pet_details(request,pet_id):
    pet = Pet.objects.get(id=pet_id)
    return HttpResponse(pet.name)

def add_pet(request):
    if request.method == 'POST':
        #check data with form
        form = PetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/adopt/list')
    else:
        form = PetForm()

    context = {
            'form':form,
    }

    return render(request,'adopt/edit.html',context)

def edit_pet(request,pet_id):
    pet = Pet.objects.get(id=pet_id)
    if request.method == 'POST':
        #check data with form
        form = PetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect(f'/adopt/{pet_id}')
    else:
        form = PetForm(instance=pet)
        #build a new empty form

    context = {
            'form':form,
    }

    return render(request,'adopt/edit.html',context)
