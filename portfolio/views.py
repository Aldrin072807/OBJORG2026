from django.http import HttpResponse
from django.shortcuts import render

def home_view(request):
    return render(request, 'portfolio/index.html')

def about_view(request):
    return HttpResponse("About page coming soon!")

def project_list(request):
    return render(request, 'portfolio/projects.html')

def testimony_list(request):
    return render(request, 'portfolio/testimonials.html')

def contact_view(request):
    return render(request, 'portfolio/contact.html')