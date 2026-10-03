from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('projects/', views.project_list, name='project_list'),
    path('testimonials/', views.testimony_list, name='testimony_list'),
    path('contact/', views.contact_view, name='contact'),
]