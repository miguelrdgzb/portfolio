from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    profile = Profile.objects.first()  # Obtiene el primer (y único) registro
    return render(request, 'index.html', {'profile': profile})

def about(request):
    profiles = Profile.objects.all
    return render(request, 'about.html')

def contact(request):
    contact = Contact.objects.all
    return render(request, 'contact.html')

def skill(request):
    skill = Skill.objects.all
    return render(request, 'services.html')

def education(request):
    education = Education.objects.all
    return render(request, 'generic.html')

def experience(request):
    experience = Experience.objects.all
    return render(request, 'generic.html')

def project(request):
    project = Project.objects.all
    return render(request, 'generic.html')

