from django.urls import path, include

from . import views

from .views import popularity_chart, popularity_chart_json

appname = 'animalfacts'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:fact_id>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('edit/<int:fact_id>/', views.edit, name='edit'),
    path('api/create/', views.api_create, name='api_create'),
    path('api/edit/', views.api_edit, name='api_edit'),
    path('delete/<int:fact_id>/', views.delete, name='delete'),
    path('confirm/<int:fact_id>/', views.confirm, name='confirm'),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),
    path('popularity', popularity_chart, name='popularity'),
    path('popularityJSON', popularity_chart_json, name='popularity_json'),
]
