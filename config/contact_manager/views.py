from django.shortcuts import render, redirect
from django.test import Client
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
import requests
import json


class RegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

@login_required
def display_contact_details(request, contact_id):
    api_url = f"http://localhost:8000/api/contacts/{contact_id}"    
    response = requests.get(api_url)

    
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


@login_required
def display_contact_list(request):
    api_url = "http://localhost:8000/api/contacts/"
    
    response = requests.get(api_url)
    
    if response.status_code == 200:
        contacts = response.json()
        print("Contacts data:", contacts)
        return render(request, 'contact_manager/contact_list.html', {'contacts': contacts})
    else:
        error_message = f'Error fetching contact list: {response.status_code}'
        return render(request, 'contact_manager/error.html', {'error_message': error_message})
    

@login_required
def contact_edit(request, contact_id):
    api_url = f"http://localhost:8000/api/contacts/{contact_id}"
    
    if request.method == 'POST':
        # Handle form submission and update the contact
        data = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'phone': request.POST.get('phone', ''),
            'email': request.POST['email'],
            'address': request.POST.get('address', ''),
            'city': request.POST.get('city', ''),
            'state': request.POST.get('state', '')
        }
        response = requests.put(api_url, json=data)
        
        if response.status_code == 200:
            return redirect('contacts')
        else:
            error_message = f'Error updating contact: {response.status_code}'
            return render(request, 'contact_manager/error.html', {'error_message': error_message})
    else:
        response = requests.get(api_url)
        
        if response.status_code == 200:
            contact_data = response.json()
            return render(request, 'contact_manager/contact_edit.html', {'contact': contact_data})
        else:
            error_message = f'Error fetching contact details: {response.status_code}'
            return render(request, 'contact_manager/error.html', {'error_message': error_message})


@login_required
def contact_delete(request, contact_id):
    api_url = f"http://localhost:8000/api/contacts/{contact_id}"
    
    if request.method == 'POST':
        response = requests.delete(api_url)
        if response.status_code == 204:
            return redirect('contacts')
        else:
            error_message = f'Error deleting contact: {response.status_code}'
            return render(request, 'contact_manager/error.html', {'error_message': error_message})
    else:
        response = requests.get(api_url)
        if response.status_code == 200:
            contact = response.json()
            return render(request, 'contact_manager/contact_delete.html', {'contact': contact})
        else:
            error_message = f'Error fetching contact details: {response.status_code}'
            return render(request, 'contact_manager/error.html', {'error_message': error_message})