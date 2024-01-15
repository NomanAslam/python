from django.shortcuts import render

def receipes(request):
    return render(request, "receipes/receipes.html")
