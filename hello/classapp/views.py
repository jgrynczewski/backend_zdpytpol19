from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from django.views import View
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from django.views.generic import CreateView

from classapp.models import Person
from classapp.forms import PersonForm

# function-based view
def hello(request):
    return HttpResponse("Hello, world!")


# class-based view
class HelloView(View):
    def get(self, request):
        return HttpResponse("Hello, world!")


#### Detail Page ####

# function-based view
def person_detail(request, id):
    p = get_object_or_404(Person, id=id)
    return render(
        request,
        'classapp/person_detail.html',
        context = {
            'person': p
        }
    )


# Class-based view
class PersonView(View):
    def get(self, request, id):
        p = get_object_or_404(Person, id=id)
        return render(
            request,
            'classapp/person_detail.html',
            context = {
                'person': p,
            }
        )


# Generic view
class PersonDetailView(DetailView):
    # domyślny szablon dla DetailView - person_detail.html
    model = Person
    template_name = 'classapp/person.html'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data()
        context['imie'] = 'Stefan'
        return context

################# CREATE PAGE #############################

# function-based view
def create_person(request):
    if request.method == "GET":
        form = PersonForm()

        return render(
            request,
            'classapp/create-person.html',
            context = {
                'form': form
            }
        )
    elif request.method == "POST":
        form = PersonForm(request.POST)
        form.save()

        return redirect('classapp:hello')


# class-based view
class PersonCreateView(View):
    def get(self, request):
        form = PersonForm()

        return render(
            request,
            'classapp/create-person.html',
            context={
                'form': form
            }
        )

    def post(self, request):
        form = PersonForm(request.POST)
        form.save()

        return redirect('classapp:hello')


# Generic view
class PersonCreateView3(CreateView):
    # domyślny szablon dla CreateView - person_form.html
    model = Person
    fields = "__all__"