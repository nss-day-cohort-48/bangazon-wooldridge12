from django.urls import path
from .views import favoriteseller_list

urlpatterns = [
    path('reports/userfavorites', favoriteseller_list),
]
