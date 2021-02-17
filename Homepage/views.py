from django.shortcuts import render

#samplefromwindowsfrom here
# Create your views here.
def home(request):
    return render(request,'index.html')

#gallery
def services_page(request):
    return render(request,'index-1.html')



def contact_us(request):
    return render(request,'index-4.html')

def blog(request):
    return render(request,'index-3.html')