from django.urls import path
from guess import views


app_name = 'guess'
urlpatterns = [
    path('', views.guess, name='guess'),
]
