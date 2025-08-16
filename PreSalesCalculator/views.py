# Django Packages
from django.shortcuts import render, redirect
from django.http import *
from .models import ReferenceCapacity
from django.db.models import Q
from django.contrib import messages


# Other Modules
import datetime

# Create your views here.

def home(request):
    referenceCapacity_model = ReferenceCapacity.objects.all()
    distinct_reference_object = ReferenceCapacity.objects.values_list('object_type', flat=True).distinct()
    context = {
        'reference_values':referenceCapacity_model,
        'reference_objects':distinct_reference_object
        }
    return render(request,'index.html',context=context)