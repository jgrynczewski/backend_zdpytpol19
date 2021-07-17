import random

from django.shortcuts import render

GOLDEN_THOUGHTS = [
    "Myśl 1",
    "Myśl 2",
    "Myśl 3"
]


def thought(request):
    t = random.choice(GOLDEN_THOUGHTS)

    return render(
        request,
        'golden_thoughts/thought.html',
        context = {
            'thought': t
        }
    )
