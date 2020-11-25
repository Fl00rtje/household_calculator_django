from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

from .models import Person, House
from .forms import PersonForm, HouseForm


def home(request):
    return render(request, 'calculate_it/base.html')

def persons(request):
	persons = Person.objects.all()
	return render(request, 'calculate_it/persons.html', {'persons': persons})

def person_new(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            person = form.save(commit=False)
            person.save()
            return redirect('/persons', pk=person.pk)
    else:
        form = PersonForm()
    return render(request, 'calculate_it/person_new.html', {'form': form})

def house(request):
    houses = House.objects.all()
    if request.method == "POST":
        form = HouseForm(request.POST)
        if form.is_valid():
            house = form.save(commit=False)
            house.save()
            return redirect('/house', pk=house.pk)
    else:
        form = HouseForm()
    return render(request, 'calculate_it/house.html', {'houses': houses, 'form': form})

