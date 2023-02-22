from django.urls import path
from . import views
from .views import *
from .forms import *

urlpatterns = [
    path('', views.index, name='index'),
    path('details/<int:pizzaid>', views.details, name='details'),
    path('confirmation/', views.confirmation, name='confirmation'),
]