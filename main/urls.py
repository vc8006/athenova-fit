from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('homeS', views.homeS,name="homeS"),
    path('about', views.about,name="about"),
    path('Programs', views.Programs,name="Programs"),
    path('contact', views.contact,name="contact"),
    path('contactS', views.contactS,name="contactS"),
    path('gallery', views.gallery,name="gallery"),
]
