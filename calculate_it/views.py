from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Person


def persons(request):
	persons = Person.objects.all()
	return render(request, 'calculate_it/persons.html', {'persons': persons})
    # return HttpResponse("Hello, world. This is the persons view. Yay!")
