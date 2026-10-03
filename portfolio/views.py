from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import ListView, DetailView
from .models import Project, TechStack, PersonalInformation, Testimony, Inquiry
from .forms import AdminLoginForm, ProjectForm, TechStackForm, TestimonyForm


def admin_login_view(request):
    """
    Superuser/Admin ONLY Login View (Requirement #1)
    Regular users cannot authenticate on this page even if account exists.
    """
    if request.user.is_authenticated and request.user.is_superuser:
        return redirect('portfolio:dashboard')

    form = AdminLoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('portfolio:dashboard')
        else:
            messages.error(request, "Access restricted. Only superuser/admin accounts can sign in.")

    return render(request, 'portfolio/login.html', {'form': form})


def admin_logout_view(request):
    logout(request)
    return redirect('portfolio:admin_login')


@login_required(login_url='portfolio:admin_login')
def dashboard_view(request):
    """
    Dashboard Page (/dashboard/)
    Displays Table of Projects and Table of Tech Stacks (Requirement #2)
    """
    if not request.user.is_superuser:
        messages.error(request, "Superuser access required.")
        return redirect('portfolio:admin_login')

    projects = Project.objects.prefetch_related('tech_stacks').all()
    tech_stacks = TechStack.objects.prefetch_related('projects').all()

    context = {
        'projects': projects,
        'tech_stacks': tech_stacks,
    }
    return render(request, 'portfolio/dashboard.html', context)


@login_required(login_url='portfolio:admin_login')
def create_project_view(request):
    """
    Create Project View (Requirement #3)
    """
    if not request.user.is_superuser:
        return redirect('portfolio:admin_login')

    form = ProjectForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        project = form.save(commit=False)
        project.save()
        form.save_m2m()  # Save many-to-many relationship
        messages.success(request, "Project created successfully.")
        return redirect('portfolio:dashboard')

    return render(request, 'portfolio/create_project.html', {'form': form})


@login_required(login_url='portfolio:admin_login')
def create_tech_stack_view(request):
    """
    Create Tech Stack View (Requirement #3)
    """
    if not request.user.is_superuser:
        return redirect('portfolio:admin_login')

    form = TechStackForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "Tech Stack created successfully.")
        return redirect('portfolio:dashboard')

    return render(request, 'portfolio/create_tech_stack.html', {'form': form})


# Public-facing views
def home_view(request):
    personal_info = PersonalInformation.objects.first()
    return render(request, 'portfolio/index.html', {'personal_info': personal_info})


def personal_info_view(request):
    personal_info = PersonalInformation.objects.first()
    return render(request, 'portfolio/personal_info.html', {'personal_info': personal_info})


class ProjectListView(ListView):
    model = Project
    template_name = 'portfolio/projects.html'
    context_object_name = 'projects'


def project_detail_view(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'portfolio/projects_detail.html', {'project': project})


class TestimonyListView(ListView):
    model = Testimony
    template_name = 'portfolio/testimony_list.html'
    context_object_name = 'testimonies'


def testimony_detail_view(request, pk):
    testimony = get_object_or_404(Testimony, pk=pk)
    return render(request, 'portfolio/testimony_detail.html', {'testimony': testimony})


def add_testimony_view(request):
    form = TestimonyForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('portfolio:testimony_list')
    return render(request, 'portfolio/add_testimony.html', {'form': form})


def contact_view(request):
    if request.method == 'POST':
        Inquiry.objects.create(
            first_name=request.POST.get('first_name', ''),
            last_name=request.POST.get('last_name', ''),
            contact_number=request.POST.get('contact_number', ''),
            email=request.POST.get('email', ''),
            address=request.POST.get('address', ''),
            message=request.POST.get('message', '')
        )
        return render(request, 'portfolio/contact_success.html')

    return render(request, 'portfolio/contact.html')