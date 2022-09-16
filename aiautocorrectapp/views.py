from django.shortcuts import render
from . import models
# Create your views here.

def get_homepage(request):

    context = {}
    return render(request, "aiautocorrectapp/index.html", context)