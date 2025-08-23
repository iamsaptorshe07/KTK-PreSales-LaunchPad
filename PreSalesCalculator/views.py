# Django Packages
from django.shortcuts import render, redirect
from django.http import *
from .models import ReferenceCapacity,InfraSetUpReference
from django.db.models import Q
from django.contrib import messages


# Other Modules
import datetime

# Create your views here.

def home(request):
    
    referenceCapacity_model = ReferenceCapacity.objects.all().order_by('object_type','level')
    distinct_reference_object = ReferenceCapacity.objects.values_list('object_type', flat=True).distinct()
    infra_setup_reference = InfraSetUpReference.objects.all().order_by('object_type','method')
    unique_infra_method = InfraSetUpReference.objects.values_list('method',flat=True).distinct()
    unique_infra_object = InfraSetUpReference.objects.values_list('object_type',flat=True).distinct()
    context = {
        'reference_values':referenceCapacity_model,
        'reference_objects':distinct_reference_object,
        'Infrasetup_reference':infra_setup_reference,
        "UniqueInfraSetupMethod":unique_infra_method,
        'UniqueInfraObject':unique_infra_object
        }
    return render(request,'index.html',context=context)