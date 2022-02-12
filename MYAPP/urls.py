from django.urls import path
from .views import *
from . import views

app_name = 'MYAPP'

urlpatterns = [
    path('', route1, name='route1')
]