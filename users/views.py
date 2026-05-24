from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# Create your views here.
def index(requrest):
    return HttpResponse("<h1>Hello Django!</h1>")


def profile(request):
    context = {
        "name": "Karen",
        "age": 40,
        "height": 157,
        "weight": 60,
    }

    return JsonResponse(context)
