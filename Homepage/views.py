from django.shortcuts import render

#samplefromwindowsfrom here
# Create your views here.
def home(request):
    return render(request,'index.html')


def services_page(request):
    return render(request,'index-1.html')