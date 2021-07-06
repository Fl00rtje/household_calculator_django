from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from .models import Person, House
from .forms import PersonForm, HouseForm


@login_required
def home(request):
    first_name = request.user.first_name

    context = {'first_name': first_name}
    return render(request, 'calculate_it/dashboard.html', context)


@login_required
def house_new(request):
    if request.method == "POST":
        form = HouseForm(request.POST)
        if form.is_valid():
            house = form.save(commit=False)
            house.save()
            return redirect('/house', pk=house.pk)
    else:
        form = HouseForm()
    return render(request, 'calculate_it/house_new.html', {'form': form})


@login_required
def persons(request):
    persons = Person.objects.all()
    return render(request, 'calculate_it/persons.html', {'persons': persons})


@login_required
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


@login_required
def houses(request):
    houses = House.objects.all()
    return render(request, 'calculate_it/houses.html', {'houses': houses})


def house(request):
    return render(request, 'calculate_it/house.html')


