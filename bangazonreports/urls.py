from django.urls import path
from .views import favoriteseller_list
from .views import incompleteorder_list

urlpatterns = [
    path('reports/userfavorites', favoriteseller_list),
    path('reports/incompleteorders', incompleteorder_list)
]
