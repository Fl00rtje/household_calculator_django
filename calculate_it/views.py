from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Person
from .forms import PersonForm


def persons(request):
	persons = Person.objects.all()
	return render(request, 'calculate_it/persons.html', {'persons': persons})

def person_new(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            person = form.save(commit=False)
            person.save()
            return redirect('persons', pk=person.pk)
    else:
        form = PersonForm()
    return render(request, 'calculate_it/person_new.html', {'form': form})
