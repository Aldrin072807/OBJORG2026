from django.shortcuts import get_object_or_404, render

from .models import PersonalInformation, Project


# View to display home page or personal info
def home_view(request):
  personal_info = PersonalInformation.objects.first()
  return render(
      request, 'portfolio/index.html', {'personal_info': personal_info}
  )


# View to return all personal info specifically
def personal_info_view(request):
  personal_info = PersonalInformation.objects.first()
  return render(
      request, 'portfolio/personal_info.html', {'personal_info': personal_info}
  )


# List view displaying all projects (titles only)
def project_list_view(request):
  projects = Project.objects.all()
  return render(request, 'portfolio/projects.html', {'projects': projects})


# Detail view for a specific project
def project_detail_view(request, pk):
  project = get_object_or_404(Project, pk=pk)
  return render(
      request, 'portfolio/projects_detail.html', {'project': project}
  )

def contact_view(request):
    return render(request, 'portfolio/contact.html')
