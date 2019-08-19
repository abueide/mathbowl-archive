from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404

# Create your views here.
# users/views.py
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm


def profile(request, username):
    context = {'user': get_object_or_404(get_user_model(), )}
    return render(request, 'user/profile.html', context)


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/templates/signup.html'
