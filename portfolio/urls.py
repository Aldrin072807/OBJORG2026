from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('personal-info/', views.personal_info_view, name='personal_info'),
    path('projects/', views.ProjectListView.as_view(), name='project_list'),
    path('projects/<int:pk>/', views.project_detail_view, name='project_detail'),
    path('testimonies/', views.TestimonyListView.as_view(), name='testimony_list'),
    path('testimonies/<int:pk>/', views.testimony_detail_view, name='testimony_detail'),
    path('testimonies/add/', views.add_testimony_view, name='add_testimony'),
    path('contact/', views.contact_view, name='contact'),

    # Quiz 5 & 6 Superuser Admin Dashboard Routes
    path('login/', views.admin_login_view, name='admin_login'),
    path('logout/', views.admin_logout_view, name='admin_logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('dashboard/projects/create/', views.create_project_view, name='create_project'),
    path('dashboard/tech-stacks/create/', views.create_tech_stack_view, name='create_tech_stack'),
]