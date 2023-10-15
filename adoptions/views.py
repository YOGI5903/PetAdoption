from django.shortcuts import render
from .models import Pet,Rehomer
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse
from django.shortcuts import render, redirect
from .models import Pet



def home(request):
    return render(request, 'adoptions/base.html')

def adopt(request):
    pets = Pet.objects.all()
    if request.method =="post":
        pets = load(request)
        pet_type = request.POST['pet_type']
        breed = request.POST['breed']
        vaccination=request.POST['vaccination']

        if pet_type:
            pets = pets.filter(pet_type=pet_type)
        if breed:
            pets = pets.filter(breed=breed)
        if breed:
            pets = pets.filter(vaccination=vaccination)
        
    context = {'pets': pets}
    return render(request, 'adoptions/adopt.html', context)

def load(request):
    pet_type = request.POST['pet_type']
    breed = request.POST['breed']
    vaccination=request.POST['vaccination']

    if pet_type:
        pets = pets.filter(pet_type=pet_type)
    if breed:
        pets = pets.filter(breed=breed)
    if breed:
        pets = pets.filter(vaccination=vaccination)
    return pets


def rehome(request):
    
    name=request.POST['name']
    age=request.POST['age']
    breed=request.POST['breed']
    image=request.FILES['image']
    vaccination=request.POST['vaccination']
    pet_type=request.POST['pet_type']
    a=Pet(name=name,age=age,vaccination=vaccination,image=image,breed=breed,pet_type=pet_type)
    a.save()
    return HttpResponseRedirect('rehomerform')

def rehomeform(request):
    t=loader.get_template('adoptions/rehomeform.html')
    return HttpResponse(t.render({},request))


def rehomer(request):
    first_name=request.POST['first_name']
    last_name=request.POST['last_name']
    number=request.POST['number']
    address=request.POST['address']
    email=request.POST['email']
    password=request.POST['password']
    a=Rehomer(first_name=first_name,last_name=last_name,number=number,address=address,email=email,password=password)
    a.save()
    return HttpResponseRedirect('backhome')


def rehomerform(request):
    t=loader.get_template('adoptions/rehomerform.html')
    return HttpResponse(t.render({},request))

def backhome(request):
    return HttpResponseRedirect(reverse("home"))

def filter(request):
    pets = Pet.objects.all()
    pet_type = request.POST['pet_type']
    breed = request.POST['breed']
    if request.POST['vaccination']:
        vaccination=request.POST['vaccination']

    if pet_type:
        pets = pets.filter(pet_type=pet_type)
    if breed:
        pets = pets.filter(breed=breed)
    if vaccination:
        pets = pets.filter(vaccination=vaccination)
        
    context = {'pets': pets}
    return render(request, 'adoptions/adopt.html', context)

def backadopt(request):
    return HttpResponseRedirect(reverse("adopt"))