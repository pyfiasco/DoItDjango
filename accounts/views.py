from django.contrib.auth.forms import UserCreationForm # django wprhd 계정관련 form
from django.urls import reverse_lazy 
from django.views.generic import CreateView
from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
