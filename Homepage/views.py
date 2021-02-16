from django.shortcuts import render

#sample123
# Create your views here.
def home(request):
    return render(request,'index.html')