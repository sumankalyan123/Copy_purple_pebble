from django.shortcuts import render

#samplefromwindows
# Create your views here.
def home(request):
    return render(request,'index.html')