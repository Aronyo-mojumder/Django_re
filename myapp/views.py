from urllib import request

from django.contrib import messages
from django.shortcuts import render, redirect
from services.models import Service, Gallery, Team
from contact.models import Contact, Subscriber



def home(request):
    services_db = Service.objects.all()
    data = {'services': services_db}
    return render(request, "index.html", data)


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        message = request.POST.get('message')

        # Create Contact instance and save
        contact_instance = Contact(name=name, email=email, number=number, message=message)
        contact_instance.save()

        messages.success(request, 'Your message has been submitted successfully!')
        return redirect('contact')  # Redirect to the contact page again

    return render(request, 'contact.html')
def subscriber(request):
    if request.method == 'POST':
        # Retrieve the name and email from the POST data
        name = request.POST.get('name', '')  # Providing a default value to avoid potential NoneType
        email = request.POST.get('email', '')

        # Check if the name is not empty
        if name:
            # Now you can save the name and email to your Subscriber model
            subscriber_db = Subscriber(name=name, email=email)
            subscriber_db.save()

            messages.success(request, 'Thank you for subscribing!')
            return redirect('home')  # Assuming 'home' is the name of the URL pattern for your home page
        else:
            messages.error(request, 'Name cannot be empty.')

    return render(request, 'index.html')


def gallery(request):
    galleries_db = Gallery.objects.all()
    data = {'galleries': galleries_db}
    return render(request, 'gallery.html', data)


def projects(request):
    return render(request, 'project.html')


def team(request):
    teams_db = Team.objects.all()
    data = {'teams': teams_db}
    return render(request, 'team.html', data)
