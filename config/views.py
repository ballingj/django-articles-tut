from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.forms import UserCreationForm

class SignupView(CreateView):
  form_class = UserCreationForm
  success_url = reverse_lazy('login')
  template_name = "registration/signup.html"

