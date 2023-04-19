from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm

'''
# auth.user 이용 경우
class SignUpView(CreateView):
    form_class = UserCreationForm 
    success_url = reverse_lazy('login') 
    template_name = 'registration/signup.html'
'''

# customuser 이용 경우
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
