from django.urls import path
from . import views




urlpatterns = [
    path("", views.home, name="home"),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('thank-you/', views.thank_you, name='thank_you'),
    path('menu/', views.menu, name='menu'),

]