from django.shortcuts import render

#sample123456
# Create your views here.
def home(request):
    return render(request,'index.html')