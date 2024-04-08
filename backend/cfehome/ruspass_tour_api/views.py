import json

from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import Cityform
from rest_framework.decorators import api_view
from rest_framework.response import Response

#Choose the city to search for tours
@api_view(['POST'])
def get_city(request):
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

#
@api_view(['GET'])
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

