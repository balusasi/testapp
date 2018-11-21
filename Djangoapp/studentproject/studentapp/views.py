from django.shortcuts import render
from .forms import StudentForm
from .models import Student
# Create your views here.
def homepage(request):
    template_name='home.html'
    return render(request,template_name)

def addstudent(request):
    form=StudentForm()
    template_name='addstudentdetails.html'
    context={'form':form}
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return homepage(request)
    return render(request,template_name,context)

def displaydetails(request):
    records=Student.objects.all()
    template_name='displaystudentdetails.html'
    context={'records':records}
    return render(request,template_name,context)