from django import forms

from .models import Person, House


class PersonForm(forms.ModelForm):

	class Meta:
		model = Person
		fields = ('first_name', 'last_name',)

class HouseForm(forms.ModelForm):

	class Meta:
		model = House
		fields = ('rent', 'servicecosts', 'gas', 'electricity')