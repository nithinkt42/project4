from django.shortcuts import render

def html5(request):
    return render(request,'temp2/html5.html')

def calicut(request):
    return render(request,'temp2/calicut.html')    

def alappuzha(request):
    return render(request,'temp2/alappuzha.html')  

def idukki(request):
    return render(request,'temp2/idukki.html')
def kochi(request):
    return render(request,'temp2/kochi.html')

def wayanad(request):
    return render(request,'temp2/wayanad.html')