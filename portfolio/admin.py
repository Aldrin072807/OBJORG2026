from django.contrib import admin
from .models import Inquiry, PersonalInformation, Project, TechStack, Testimony

admin.site.register(Inquiry)
admin.site.register(PersonalInformation)
admin.site.register(Project)
admin.site.register(TechStack)
admin.site.register(Testimony)