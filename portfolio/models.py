from django.db import models

class Profile(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='profile_pictures/')
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Skill(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField()  # 1 to 100 scale or use choices

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)
    created_at = models.DateField()
    updated_at = models.DateField()

    def __str__(self):
        return self.title

class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.degree} - {self.institution}"

class Experience(models.Model):
    job_title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.job_title} at {self.company}"

class Contact(models.Model):
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.email
