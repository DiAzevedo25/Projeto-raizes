from django.urls import path
from .views import *

#* é para importar tudo

urlpatterns = [path('', index, name = 'index')]