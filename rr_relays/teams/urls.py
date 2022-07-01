from django.urls import path

from . import views

app_name = 'teams'
urlpatterns = [
    path('', views.index, name='index'),
    path('timer/', views.timer, name='timer'),
]
