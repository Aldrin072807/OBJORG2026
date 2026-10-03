from django.contrib import admin

from .models import Inquiry, PersonalInformation, Project, Testimony

admin.site.register(PersonalInformation)
admin.site.register(Project)
admin.site.register(Testimony)
admin.site.register(Inquiry)