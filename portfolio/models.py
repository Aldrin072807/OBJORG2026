from django.db import models


class PersonalInformation(models.Model):
  first_name = models.CharField(max_length=100)
  middle_name = models.CharField(max_length=100, blank=True, null=True)
  last_name = models.CharField(max_length=100)
  summary = models.TextField()
  contact_number = models.CharField(max_length=20)
  email = models.EmailField()
  address = models.TextField()

  class Meta:
    verbose_name_plural = 'Personal Information'

  def __str__(self):
    return f'{self.first_name} {self.last_name}'


class Project(models.Model):
  project_name = models.CharField(max_length=200)
  description = models.TextField()
  tech_stack = models.CharField(max_length=200)
  link = models.URLField()

  class Meta:
    verbose_name_plural = 'Projects'

  def __str__(self):
    return self.project_name


class Testimony(models.Model):
  full_name = models.CharField(max_length=150)
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    verbose_name_plural = 'Testimonies'

  def __str__(self):
    return f'Testimony from {self.full_name}'


class Inquiry(models.Model):
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  contact_number = models.CharField(max_length=20)
  email = models.EmailField()
  address = models.TextField()
  message = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    verbose_name_plural = 'Inquiries'

  def __str__(self):
    return f'Inquiry from {self.first_name} {self.last_name}'