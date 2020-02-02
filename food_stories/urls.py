from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


from ckeditor_uploader import views as uploader_views
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('stories.urls', namespace = 'stories')),
    path('accounts/', include('accounts.urls', namespace = 'accounts')),
    path('socials/', include('allauth.urls')),

    # path('ckeditor/', include('ckeditor_uploader.urls')),

    path('ckeditor/upload/',login_required(uploader_views.upload), name='ckeditor_upload'),
    path('ckeditor/browse/', never_cache(login_required(uploader_views.browse)), name='ckeditor_browse'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)