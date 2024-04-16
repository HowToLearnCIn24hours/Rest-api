from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.getCity),
    path('tours/', views.getTours),
    path('tours/<str:pk>', views.getTour),
]

urlpatterns = format_suffix_patterns(urlpatterns)