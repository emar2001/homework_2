from django.shortcuts import render

def index_view(request):
    return render(request,'index.html')

def email_view(request):
    return render(request,'email.html')

def phone_view(request):
    return render(request,'phone.html')

