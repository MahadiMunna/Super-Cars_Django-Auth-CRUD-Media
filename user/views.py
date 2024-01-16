from django.shortcuts import render, redirect
from . import forms
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.views.generic import View
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from cars.models import Owner


# Create your views here.
def register(request):
    if request.method == 'POST':
        register_form = forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request,'Account created successfully')
            return redirect('login')
    else:
        register_form = forms.RegistrationForm()
    return render(request, 'form.html', {'form': register_form, 'type':'Register'})

class UserLoginView(LoginView):
    template_name = 'form.html'
    def get_success_url(self):
        return reverse_lazy('profile')
    def form_valid(self, form):
        messages.success(self.request, 'Logged In Successfully')
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.warning(self.request, 'User Information is incorrect')
        return super().form_invalid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context
    
class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')

@login_required
def profile(request):
    owner = Owner.objects.get(owner=request.user)
    data = owner.purchased_cars.all()
    return render(request, 'profile.html', {'data': data})

@login_required
def editProfile(request):
    if request.method == 'POST':
        profileform = forms.EditProfile(request.POST, instance = request.user)
        if profileform.is_valid():
            profileform.save()
            messages.success(request,'Profile updated successfully')
            return redirect('profile')
    else:
        profileform = forms.EditProfile(instance = request.user)
    return render(request, 'form.html', {'form': profileform, 'type':'Edit Profile'})