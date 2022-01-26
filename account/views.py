from django.shortcuts import render

from django.views.generic import CreateView 

from .forms import CustomUserCreationForm

from django.urls import reverse_lazy


class SignUpView(CreateView):
    template_name = 'signup.html'
    form_class = CustomUserCreationForm 

    def get_success_url(self):
        return reverse_lazy('account:signup_view')