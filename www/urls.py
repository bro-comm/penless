from django.urls import path
from www import views

urlpatterns = [
    # The home page
    path('', views.index, name='index'),

    ]
