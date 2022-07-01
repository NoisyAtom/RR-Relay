from django.urls import path

from . import views

app_name = 'teams'
urlpatterns = [
    path("runners/", views.runners, name="runners"),
    path("team/", views.teams, name="teams"),
    path('', views.index, name='index'),
    path('timer/', views.timer, name='timer'),
    path('<str:runner_id>', views.find_runner, name="find_runner"),
    #path('<str:runner_id>/set', views.set_runner_time, name="set_runner_time")

]
