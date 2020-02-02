from django import forms
from django.forms import modelformset_factory, inlineformset_factory, formset_factory
from stories.models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from ckeditor.widgets import CKEditorWidget


class ContactForm(forms.ModelForm):
    name = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'placeholder' : 'Your Name',
                'class': 'form-control',
            }))
    email = forms.EmailField(
        widget = forms.EmailInput(
            attrs={
                'placeholder' : 'Your Email',
                'class': 'form-control',
            }))
    subject = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'placeholder' : 'Subject',
                'class': 'form-control',
            }))
    message = forms.CharField(
        widget = forms.Textarea(
            attrs={
                'placeholder' : 'Your Message',
                'class': 'form-control',
                'cols' : '30',
                'rows' : '7',
            }))

    class Meta:
        model = Contact
        fields = ('name', 'email', 'subject', 'message', )


class SubscribeForm(forms.ModelForm):
    email = forms.EmailField(
    widget = forms.EmailInput(
        attrs={
            'placeholder' : 'Enter email address',
            'class': 'form-control',
        }))

    class Meta:
        model = Subscribe
        fields = ('email', )


class StoryForm(forms.ModelForm):
    title = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'placeholder' : 'Title',
                'class': 'form-control',
            }))
    cover = forms.ImageField(label='Cover photo')
    description = forms.CharField(
        widget=CKEditorUploadingWidget(
            attrs={
                'placeholder' : 'Title',
                'class': 'form-control',
            }))

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label= 'Select category',
        widget = forms.Select(
            attrs={
                'class': 'form-control',
            }))
    # tag = forms.CharField(
    #     required=False,
    #     widget = forms.TextInput(
    #         attrs={
    #             'placeholder' : 'Insert your tags (seperate with " ; ")',
    #             'class': 'form-control',
    #         }))

    class Meta:
        model = Story
        fields = ('title', 'cover', 'description', 'category',  )


class CommentForm(forms.ModelForm):
    name = forms.CharField(
        required=False,
        label = 'Name',
        widget = forms.TextInput(
            attrs={
                'class': 'form-control',
            }))
    email = forms.EmailField(
        required=False,
        label = 'Email',
        widget = forms.EmailInput(
            attrs={
                'class': 'form-control',
            }))
    text = forms.CharField(
        label = 'Message',
        widget = forms.Textarea(
            attrs={
                'class': 'form-control',
                'cols' : '30',
                'rows' : '10',
            }))
    
    class Meta:
        model = Comment
        fields = ('name', 'email', 'text', )

