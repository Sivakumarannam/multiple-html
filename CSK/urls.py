from CSK.views import *
from django.urls import path
app_name='something_something'
urlpatterns=[
    path('msd/', msd, name='msd'),
    path('raina/', raina, name='raina'),
]