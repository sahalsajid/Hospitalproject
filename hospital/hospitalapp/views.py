from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def doctors(request):
    return render(request,'doctors.html')

def department(request):
    return render(request,'department.html')

def contact(request):
    return render(request,'contact.html')

def booking(request):
    return render(request,'booking.html')
    
def about(request):
    return render(request,'about.html')