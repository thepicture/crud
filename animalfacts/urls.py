from django.urls import path

from . import views

appname = 'animalfacts'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:fact_id>/', views.detail, name='detail'),
]
