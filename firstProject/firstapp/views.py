from django.shortcuts import render
def home(request):
    return render(request, 'firstapp/home.html')
# Create your views here.
