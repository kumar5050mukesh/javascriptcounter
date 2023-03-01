from django.shortcuts import render
from django.urls import path

def test(request):
    return render(request, "index.html")
