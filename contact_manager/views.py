from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.conf import settings
from django.middleware.csrf import get_token
import requests
import json

class RegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

def display_contact_details(request, contact_id):
    api_url = f"{settings.API_BASE_URL}/api/contacts/{contact_id}"    
    response = requests.get(api_url, headers={'X-CSRFToken': get_token(request)})

    if response.status_code == 200:
        try:
            contact_data = response.json()
            return render(request, 'contact_manager/contact_details.html', {'contact': contact_data})
        except json.JSONDecodeError as e:
            print(f"JSON Decode Error: {e}")
            print(f"Response Text: {response.text}")
            error_message = 'Error fetching contact details: Invalid JSON'
            return render(request, 'contact_manager/error.html', {'error_message': error_message})
    else:
        error_message = f'Error fetching contact details: {response.status_code}'
        return render(request, 'contact_manager/error.html', {'error_message': error_message})

def display_contact_list(request):
    api_url = f"{settings.API_BASE_URL}/api/contacts/"
    headers = {'X-CSRFToken': get_token(request)}
    
    response = requests.get(api_url, headers=headers)
    
    if response.status_code == 200:
        contacts = response.json()
        print("Contacts data:", contacts)
        return render(request, 'contact_manager/contact_list.html', {'contacts': contacts})
    else:
        error_message = f'Error fetching contact list: {response.status_code}'
        print(error_message) 
        return render(request, 'contact_manager/error.html', {'error_message': error_message})


@login_required
def contact_delete(request, contact_id):
    api_url = f"{settings.API_BASE_URL}/api/contacts/{contact_id}"
    headers = {'X-CSRFToken': get_token(request)}
    
    if request.method == 'POST' and request.POST.get('_method') == 'DELETE':
        response = requests.delete(api_url, headers=headers)
        if response.status_code == 204:
            return redirect('contacts')
        else:
            error_message = f'Error deleting contact: {response.status_code}'
            return render(request, 'contact_manager/error.html', {'error_message': error_message})
    else:
        response = requests.get(api_url, headers=headers)
        if response.status_code == 200:
            contact = response.json()
            return render(request, 'contact_manager/contact_delete.html', {'contact': contact})
        else:
            error_message = f'Error fetching contact details: {response.status_code}'
            return render(request, 'contact_manager/error.html', {'error_message': error_message})
