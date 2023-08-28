from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView, TemplateView
from django.contrib.auth import login, authenticate, logout
from .forms import RegistrationForm, LoginForm



class RegisterView(CreateView):
    form_class = RegistrationForm
    template_name = 'register.html'
    success_url = reverse_lazy('ads-list')

    def form_vaild(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_vaild(form)

class LoginView(LoginView):
    form_class = LoginForm
    template_name = 'login.html'
    

    def get_success_url(self):
        return reverse_lazy('ads-list')
         
class ProfileView(TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

class LogoutView(LogoutView):
    next_page = reverse_lazy('ads-list')


