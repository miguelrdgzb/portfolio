from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    profile = Profile.objects.first()
    skill = Skill.objects.all() 
    projects = Project.objects.all()
    education = Education.objects.all() 
    contact = Contact.objects.first()
    experience = Experience.objects.all()
    # bio
    bio = profile.bio.split('.')
    first_five = bio[:5]
    bio_excerpt = '.'.join(first_five) 
    return render(request, 'index.html', {'profile': profile,
                                          'Skill': skill,
                                          'projects': projects,
                                          'education': education,
                                          'contact': contact,
                                          'experience': experience,
                                          'bio_excerpt': bio_excerpt})

def about(request):
    profile = Profile.objects.first()
    nombreApellidos = profile.first_name + " " + profile.last_name
    return render(request, 'about.html',{'profile': profile,
                                         'nombreApellidos': nombreApellidos})

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

