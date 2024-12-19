from django.urls import path,include
from .views import *

urlpatterns = [
    path('', home, name='home'), 
    path('add/', add_transaction, name='add_transaction'),
    
]
