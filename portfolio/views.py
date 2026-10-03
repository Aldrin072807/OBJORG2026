from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView

from .forms import ProjectForm, TestimonyForm
from .models import Inquiry, PersonalInformation, Project, Testimony


def home_view(request):
  personal_info = PersonalInformation.objects.first()
  return render(
      request, 'portfolio/index.html', {'personal_info': personal_info}
  )


def personal_info_view(request):
  personal_info = PersonalInformation.objects.first()
  return render(
      request, 'portfolio/personal_info.html', {'personal_info': personal_info}
  )


def project_list_view(request):
  projects = Project.objects.all()
  return render(request, 'portfolio/projects.html', {'projects': projects})


def project_detail_view(request, pk):
  project = get_object_or_404(Project, pk=pk)
  return render(
      request, 'portfolio/projects_detail.html', {'project': project}
  )


# Add Project: Function-Based Create View with Django Form
def add_project_view(request):
  if request.method == 'POST':
    form = ProjectForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('portfolio:project_list')
  else:
    form = ProjectForm()
  return render(request, 'portfolio/add_project.html', {'form': form})


# Contact Page: Function-Based View processing raw HTML Form
def contact_view(request):
  if request.method == 'POST':
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    contact_number = request.POST.get('contact_number')
    email = request.POST.get('email')
    address = request.POST.get('address')
    message = request.POST.get('message')

    Inquiry.objects.create(
        first_name=first_name,
        last_name=last_name,
        contact_number=contact_number,
        email=email,
        address=address,
        message=message,
    )
    return redirect('portfolio:contact_success')

  return render(request, 'portfolio/contact.html')


def contact_success_view(request):
  return render(request, 'portfolio/contact_success.html')


# Add Testimony: Function-Based Create View with Django Form
def add_testimony_view(request):
  if request.method == 'POST':
    form = TestimonyForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('portfolio:testimony_list')
  else:
    form = TestimonyForm()
  return render(request, 'portfolio/add_testimony.html', {'form': form})


# Listing Testimonies: Class-Based ListView
class TestimonyListView(ListView):
  model = Testimony
  template_name = 'portfolio/testimony_list.html'
  context_object_name = 'testimonies'


# Testimony Detail: Function-Based Detail View
def testimony_detail_view(request, pk):
  testimony = get_object_or_404(Testimony, pk=pk)
  return render(
      request, 'portfolio/testimony_detail.html', {'testimony': testimony}
  )