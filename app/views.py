from django.shortcuts import render,HttpResponse

def home(request):
    return HttpResponse('<h1> hellooooooo</h1>')
def index(request):
    return render(request,'new.html')