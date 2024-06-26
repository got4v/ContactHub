from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from contact_manager.views import RegisterView, display_contact_details, display_contact_list, contact_edit, contact_delete
from contact_manager.api import api

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('contacts/', display_contact_list, name='contacts'),
    path('contacts/<int:contact_id>/', display_contact_details, name='contact_details'),
    path('contacts/<int:contact_id>/edit/', contact_edit, name='contact_edit'),
    path('contacts/<int:contact_id>/delete/', contact_delete, name='contact_delete'),
    path("api/", api.urls),
]