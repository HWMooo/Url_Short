from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.Home, name = 'url-home'),
    path('shorten/', views.Shorten, name = 'url-Shorten')

]


