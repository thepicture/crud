from django.urls import path, include

from . import views

appname = 'animalfacts'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:fact_id>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('edit/<int:fact_id>/', views.edit, name='edit'),
    path('api/create/', views.api_create, name='api_create'),
    path('api/edit/', views.api_edit, name='api_edit'),
    path('delete/<int:fact_id>/', views.delete, name='delete'),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),
]
