from .serializers import CitySerializer
from .models import Cities, Tours
from .serializers import CitySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

#Choose the city to search for tours
@api_view(['GET'])
def getCity(request,pk):
        city = Cities.objects.get(id=pk)
        serializer = CitySerializer(city)
        # check whether it's valid:
        if serializer.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:  return HttpResponseRedirect("/choose_tours/")
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

