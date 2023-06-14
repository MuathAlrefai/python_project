from django.shortcuts import render, redirect

def halls(request):
    return render(request, 'halls.html')