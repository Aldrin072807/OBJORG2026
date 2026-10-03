from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('personal-info/', views.personal_info_view, name='personal_info'),
    path('projects/', views.project_list_view, name='project_list'),
    path('projects/<int:pk>/', views.project_detail_view, name='project_detail'),
]