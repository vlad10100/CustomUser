from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views.generic import CreateView, TemplateView

from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView 
from django.contrib.auth.forms import UserCreationForm

from .forms import CustomUserForm

from .models import CustomUser 




class UserSignUpView(CreateView):
    template_name = 'signup_page.html'
    form_class = CustomUserForm

    def get_success_url(self):
        return reverse_lazy('accounts:login_page')

    # def form_valid(self, form):
    #     user = form.save(commit=False)
    #     user.save()
    #     return super(UserSignUpView, self).form_valid(form)
    



class UserLogInView(LoginView):
    template_name = 'login_page.html'
    fields = '__all__'
    
    def get_success_url(self):
        return reverse_lazy('accounts:home_page')


class HomePage(TemplateView):
    template_name = 'home_page.html'

    def get_success_url(self):
        return reverse_lazy('accounts:home_page')
