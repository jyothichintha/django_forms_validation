from django.shortcuts import render


# Create your views here.
from app.forms import *
from django.http import HttpResponse

def student(request):
    SFO=Student_form()
    d={'SFO':SFO}
    if request.method=='POST':
        FO=Student_form(request.POST)
        if FO.is_valid():
            return HttpResponse( str(FO.cleaned_data))

    return render(request,'student.html',d)
  