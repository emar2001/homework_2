from django.shortcuts import render

def index_view(request):
    return render(request,'index.html')

def contact_view(request):
    return render(request,'contact.html',{'phone':'901 559 3658','email':'mohamadrezaa.nasouri@gmail.com'})



