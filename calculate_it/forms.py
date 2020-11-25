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
		labels = {
			'rent': ('How much do you pay for rent?'),
			'servicecosts': ('How much do you pay for servicecosts?'),
			'gas': ('How much do you pay for gas?'),
			'electricity': ('How much do you pay for electricity?'),
			}
		# help_texts = {'rent': ('Rent is here considered basic rent. '),}
		# error_messages = {'rent': {'max_length': ("Are you a millionaire?"),},}
