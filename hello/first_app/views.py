from django.shortcuts import render


# Create your views here.
def first(request):
    return render(
        request,
        'first_app/first.html'
    )