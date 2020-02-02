from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.urls import reverse
from django.template.defaultfilters import slugify
from accounts.models import *
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField



class Story(models.Model):
    title = models.CharField(("Title"), max_length=50)
    description = RichTextUploadingField(blank=True, null=True)
    cover = models.ImageField(_("Cover photo"), upload_to='cover/', height_field=None, width_field=None, max_length=None)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=("Author"), related_name='stories', on_delete=models.CASCADE)
    category = models.ForeignKey("Category", verbose_name=("Category"), related_name='stories', on_delete=models.CASCADE)
    tag = models.ManyToManyField("Tag", verbose_name=("Tags"))

    created_at = models.DateTimeField(("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(("Updated at"), auto_now=True)

    class Meta:
        db_table = 'Story'
        verbose_name = 'Story'
        verbose_name_plural = 'Stories'

    def __str__(self):
        return f'{self.title} | {self.updated_at}'


class Recipe(models.Model):
    title = models.CharField(("Recipe name"), max_length=50)
    short_decription = models.CharField(("Short description"), max_length=250)
    description = models.TextField(("Description"))

    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=("Author"), related_name='recipes', on_delete=models.CASCADE)
    category = models.ForeignKey("Category", verbose_name=("Category"), related_name='recipes', on_delete=models.CASCADE)
    tag = models.ManyToManyField("Tag", verbose_name=("recipes"))

    created_at = models.DateTimeField(("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(("Updated at"), auto_now=True)

    class Meta:
        db_table = 'Recipe'
        verbose_name = 'Recipe'
        verbose_name_plural = 'Recipes'

    def __str__(self):
        return f'{self.title} | {self.updated_at}'


class Category(models.Model):
    name = models.CharField(("Name"), max_length=50)
    image = models.ImageField(("Image"), upload_to=None, blank=True, null=True)

    created_at = models.DateTimeField(("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(("Updated at"), auto_now=True)

    class Meta:
        db_table = 'Category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f'{self.name}'


class Tag(models.Model):
    name = models.CharField(("Name"), max_length=50)
    is_active = models.BooleanField(_("Active"), default=0)
    
    created_at = models.DateTimeField(("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(("Updated at"), auto_now=True)

    class Meta:
        db_table = "Tag"
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        return f'{self.name}'


class Comment(models.Model):
    text = models.CharField(("Context"), max_length=50)

    parent = models.ForeignKey("self", verbose_name=("Reply"), related_name='children', on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=("Author"), related_name='comments', on_delete=models.CASCADE, null=True, blank=True)
    story = models.ForeignKey("Story", verbose_name=("Story"), related_name='comments', on_delete=models.CASCADE)

    created_at = models.DateTimeField(("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(("Updated at"), auto_now=True)

    class Meta:
        db_table = 'Comment'
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return f'{self.id} | {self.text} | {self.story} | {self.updated_at}'


class Subscribe(models.Model):
    email = models.EmailField(("E-mail"), max_length=254)
    
    created_at = models.DateTimeField(("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(("Updated at"), auto_now=True)

    class Meta:
        db_table = "Subscribe"
        verbose_name = "Subscriber"
        verbose_name_plural = "Subscribers"

    def __str__(self):
        return f'{self.email} | {self.updated_at}'


class Contact(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    email = models.EmailField(_("E-mail"), max_length=254)
    subject = models.CharField(_("Subject"), max_length=50)
    message = models.TextField(_("Subject"))

    created_at = models.DateTimeField(("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(("Updated at"), auto_now=True)


    class Meta:
        db_table = 'Contact'
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")

    def __str__(self):
        return f'{self.name} | {self.subject}'



