from django.urls import path

from . import views

appname = 'animalfacts'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:fact_id>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('api/create/', views.api_create, name='api_create'),
    path('delete/<int:fact_id>/', views.delete, name='delete'),
]
