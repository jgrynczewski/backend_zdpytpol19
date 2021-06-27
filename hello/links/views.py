from django.shortcuts import render


# Create your views here.
def first(request):
    return render(
        request,
        'links/first_view.html'
    )

def second(request):
    return render(
        request,
        'links/second_view.html'
    )



def third(request, param):
    return render(
        request,
        'links/third_view.html',
        context={
            'param': param
        }
    )