import json

from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import Cityform

def get_city(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = Cityform(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("/choose_tours/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = Cityform()

    return render(request, "search_city_form.html", {"form": form})

def api_home(request):
    body = request.body
    data = {}
    try:
        data = json.loads(body)  # this converts json data into python dict
    except:
        pass
    print(data)
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    return JsonResponse(data)

