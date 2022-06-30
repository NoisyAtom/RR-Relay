from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:runner_id>', views.find_runner, name="find_runner"),
    path('<str:runner_id>/set', views.set_runner_time, name="set_runner_time")
]