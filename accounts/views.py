from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import *
from django.contrib.auth.views import (LoginView, PasswordChangeView, PasswordResetView, PasswordResetConfirmView, )

from .forms import *
from .models import *
from .mixins import *

from stories.models import *

from django.contrib.auth.mixins import (LoginRequiredMixin, )





class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = "register.html"
    success_url = reverse_lazy('accounts:login')


class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'login.html'


class CustomPasswordChangeView(PasswordChangeView):
    form_class = CustomPasswordChangeForm
    template_name = "change_password.html"
    success_url = reverse_lazy('accounts:login')


class CustomPasswordResetView(PasswordResetView):
    template_name= "forget_password.html" 
    success_url = reverse_lazy('accounts:login')
    email_template_name = 'password_reset_email.html'
    form_class = CustomPasswordResetForm


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name= "reset_password.html" 
    success_url = reverse_lazy('accounts:login')
    form_class = PasswordResetConfirmForm


class UserProfileView(LoginRequiredMixin,DetailView):
    model = User
    template_name = "user-profile.html"

    def get_success_url(self):
        return reverse_lazy("accounts:user-profile", kwargs={"pk": self.object.pk})

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        context['stories'] = Story.objects.filter(user=self.object.pk)
        return context



class UserProfileRedirectView(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, **kwargs):
        return reverse_lazy('accounts:user-profile', kwargs={'pk': self.request.user.id})




class ProfileEditView(LoginRequiredMixin, ProfileEditMixin, UpdateView):
    model = User
    form_class = ProfileEditForm
    template_name = "edit_profile.html"
    success_url = reverse_lazy('stories:user-profile')
