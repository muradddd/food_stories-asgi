from django.urls import path, include
from .views import *

from .routers import router


app_name = 'stories'

urlpatterns = [
    path('', HomePageView.as_view(), name = 'home' ),
    path('about/', about_page, name = 'about' ),
    path('contact/', ContactCreateView.as_view(), name = 'contact' ),
    path('stories/', stories_page, name = 'stories' ),
    path('recipes/', recipes_page, name = 'recipes' ),
    path('email-subscribers/', email_subscribers, name = 'email-subscribers'),
    path('single/', single, name = 'single'),


# story
    path('create-story/', StoryCreateView.as_view(), name = 'create-story'),
    path('edit-story/<int:pk>/', StoryEditView.as_view(), name = 'edit-story' ),
    path('delete-story/<int:pk>/', StoryDeleteView.as_view(), name = 'delete-story' ),
    path('story/<int:pk>/', StoryDetailView.as_view(), name = 'story-detail' ),
# subscribe
    path('subscribe/', SubscribeCreateView.as_view(), name = 'subscribe' ),
# rest-api
    path('', include(router.urls)),
]
