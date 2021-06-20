from django.shortcuts import HttpResponse
from django.shortcuts import render

# Widoki (Views)
# def hello(request):  # HTTP request
#     return HttpResponse("Witaj, świecie!")  # HTTP response


def hello(request):  # HTTP request
    return HttpResponse("<!DOCTYPE html><html><head><title>Witaj!</title></head><body><h2>Witaj, świecie!</h2></body></html>")  # HTTP response


def hello2(request):
    return render(
        request,
        "hello.html"
    )