from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'a':240,'b':2409,'c':78909876}
    return render(request,'conditions.html',d)

def loops(request):
    d={'name':'ASHU'}
    return render(request,'loops.html',d)