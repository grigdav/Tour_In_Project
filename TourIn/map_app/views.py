from django.shortcuts import render

from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse

from .models import *

class HomePageView(TemplateView):
	template_name = 'index.html'
