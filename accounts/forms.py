from django import forms
from accounts.models import (User, )
from django.contrib.auth.forms import (UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm, PasswordResetForm, SetPasswordForm, )


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'placeholder' : 'First name',
                'class' : 'form-control',
                'autofocus': 'autofocus',
            }))

    last_name = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'placeholder' : 'Last name',
                'class' : 'form-control',
            }))

    username = UsernameField(
        widget = forms.TextInput(
            attrs={
                'placeholder' : 'Username',
                'class' : 'form-control',
            }))

    email = forms.EmailField(
        widget = forms.EmailInput(
            attrs={
                'placeholder' : 'Email',
                'class' : 'form-control',
            }))

    password1 = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'placeholder' : 'Password',
                'class' : 'form-control',
            }))

    password2 = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'placeholder' : 'Confirm password',
                'class' : 'form-control',
             }))

    class Meta:
        model = User
        fields = ('first_name', 'last_name' ,"username", 'email', 'password1', 'password2', )


class LoginForm(AuthenticationForm):
    username = UsernameField(
        widget = forms.TextInput(
            attrs={
                'placeholder' : 'Username',
                'class' : 'form-control',
            }))

    password = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'placeholder' : 'Password',
                'class' : 'form-control',
            }))
    
    class Meta:
        model = User
        fields = ("username", 'password', )


class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'placeholder' : 'Old password',
                'class' : 'form-control',
            }))

    new_password1 = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'placeholder' : 'New password',
                'class' : 'form-control',
            }))

    new_password2 = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'placeholder' : 'Re-enter new password',
                'class' : 'form-control',
            }))

    class Meta:
        fields = ("old_password", 'new_password1', 'new_password2', )


class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'autocomplete': 'email',
                'placeholder' : 'Email',
                'class' : 'form-control',
                }))

    class Meta:
        fields = ("email", )


class PasswordResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'placeholder' : 'New password',
                'class' : 'form-control',
             }))
    
    new_password2 = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'placeholder' : 'Re-enter new password',
                'class' : 'form-control',
             }))

    class Meta:
        fields = ("new_password1", 'new_password2', )


class ProfileEditForm(forms.ModelForm):
    first_name = forms.CharField(
        label = 'Name',
        widget = forms.TextInput(
            attrs={
                'placeholder' : 'First name',
                'class' : 'form-control',
                'autofocus': 'autofocus',
            }))

    last_name = forms.CharField(
        label = 'Surname',
        widget = forms.TextInput(
            attrs={
                'placeholder' : 'Last name',
                'class' : 'form-control',
            }))

    username = UsernameField(
        label = 'Username',
        widget = forms.TextInput(
            attrs={
                'placeholder' : 'Username',
                'class' : 'form-control',
            }))

    email = forms.EmailField(
        label = 'E-mail',
        widget = forms.EmailInput(
            attrs={
                'placeholder' : 'Email',
                'class' : 'form-control',
            }))

    bio = forms.CharField(
        label = 'Bio',
        widget = forms.TextInput(
            attrs={
                'placeholder' : 'Last name',
                'class' : 'form-control',
            }))

    class Meta:
        model = User
        fields = ('first_name', 'last_name' ,"username", 'email', 'bio', )

