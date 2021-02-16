from django.shortcuts import render

#sample
# Create your views here.
def home(request):
    return render(request,'index.html')