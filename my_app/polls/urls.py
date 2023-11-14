from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('persons/', views.person_list, name='person-list'),
    path('persons/<int:pk>/', views.person_detail, name='person-detail'),
    path('persons/search/<str:search_string>/', views.person_list_by_name, name='person-list-by-name'),
    path('positions/', views.position_list, name='position-list'),
    path('positions/<int:pk>/', views.position_detail, name='position-detail'),
    path('persons/add/', views.add_person, name='add-person'),
    path('positions/add/', views.add_position, name='add-position'),
]