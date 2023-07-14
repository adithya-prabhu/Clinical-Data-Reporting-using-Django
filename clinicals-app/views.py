from django.shortcuts import render,redirect
from .models import Patient,ClinicalData
from .forms import PatientForm,ClinicalDataForm
from django.http import HttpResponse
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.


class PatientListView(LoginRequiredMixin,ListView):
    model=Patient
    

class PatientCreateView(CreateView):
    model=Patient
    success_url=reverse_lazy('index')
    fields=('firstname','lastname','age')

class PatientUpdateView(UpdateView):
    model=Patient
    success_url=reverse_lazy('index')
    fields=('firstname','lastname','age')

class PatientDeleteView(DeleteView):
    model=Patient
    success_url=reverse_lazy('index')


def ClinicalAdd(request,**kwargs):
    form=ClinicalDataForm()
    patient=Patient.objects.get(id=kwargs['pk'])
    if request.method=='POST':
        form=ClinicalDataForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'clinicalsapp/clinicaladd.html',{'form':form,'patient':patient})

def analyze(request,**kwargs):
    data=ClinicalData.objects.filter(patient_id=kwargs['pk'])
    responsedata=[]
    for eachentry in data:
        if eachentry.componentName=='hw':
            heightandweight=eachentry.componenetValue.split('/')
            if len(heightandweight) > 1:
                feetTometers=float(heightandweight[0])*0.4536
                BMI=(float(heightandweight[1]))/(feetTometers*feetTometers)
                bmientry=ClinicalData()
                bmientry.componentName='BMI'
                bmientry.componenetValue=BMI
                responsedata.append(bmientry)
        responsedata.append(eachentry)
    return render(request,'clinicalsapp/generatereport.html',{'data':responsedata})

def logout(request):
    return render(request,'clinicalsapp/logout.html')