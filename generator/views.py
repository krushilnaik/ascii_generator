from django.shortcuts import render

# Create your views here.


def index(request):
    response = "yes"

    return render(request, "generator/home.html", {
        "content": response
    })
