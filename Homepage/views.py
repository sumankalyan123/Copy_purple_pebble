from django.shortcuts import render

#sample12345678
# Create your views here.
def home(request):
    return render(request,'index.html')