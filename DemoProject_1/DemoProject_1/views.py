from django.http import HttpResponse
from django.shortcuts import render

def Home(request):
   # return HttpResponse("<h1>Welcome to django</h1>");
   return render(request,"websites/index.html");

def About(request):
   # return HttpResponse("<h1>This is about page</h1>");
   return render(request,"websites/about.html");

def Contact(request):
   # return HttpResponse("<h1>This is contact page</h1>");
   return render(request,"websites/contact.html");