from django.urls import path
from . import views



urlpatterns = [
path('', views.index, name='index'),
path('news/<str:pk>', views.news, name='news'),
path('sport/<str:pk>', views.sport, name='sport'),
path('business/<str:pk>', views.business, name='business'),
path('politics/<str:pk>', views.politics, name='politics'),
path('contact', views.contact, name='contact'),


]