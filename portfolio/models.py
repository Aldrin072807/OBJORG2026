from django.db import models


class TechStack(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Tech Stacks"
        ordering = ['-created_at']

    def __str__(self):
        return self.name


class Project(models.Model):
    project_name = models.CharField(max_length=200)
    description = models.TextField()
    tech_stacks = models.ManyToManyField(TechStack, related_name='projects', blank=True)
    link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Projects"
        ordering = ['-created_at']

    def __str__(self):
        return self.project_name

    @property
    def tech_stack_names(self):
        return ", ".join([ts.name for ts in self.tech_stacks.all()])


class PersonalInformation(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    summary = models.TextField()
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Personal Information"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# Alias PersonalInfo to PersonalInformation
PersonalInfo = PersonalInformation


class Inquiry(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Inquiries"

    def __str__(self):
        return f"Inquiry from {self.first_name} {self.last_name}"


class Testimony(models.Model):
    full_name = models.CharField(max_length=150)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Testimonies"

    def __str__(self):
        return f"Testimony by {self.full_name}"