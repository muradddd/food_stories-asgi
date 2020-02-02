from django.urls import path
from .views import *
from accounts.views import (RegisterView, CustomLoginView, CustomPasswordChangeView, CustomPasswordResetView, CustomPasswordResetConfirmView, ProfileEditView, )
from django.contrib.auth.views import (LogoutView, )

app_name = 'accounts'

urlpatterns = [
    path('register/', RegisterView.as_view(), name = 'register'),
    path('login/', CustomLoginView.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(), name = 'logout'),
    path('change-password/', CustomPasswordChangeView.as_view(), name = 'change-password'),
    path('forget-password/', CustomPasswordResetView.as_view(), name = 'forget-password'),
    path('password-reset-confirm/<str:uidb64>/<str:token>/', CustomPasswordResetConfirmView.as_view(), name = 'password-reset-confirm'),

    path('user-profile/<int:pk>/', UserProfileView.as_view(), name = 'user-profile'),
    path('user-profile-redirect/', UserProfileRedirectView.as_view(), name = 'user-profile-redirect'),
    path('edit-profile/<int:pk>/', ProfileEditView.as_view(), name = 'edit-profile'),
]
