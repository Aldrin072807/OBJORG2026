from django.urls import path

from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('personal-info/', views.personal_info_view, name='personal_info'),
    path('projects/', views.project_list_view, name='project_list'),
    path(
        'projects/<int:pk>/', views.project_detail_view, name='project_detail'
    ),
    path('projects/add/', views.add_project_view, name='add_project'),
    path('contact/', views.contact_view, name='contact'),
    path(
        'contact/success/',
        views.contact_success_view,
        name='contact_success',
    ),
    path(
        'testimonies/',
        views.TestimonyListView.as_view(),
        name='testimony_list',
    ),
    path(
        'testimonies/add/', views.add_testimony_view, name='add_testimony'
    ),
    path(
        'testimonies/<int:pk>/',
        views.testimony_detail_view,
        name='testimony_detail',
    ),
]