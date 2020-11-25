from django.urls import path

from . import views

urlpatterns = [
	path('home', views.home, name='base'),
	path('house/new', views.house_new, name='house_new'),
	path('house', views.house, name='house'),
	path('houses', views.houses, name='houses'),
    path('persons', views.persons, name='persons'),
    path('person/new/', views.person_new, name='person_new'),
]