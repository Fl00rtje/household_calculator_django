from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def persons(request):
	return render(request, 'calculate_it/persons.html', {})
    # return HttpResponse("Hello, world. This is the persons view. Yay!")
