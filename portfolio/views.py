# portfolio/views.py
from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Contact
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login

def index(request):
    projects = [
        {
            'id': 1,
            'title': 'ETL Pipelines in Apache Airflow',
            'description': 'With Airflow, data teams can schedule, monitor, and manage the entire data workflow.',
            'image_url': 'static/images/image1.jpg'
        },
        {
            'id': 2,
            'title': 'Project 2',
            'description': 'A brief description of Project 2.',
            'image_url': 'static/images/image1.jpg'
        },
    ]
    successful_companies_count = 12000  # Replace with your actual count
    return render(request, 'portfolio/index.html', {
        'projects': projects,
        'contact_form': ContactForm(),
        'successful_companies_count': successful_companies_count
    })

def brief_summary(request):
    summary = {
        'title': 'About Me',
        'content': 'I am a passionate Data Engineer with experience in various technologies \n in developing, orchestrating scalable data pipelines \n I have 4 years of experience data engineering fileds'
    }
    return render(request, 'portfolio/brief_summary.html', {
        'summary': summary,
        'contact_form': ContactForm()
    })

def skills(request):
    skills = {
        'Programming Languages': ['Python', 'JavaScript', 'C++'],
        'Frameworks': ['Django', 'React', 'Flask'],
        'Tools': ['Git', 'Docker', 'Jenkins']
    }
    return render(request, 'portfolio/skills.html', {
        'skills': skills,
        'contact_form': ContactForm()
    })

def completed_projects(request):
    completed_projects = [
        {
            'id': 1,
            'title': 'Completed Project 1',
            'description': 'Detailed description of completed project 1...',
            'image_url': 'static/images/completed1.jpg'
        },
        {
            'id': 2,
            'title': 'Completed Project 2',
            'description': 'Detailed description of completed project 2...',
            'image_url': 'static/images/completed2.jpg'
        },
    ]
    return render(request, 'portfolio/completed_projects.html', {
        'projects': completed_projects,
        'contact_form': ContactForm()
    })

def ongoing_projects(request):
    ongoing_projects = [
        {
            'id': 1,
            'title': 'Ongoing Project 1',
            'description': 'Detailed description of ongoing project 1...',
            'image_url': 'static/images/ongoing1.jpg'
        },
        {
            'id': 2,
            'title': 'Ongoing Project 2',
            'description': 'Detailed description of ongoing project 2...',
            'image_url': 'static/images/ongoing2.jpg'
        },
    ]
    return render(request, 'portfolio/ongoing_projects.html', {
        'projects': ongoing_projects,
        'contact_form': ContactForm()
    })

def project_detail(request, id):
    project = {
        'id': id,
        'title': f'Project {id}',
        'description': f'Detailed description of project {id}...',
        'image_url': f'static/images/project{id}.jpg',
        'technologies': ['Python', 'Django', 'JavaScript'],
        'live_demo_url': 'https://example.com/demo',
        'github_url': 'https://github.com/user/project',
    }
    return render(request, 'portfolio/project_detail.html', {
        'project': project,
        'contact_form': ContactForm()
    })
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Manually process the form data
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            message = form.cleaned_data.get('message')

            return redirect('contact_success')
    else:
        form = ContactForm()

    return render(request, 'portfolio/contact.html', {'form': form})

def contact_success(request):
    return render(request, 'portfolio/contact_success.html')

def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'portfolio/contact_list.html', {'contacts': contacts})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Log the user in after signup
            return redirect('home')  # Redirect to home or any other page
    else:
        form = UserCreationForm()
    
    return render(request, 'portfolio/signup.html', {'form': form})

