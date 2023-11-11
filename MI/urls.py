from MI.views import *
from django.urls import path
app_name = 'something'
urlpatterns=[
    path('rohit/',rohit,name='rohit'),
    path('bumrah/', bumrah, name='bumrah'),

]