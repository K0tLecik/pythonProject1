from django.urls import path
from . import views

urlpatterns = [
    path('persons/', views.PersonList.as_view()),  # Obsługuje listę osób
    path('persons/<int:pk>/', views.PersonDetail.as_view()),  # Obsługuje szczegóły pojedynczej osoby
]