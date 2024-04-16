from .serializers import CitySerializer
from .models import Cities, Tours
from .serializers import CitySerializer, TourSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Choose the city to search for tours
@api_view(['GET'])
def getCity(request, pk, format=None):
    city = Cities.objects.get(id=pk)
    serializer = CitySerializer(city)
    return Response(serializer.data)

@api_view(['GET'])
def getTours(request, format=None):
    tours = Tours.objects.all()
    serializer = TourSerializer(tours, many = True)
    return Response(serializer.data)
@api_view(['GET'])
def getTour(request, pk, format=None):
    tour = Tours.objects.get(id=pk)
    serializer = TourSerializer(tour, many = False)
    return Response(serializer.data)
