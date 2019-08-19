from django.urls import path, include

from .views import SignUpView, profile

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('<str:username>', profile, name='profile'),
]