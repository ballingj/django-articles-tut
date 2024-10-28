# from django.shortcuts import render, redirect


#built-in TemplateView to display a template
from django.views.generic import TemplateView


class HomePageView(TemplateView):
  template_name = 'pages/home.html'

class AboutPageView(TemplateView):
  template_name = 'pages/about.html'

