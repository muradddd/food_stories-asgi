from django.shortcuts import render
from django.http import JsonResponse
from django.urls import reverse_lazy

from .models import *
from .forms import *
from .serializers import *
from .mixins import *

from accounts.models import (User,)

from django.views.generic import *
from django.views.generic.edit import (FormMixin, ModelFormMixin, )
from django.contrib.auth.mixins import (LoginRequiredMixin, )
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.views import APIView




def about_page(request):
    return render(request, 'about.html')

def stories_page(request):
    return render(request, 'stories.html')

def recipes_page(request):
    return render(request, 'recipes.html')


def email_subscribers(request):
    return render(request, 'email-subscribers.html')

def single(request):
    return render(request, 'single.html')


class HomePageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            'last_4_stories' : Story.objects.order_by('created_at').reverse()[:4],
            'first_3_categories' : Category.objects.order_by('created_at')[:3],
            'last_2_recipes' : Recipe.objects.order_by('created_at').reverse()[:2],
            'categories' : Category.objects.all(),
            'recipes' : Recipe.objects.all(),
            'stories' : Story.objects.all(),
            'stories_count' : Story.objects.all().count(),
            'recipes_count' : Recipe.objects.all().count(),
            'authors_count' : User.objects.all().count(),
        }
        return context
    



class ContactCreateView(CreateView):
    form_class = ContactForm
    template_name = "contact.html"
    success_url = reverse_lazy('stories:contact')


class SubscribeCreateView(CreateView):
    form_class = SubscribeForm
    http_method_names = ('post', )

    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER')


class StoryCreateView(LoginRequiredMixin, CreateView):
    form_class = StoryForm
    template_name = "create_story.html"

    def get_success_url(self):
        return reverse_lazy('accounts:user-profile', kwargs={'pk': self.request.user.id})

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['formset'] = StoryFormSet
    #     return context

    def form_valid(self, form):
        print('DDDDDDDDD', self.request.POST)
        form.instance.user = self.request.user
        form.instance.save()
        tags = self.request.POST.get('tag').split(',')
        print('CCCCCCCCC', tags)
        for tag in tags:
            tag_obj, created = Tag.objects.get_or_create(name=tag.upper())
            form.instance.tag.add(tag_obj.id)
        return super(StoryCreateView, self).form_valid(form)



class StoryEditView(LoginRequiredMixin, StoryEditMixin, UpdateView):
    model = Story
    form_class = StoryForm
    template_name = "create_story.html"
    
    def get_success_url(self):
        return reverse_lazy('accounts:user-profile', kwargs={'pk': self.request.user.id})


class StoryDeleteView(LoginRequiredMixin, StoryEditMixin, DeleteView):
    model = Story

    def get_success_url(self):
        return reverse_lazy('accounts:user-profile', kwargs={'pk': self.request.user.id})


class StoryDetailView(FormMixin, DetailView):
    model = Story
    form_class = CommentForm
    template_name = "single.html"

    def get_success_url(self):
        return reverse_lazy("stories:story-detail", kwargs={"pk": self.object.pk})

    def get_context_data(self, **kwargs):
        context = super(StoryDetailView, self).get_context_data(**kwargs)
        context["comment_form"] = self.get_form()
        context['tags'] = self.object.tag.filter(is_active=True)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        parent_id = self.request.POST.get('parent')
        form.instance.user = self.request.user
        form.instance.story = self.get_object()
        if parent_id:
            form.instance.parent = Comment.objects.filter(id=parent_id).first()
        else:
            form.instance.parent = None
        form.save()
        return super().form_valid(form)


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    # serializers = {
    #     'default': StorySerializer,
    #     'create': StorySerializer,
    #     'destroy': StorySerializer,
    #     'update': StorySerializer,
    #     'partial_update': StorySerializer,
    #     'list': StorySerializer,
    #     'retrieve': StorySerializer
    # }

    # def get_serializer_class(self):
    #     return self.serializers.get(self.action)

    def get_queryset(self):
        tag = self.request.GET.get('tag', '')
        try:
            obj = Tag.objects.get(name=tag)
        except:
            print('yoxdur')
        return self.queryset.filter(name__icontains=tag, is_active=True)
    
